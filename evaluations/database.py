from langsmith import Client

client = Client()

examples = [
    {
        "inputs": {
            "question": "Which cocktail contains rum, lime juice, sugar, mint, and soda water?"
        },
        "outputs": {
            "answer": "Mojito"
        },
    },
    {
        "inputs": {
            "question": "What glass should I use for a Mojito?"
        },
        "outputs": {
            "answer": "Highball glass"
        },
    },
    {
        "inputs": {
            "question": "Do you have a strong cocktail with gin and lemon peel? But I prefer carbonated water rather than ginger."
        },
        "outputs": {
            "answer": "English Highball, served in a Highball glass."
        },
    },
    {
        "inputs": {
            "question": "I like Kahlua in my cocktails. What do you have? But don't provide cocktails with the word Kahlua in the name."
        },
        "outputs": {
            "answer": "Espresso Martini"
        },
    },
    {
        "inputs": {
            "question": "We need some punch drinks for a party. What do you have? Especially with a weird name."
        },
        "outputs": {
            "answer": "Brain Fart"
        },
    },
    {
        "inputs": {
            "question": "Provide me some ordinary rum drink, something like Caipirinha."
        },
        "outputs": {
            "answer": "Caipirissima"
        },
    },
    {
        "inputs": {
            "question": "I don't drink alcohol, but I want something hot with milk, maybe chocolate."
        },
        "outputs": {
            "answer": "Drinking Chocolate"
        },
    },
    {
        "inputs": {
            "question": "Fruit boom. I like a non-alcoholic fruit cocktail. It should contain at least apple and strawberries, maybe bananas."
        },
        "outputs": {
            "answer": "Fruit Cooler"
        },
    },
    {
        "inputs": {
            "question": "I want a pizza cocktail."
        },
        "outputs": {
            "answer": "There is no available pizza cocktail in our menu."
        },
    },
    {
        "inputs": {
            "question": "Some weird question."
        },
        "outputs": {
            "answer": "Please provide a more relevant or understandable question."
        },
    },
    {
        "inputs": {
            "question": "Which one uses mint?"
        },
        "outputs": {
            "answer": "Acapulco or Derby"
        },
    },
    {
        "inputs": {
            "question": "Recently I was in hell, so today I want to drink something from Heaven-Paradise."
        },
        "outputs": {
            "answer": "Paradise"
        },
    },
    {
        "inputs": {
            "question": "Something for a lady in a pink dress."
        },
        "outputs": {
            "answer": "Pink Lady"
        },
    },
    {
        "inputs": {
            "question": "Do you have a moon cocktail?"
        },
        "outputs": {
            "answer": "Pink Moon"
        },
    },
    {
        "inputs": {
            "question": "Whatever cocktail with a straw."
        },
        "outputs": {
            "answer": "Flaming Lamborghini"
        },
    },
    {
        "inputs": {
            "question": "I want something served in a punch bowl with cola."
        },
        "outputs": {
            "answer": "Mudslinger"
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