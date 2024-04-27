from flask import Flask, render_template, request, session
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Set the secret key to enable session usage
app.secret_key = os.urandom(24)

# Load environment variables from .env file
load_dotenv()

def chatbot(message):
    API_URL = os.getenv("API_URL")  # Fetch API URL from environment variables
    payload = {"question": message}
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to get response from the chatbot API."}

@app.route("/", methods=["GET", "POST"])
def index():
    chat_history = []
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_input = request.form["user_input"]
        if user_input:
            bot_response = chatbot(user_input)
            # Add the new message at the end of the chat history
            session["chat_history"].append({"User": user_input, "Knowbot": bot_response["text"] if "text" in bot_response else "Sorry, I couldn't understand that."})
        else:
            return render_template("index.html", error="Please enter a message.")

    # Reverse the chat history to display the most recent messages at the bottom
    chat_history = session["chat_history"][::-1]
    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
