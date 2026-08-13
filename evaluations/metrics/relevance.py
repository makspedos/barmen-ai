from langchain_openai import ChatOpenAI
from typing_extensions import Annotated, TypedDict
import os

class RelevanceGrade(TypedDict):
    explanation: Annotated[str, ..., "Explain your reasoning for the score"]
    relevant: Annotated[
        bool, ..., "Provide the score on whether the answer addresses the question"
    ]

relevance_instructions = """You are a model grading barman that provides cocktails recommendation . You will be given a QUESTION and a BARMEN ANSWER. Here is the grade criteria to follow:
(1) Ensure the barman ANSWER is concise and relevant to the QUESTION
(2) Ensure the barman ANSWER helps to answer the QUESTION

Relevance:
A relevance value of True means that the barman's answer meets all of the criteria.
A relevance value of False means that the barman's answer does not meet all of the criteria.

Explain your reasoning in a step-by-step manner to ensure your reasoning and conclusion are correct. Avoid simply stating the correct answer at the outset."""


grader_llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"), temperature=0).with_structured_output(RelevanceGrade, method="json_schema", strict=True)

# Evaluator
def relevance(inputs: dict, outputs: dict) -> dict:
    """A simple evaluator for RAG answer helpfulness."""
    answer = f"QUESTION: {inputs['question']}\nSTUDENT ANSWER: {outputs['answer']}"
    grade = grader_llm.invoke([
        {"role": "system", "content": relevance_instructions},
        {"role": "user", "content": answer}
    ])
    return {
        "key": "relevance",
        "score": 1 if grade['relevant'] else 0,
        "comment": grade['explanation']
    }