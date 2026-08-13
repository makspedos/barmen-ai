from langchain_openai import ChatOpenAI
from typing_extensions import Annotated, TypedDict
import os

class CorrectnessGrade(TypedDict):
    explanation: Annotated[str, ..., "Explain your reasoning for the score"]
    correct: Annotated[bool, ..., "True if the answer is correct, False otherwise."]

correctness_instructions = """You are a model grading barman that provides cocktails recommendation .  You will be given a QUESTION,  the GROUND TRUTH (correct) ANSWER and a BARMEN ANSWER. Here is the grade criteria to follow:
(1) Grade the barman answers based ONLY on their factual accuracy relative to the ground truth answer.
(2) Ensure that the barman answer does not contain any conflicting statements.
(3) It is OK if the barman answer contains more information than the ground truth answer, as long as it is factually accurate relative to the  ground truth answer.

Correctness:
A correctness value of True means that the barman's answer meets all of the criteria.
A correctness value of False means that the barman's answer does not meet all of the criteria.

Explain your reasoning in a step-by-step manner to ensure your reasoning and conclusion are correct. Avoid simply stating the correct answer at the outset."""


grader_llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"), temperature=0).with_structured_output(CorrectnessGrade, method="json_schema", strict=True)

def correctness(inputs: dict, outputs: dict, reference_outputs: dict) -> dict:
    """An evaluator for RAG answer accuracy"""
    answers = f"""\
QUESTION: {inputs['question']}
GROUND TRUTH ANSWER: {reference_outputs['answer']}
MODEL ANSWER: {outputs['answer']}"""
    # Run evaluator
    grade = grader_llm.invoke([
        {"role": "system", "content": correctness_instructions},
        {"role": "user", "content": answers}
    ])
    return {
        "key":"correctness",
        "score":1 if grade['correct'] else 0,
        "comment": grade['explanation']
    }
