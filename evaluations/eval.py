from backend.services.langchain_prompt import LangchainService
from backend.services.llm_service import LLMService
from langsmith import evaluate
from database import *
import asyncio
from evaluations.metrics.correctness import correctness
from evaluations.metrics.relevance import relevance
from evaluations.metrics.retrieval_relevance import retrieval_relevance
from evaluations.metrics.groundedness import groundedness

model = LangchainService()
def predict_rag_answer(data: dict):
    response = asyncio.run(model.make_prompt(data["question"]))

    if response is None:
        return {
            "answer": "Please, make relevant or more understandable request."
        }

    model_response = response["answer"]

    cocktail_response = ""

    for cocktail in response["cocktails"]:
        if cocktail.get("name"):
            cocktail_response += f"\nName: {cocktail['name']}\n"

        if cocktail.get("ingredients"):
            cocktail_response += "Ingredients:\n"
            cocktail_response += "\n".join(
                f"- {ingredient}"
                for ingredient in cocktail["ingredients"]
            )

        if cocktail.get("instructions"):
            cocktail_response += "\nInstructions:\n"
            cocktail_response += "\n".join(cocktail["instructions"])

        if cocktail.get("glass"):
            cocktail_response += f"\nGlass: {cocktail['glass']}\n"

    return {
        "answer": model_response + "\n" + cocktail_response,
        "documents": response['documents']
    }

results = client.evaluate(
    predict_rag_answer,
    data = dataset,
    evaluators=[correctness, groundedness, relevance, retrieval_relevance],
)

print(results)