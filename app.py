import streamlit as st
import requests
from dotenv import load_dotenv
import os


API_URL = "http://localhost:3000/api/v1/prediction/923ed8db-acac-4aa4-8bea-69202cb14e74"
body_data = {
    "returnSourceDocuments": True
}

def upload_file_to_api(file):
    form_data = {"file": (file.name, file)}
    response = requests.post(API_URL, files=form_data)
    if response.status_code == 200:
        st.success(f"File '{file.name}' uploaded successfully!")
    else:
        st.error(f"Failed to upload file '{file.name}'. Status code: {response.status_code}")



def send_message_to_api(message):
    # Send the user's message to the API and get a response
    payload = {"question": message}
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return "Failed to get response from the API"

def main():
    st.title("AI Document Assistant")

    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=['csv'], accept_multiple_files=False, help="Max file size: 50MB")
    if st.sidebar.button("Upload"):
        upload_file_to_api(uploaded_file)

    # Display chat interface
    st.subheader("Chat Interface")
    st.write("Use the text area below to ask questions:")
    user_input = st.text_area("User Input")
    if st.button("Send"):
        if user_input.strip() != "":
            response = send_message_to_api(user_input)
            st.write("User: ", user_input)
            st.write("Assistant: ", response['text'])

if __name__ == "__main__":
    main()
