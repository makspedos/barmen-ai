from typing_extensions import Annotated, TypedDict
import os
from langchain_openai import ChatOpenAI

class GroundedGrade(TypedDict):
    explanation: Annotated[str, ..., "Explain your reasoning for the score"]
    grounded: Annotated[
        bool, ..., "Provide the score on if the answer hallucinates from the documents"
    ]

# Grade prompt
grounded_instructions = """You are a model grading barman that provides cocktails recommendation. You will be given FACTS and a BARMEN ANSWER. Here is the grade criteria to follow:
(1) Ensure the BARMEN ANSWER is grounded in the FACTS. (2) Ensure the BARMEN ANSWER does not contain "hallucinated" information outside the scope of the FACTS.

Grounded:
A grounded value of True means that the barman's answer meets all of the criteria.
A grounded value of False means that the barman's answer does not meet all of the criteria.

Explain your reasoning in a step-by-step manner to ensure your reasoning and conclusion are correct. Avoid simply stating the correct answer at the outset."""

# Grader LLM
grader_llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"), temperature=0).with_structured_output(GroundedGrade, method="json_schema", strict=True)


# Evaluator
def groundedness(inputs: dict, outputs: dict) -> dict:
    """A simple evaluator for RAG answer groundedness."""
    doc_string = "\n\n".join(doc.page_content for doc in outputs["documents"])
    answer = f"FACTS: {doc_string}\nBARMEN ANSWER: {outputs['answer']}"
    grade = grader_llm.invoke([
        {"role": "system", "content": grounded_instructions},
        {"role": "user", "content": answer}
    ])
    return {
        "key": "groundedness",
        "score": 1 if grade['grounded'] else 0,
        "comment": grade['explanation']
    }