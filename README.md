# Chatbot Project: KnowBot

This project serves as a guide on how to create a chatbot from scratch usign little to no code. Developed as a part of the Prompt Engineering course (Info 7375) for Spring '24 at Northeastern University under the guidance of Prof. Nick Bear Brown.

## Project Overview

KnowBot is a chatbot designed to act as a teaching assistant (TA) for any course. It assists professors and students by providing guidance, answering questions, and delivering course-related information. KnowBot is built using Flowise, Pinecone Vector Database, and OpenAI technologies.

## Objectives

The primary objective of this project is to develop KnowBot, an intelligent TA bot, to support students in the course. KnowBot aims to enhance the learning experience by providing timely and accurate assistance with course materials and queries.

## Technology Stack

- **Flowise:** Utilized for building chatbot workflows and integrating language models, vector databases, chains.
- **Pinecone Vector Database:** Used for efficient storage and retrieval of knowledge in vecor format.
- **OpenAI models:** Employs AI models for natural language understanding and generation of embeddings.

## Theory and Quiz

For in-depth information about Flowise, Vector DB, and chatbots, refer to the theory and quiz section in the report.md file [here](reports/quiz.md).

## Setup Instructions

### Setting up Flowise and Pinecone Vector Database

Detailed instructions for setting up Flowise and Pinecone Vector Database can be found in **flowise_setup.md** file [here](chatflows/flowise_setup.md).

### Programming the Chatbot

To program KnowBot, follow these steps:
1. Upload PDFs of class-related documents to the bot in the Flowise UI on localhost port 3000 in the Chatflows section. As shown here:
<img width="1115" alt="image" src="https://github.com/Harsha-Bhargav/prompt-engineering-project/assets/123515723/e713f4ab-0207-41ad-b612-5171536a3f6b">



### Obtaining the Chatbot API

To get the chatbot API or bot UI:
1. Add a `.env` file with the API_URL, replacing it with the URL obtained from Flowise.
<img width="1069" alt="image" src="https://github.com/Harsha-Bhargav/prompt-engineering-project/assets/123515723/93860666-8d69-446f-8607-358d6f8f8285">


### Testing Process

To test KnowBot:
1. Upload a document and check the answers on this document.
2. Ensure error handling is functional.
Detailed testing instructions can be found in the report file [here](https://github.com/Harsha-Bhargav/prompt-engineering-project/blob/main/reports/Report.md).


# Publishing the Chatbot

The chatbot can be published using various methods to make it accessible to students. Here are the three options available:

1. Flowise Chatbot UI: The chatbot can be published using the Flowise Chatbot UI. This method provides an intuitive interface for deploying and managing the chatbot. It allows for easy customization of the chatbot's behavior and integration with other components of the application.

2. Streamlit App: Another option is to publish the chatbot as a Streamlit app. Streamlit provides a user-friendly interface for interacting with the chatbot. This method is ideal for creating a standalone application that can be accessed by students without any additional setup.

3. Flask App: The chatbot can also be published using a Flask app located in the frontend folder. This method offers flexibility and customization options. By using Flask, you can integrate the chatbot with other features of your application and tailor it to your specific requirements.

Students can choose any of these methods to access and interact with the chatbot. Each option has its own advantages and can be selected based on the project's needs and the desired user experience.
