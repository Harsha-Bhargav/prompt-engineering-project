import streamlit as st
import requests
import os
from dotenv import load_dotenv

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

def main():
    st.title("Chatbot App")

    st.write("Welcome to the Chatbot App!")
    st.write("Enter your message below:")

    # Initialize chat history as an empty list
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", "")

    if st.button("Send"):
        if user_input:
            bot_response = chatbot(user_input)
            st.session_state.chat_history.append({"You": user_input, "Bot": bot_response["answer"] if "answer" in bot_response else "Sorry, I couldn't understand that."})

        else:
            st.write("Please enter a message.")

    # Display chat history
    st.write("Chat History:")
    for chat in st.session_state.chat_history:
        st.write("You:", chat["You"])
        st.write("Bot:", chat["Bot"])

if __name__ == "__main__":
    main()
