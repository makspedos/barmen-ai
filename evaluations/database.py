from langsmith import Client

client = Client()

examples = [
    {
        "inputs": {
            "question": "Which cocktail contains rum, lime juice, sugar, mint, and soda water?"
        },
        "outputs": {
            "answer": "A Mojito contains white rum, lime juice, sugar, mint leaves, and soda water.",
        },
    },
    {
        "inputs": {
            "question": "What glass should I use for a Mojito?"
        },
        "outputs": {
            "answer": "A highball glass.",
        },
    },
    {
        "inputs": {
            "question": "Do you have a strong cocktail with gin and lemon peel? But I prefer carbonated water rather than ginger"
        },
        "outputs": {
            "answer": "English Highball, served in a Highball glass.",
        },
    },
    {
        "inputs": {
            "question": "I like Kahlua in my cocktails, what do you have? But don't provide cocktails with word Kahlua in the name"
        },
        "outputs": {
            "answer": "Espresso Martini.",
        },
    },
    {
        "inputs": {
            "question": "We need some punch drinks for a party, what do you have? Especially with weird name"
        },
        "outputs": {
            "answer": "Brain Fart.",
        },
    },
    {
        "inputs": {
            "question": "Provide me some ordinary rum drink, something like Caipirinha."
        },
        "outputs": {
            "answer": "Caipirissima.",
        },
    },
    {
        "inputs": {
            "question": "I don't drink alcohol, but I want something hot with milk, maybe chocolate."
        },
        "outputs": {
            "answer": "Drinking Chocolate.",
        },
    },
    {
        "inputs": {
            "question": "Fruit boom. I like a non-alcoholic fruit cocktail. It should contain at least apple and strawberries, maybe bananas."
        },
        "outputs": {
            "answer": "Fruit Cooler.",
        },
    },
    {
        "inputs": {
            "question": "I want pizza cocktail"
        },
        "outputs": {
            "answer": "There is no available pizza cocktail in our menu",
        },
    },
    {
        "inputs": {
            "question": "SOme weird question"
        },
        "outputs": {
            "answer": "Please, provide more relevant question. Until then, take those cocktails as an answer",
        },
    },
]

dataset_name = "Cocktails_Q&A"
try:
    dataset = client.read_dataset(dataset_name=dataset_name)
except Exception:
    dataset = client.create_dataset(dataset_name=dataset_name)

client.create_examples(
    dataset_id = dataset.id,
    examples=examples
)