
# Part 1: Theoretical Foundations for Flowise Chatbot

### Chatbots and AI
Chatbots have emerged as transformative tools in educational technology, reshaping the dynamics of interaction between learners and educational content. Rooted in the evolution of artificial intelligence (AI), chatbots have witnessed significant advancements, particularly in natural language processing (NLP). These advancements have empowered chatbots to deliver personalized learning experiences, engage students in interactive discussions, and provide instant assistance with educational queries.

### Natural Language Processing (NLP)
NLP serves as the backbone of chatbot functionality, enabling them to comprehend and respond to human language effectively. Through techniques like speech recognition, language understanding, and language generation, NLP equips chatbots with the ability to interpret user input, extract meaning, and generate appropriate responses. Recent strides in deep learning and transformer models have further bolstered the capabilities of NLP, enhancing chatbot performance and natural language understanding.

### Choosing Your Platform: Flowise
For the development of our educational chatbot, we have selected Flowise as the platform of choice. Flowise stands out as an open-source, low-code tool designed specifically for building customized LLM orchestration flows and AI agents. With its intuitive interface, Flowise simplifies the process of designing chatbot workflows, integrating various language models, and deploying conversational agents.

#### Flowise Documentation:
- GitHub Repository: [Flowise GitHub Repository](https://github.com/FlowiseAI/Flowise)
- Official Documentation: [Flowise Official Documentation](https://docs.flowiseai.com/)
- Getting Started Guide: [Flowise Getting Started Guide](https://docs.flowiseai.com/getting-started)

### Building a RAG-based Knowledge Application with Flowise and Pinecone Vector Database
To implement our educational chatbot, we are leveraging Flowise along with the Pinecone Vector Database. The RAG (Retriever-Reader-Generator) model serves as the foundation for our knowledge application, allowing the chatbot to retrieve and generate responses based on user queries [6].

#### Process Overview:
1. **Setting up Flowise**: Begin by installing the necessary dependencies and starting the Flowise server as per the instructions provided in the [flowise setup.md](chatflows/flowise_setup.md).

2. **Designing the Chatbot Workflow**: Utilize Flowise's visual interface to design the chatbot workflow, incorporating the RAG model and other relevant components.

3. **Integrating Pinecone Vector Database**: Establish a connection between Flowise and the Pinecone vector database to store and retrieve knowledge efficiently. Pinecone's vector similarity search capabilities enhance the chatbot's ability to provide relevant responses based on user queries.

4. **Testing and Deployment**: Conduct thorough testing of the chatbot to verify its functionality and accuracy. Once validated, deploy the chatbot to the desired platform or environment for user interaction.

By leveraging Flowise and integrating it with the Pinecone Vector Database, we can develop a robust educational chatbot powered by the RAG model. This chatbot promises to deliver accurate and relevant information to users through natural language interactions.

## Quiz Questions

If you want to test your understanding of the flowise chatbot here are some practise [quiz questions:](quiz.md)

# Part 2: Building Your Educational Bot

### Purpose and Functionality
- **Educational Bot Name:** KnowBot
- **Purpose:** KnowBot serves as a teaching assistant bot for a course, aiming to assist students with their questions regarding course materials such as class presentations, syllabus, project outlines, assignments, and rubrics.
- **Functionality:**
  - **Document Upload:** KnowBot accepts documents in PDF format uploaded from the Flowise backend.
  - **Information Extraction:** It extracts relevant information from uploaded documents, such as key topics, assignment details, and project requirements.
  - **Question Answering:** KnowBot provides assistance to students by answering questions based on the content of the uploaded documents, offering explanations, summaries, and additional resources as needed.

### Creating KnowBot
#### 1. Quick Setup
- **Install Flowise:**
  - Developers can install Flowise using Node.js package manager (npm) with the following command:
    ```
    npm install -g flowise
    ```
- **Start Flowise:**
  - After installation, developers can start Flowise locally with the following command:
    ```
    npx flowise start
    ```
    
- **Setup Pinecone DB:**
  - To enable document embedding and retrieval, developers need to create an account in Pinecone DB, a vector database.
- **Upload Chatflow:**
  - The provided chatflow, containing the conversational logic and integration with Pinecone DB, is uploaded to the Flowise instance.
  - Documents in PDF format are uploaded to the chatflow, which extracts text and generates vector embeddings for storage in Pinecone DB.
- **Get API Link:**
  - Once the chatflow is set up and documents are uploaded, developers can obtain the API link for KnowBot from the share option in Flowise.
  - This API link can be used directly to interact with KnowBot or integrated into a streamlit/flask app for a more user-friendly interface.

    Detailed setup instructions [here:](chatflows/flowise_setup.md)

### Conversational Flow Design
- **Architecture:** KnowBot leverages the RAG (Retrieval Augmented Generation) architecture, which combines retrieval of relevant information from a knowledge base with language generation to produce informative responses.
- **Prompt Engineering:** To simulate the role of a teaching assistant, KnowBot is programmed with prompts that guide users in asking questions related to course materials.
- **Examples of Prompts:**
  - "KnowBot, can you provide an overview of today's class presentation?"
  - "KnowBot, what are the key topics covered in the syllabus?"
  - "KnowBot, could you explain the requirements for the upcoming project?"
- **Engaging Users:**
  - **Teachers:** KnowBot serves as a valuable resource for teachers, allowing them to quickly access information and resources to supplement their teaching materials.
  - **Students:** Students can interact with KnowBot to ask questions about course materials, assignments, and projects, receiving timely and accurate assistance to enhance their learning experience.

---

# Part 3: Testing, Quality Assurance

### Task 1: Testing Your Bot

#### Testing Process
- **Objective:** To evaluate the performance of KnowBot and ensure its functionality meets the intended requirements.
- **Test Cases:**
  1. **Document Upload Test:**
     - **Test Case:** Upload a class presentation PDF.
     - **Expected Result:** KnowBot extracts key topics and themes from the presentation.
     - **Actual Result:** Key topics are successfully extracted and presented to the user.
  2. **Question-Answering Test:**
     - **Test Case:** Ask KnowBot about the deadline for an upcoming assignment.
     - **Expected Result:** KnowBot accurately identifies the assignment deadline and provides relevant details.
     - **Actual Result:** KnowBot retrieves the correct deadline information from the uploaded documents.
  3. **Error Handling Test:**
     - **Test Case:** Input a vague query with ambiguous terms.
     - **Expected Result:** KnowBot responds with a helpful error message, guiding the user to provide clearer input.
     - **Actual Result:** KnowBot recognizes the ambiguity and prompts the user to rephrase the query.

#### Issues Encountered
- **Issue:** Inconsistent document extraction results.
  - **Resolution:** Implemented improvements in document parsing algorithms to enhance extraction accuracy.
- **Issue:** Occasional delays in response time.
  - **Resolution:** Optimized backend processes and server configurations to improve response speed.
- **Issue:** Misunderstanding of certain complex queries.
  - **Resolution:** Expanded training data and refined natural language processing models to better handle diverse query types.

### Task 2: Quality and Documentation

#### Quality Assessment
- **User Experience:** Users find KnowBot's interface intuitive and easy to use, with prompt and accurate responses enhancing their learning experience.
- **Accuracy:** KnowBot demonstrates high accuracy in extracting information from uploaded documents and providing relevant answers to user questions, minimizing errors and misinformation.
- **Error Handling:** KnowBot effectively handles errors by providing informative error messages and guiding users to rephrase ambiguous queries, ensuring smooth interaction even in challenging scenarios.

---

These examples provide specific instances of test cases and issues encountered during testing, along with resolutions, and assess the quality of KnowBot in terms of user experience, accuracy, and error handling.
