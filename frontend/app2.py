import streamlit as st
import requests
from dotenv import load_dotenv
import os


API_URL = "http://localhost:3000/api/v1/prediction/f5937548-0b97-4c97-b980-9ad704276155"
body_data = {
    "returnSourceDocuments": True
}

# def upload_file_to_api(file):
#     form_data = {"file": (file.name, file)}
#     #form_data = {"files": ('Sample Final.pdf', open('Sample Final.pdf', 'rb'))}
#     response = requests.post(API_URL, files=form_data)
#     if response.status_code == 200:
#         st.success(f"File '{file.name}' uploaded successfully!")
#     else:
#         st.error(f"Failed to upload file '{file.name}'. Status code: {response.status_code}")


def send_message_to_api(message):
    # Send the user's message to the API and get a response
    payload = {"question": message}
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return "Failed to get response from the API"

def display_chat_history(container):
    """Dynamically displays the chat history within the specified container."""
    if 'chat_history' not in st.session_state:
        st.session_state.setdefault("chat_history", [])
    with container:
        for message in st.session_state.chat_history:
            role = message["role"]
            content = message["content"]
            # Use the global counter to generate a unique key for each widget
            key = f"chat_{st.session_state.widget_counter}"
            st.text_area(label=role.capitalize(), value=content, height=100, disabled=True, key=key)
            # Increment the global counter after each widget creation
            st.session_state.widget_counter += 1

def main():
    st.title("AI Document Assistant")

    uploaded_file = st.sidebar.file_uploader("Upload PDF", type=['pdf'], accept_multiple_files=False, help="Max file size: 50MB")
    if st.sidebar.button("Upload File"):
        if uploaded_file is not None:
            files = {'file': uploaded_file}
            response = requests.post(API_URL, files=files,data=body_data )
            if response.status_code == 200:
                st.success(f"File '{uploaded_file.name}' uploaded successfully!")
            else:
                st.error(f"Failed to upload file '{uploaded_file.name}'. Status code: {response.status_code}")

    st.subheader("Chat Interface")
    st.write("Use the text area below to ask questions:")
    user_input = st.text_area("User Input")
    if st.button("Send"):
        if user_input.strip() != "":
            response = send_message_to_api(user_input)
            st.write("User: ", user_input)
            st.write("Assistant: ", response)


if __name__ == "__main__":
    main()
