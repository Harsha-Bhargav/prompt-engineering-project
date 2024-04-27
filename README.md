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


## Theory and Quiz

For in-depth information about Flowise, Vector DB, and chatbots, refer to the theory and quiz section in the report.md file [here](reports/quiz.md).

---

This README provides a comprehensive overview of the project, including its objectives, technology stack, setup instructions, testing process, and resources for further exploration. Feel free to expand or modify any section as needed.
