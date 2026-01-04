from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


questions = [
    "hi", "hello",
    "what is ai",
    "what is machine learning",
    "what is python",
    "bye"
]

answers = [
    "Hello! How can I help you?",
    "Hello! How can I help you?",
    "AI means Artificial Intelligence.",
    "Machine Learning is a subset of AI.",
    "Python is a programming language.",
    "Goodbye! Have a nice day."
]


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(questions)


model = MultinomialNB()


model.fit(X, answers)

print(" ML Chatbot is LIVE (type 'bye' to exit)\n")

while True:
    user = input("You: ").lower().strip()

   
    X_test = vectorizer.transform([user])


    response = model.predict(X_test)[0]
    print("Bot:", response)

    if user == "bye":
        break
