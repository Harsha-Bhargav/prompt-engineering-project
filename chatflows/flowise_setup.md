# Setting up Flowise Locally

There are three main ways to set up Flowise on your local system:

1. **Using Docker and Docker Compose**
2. **Cloning the Git repository and running it locally**
3. **Installing Flowise via npm**

## 1. Using Docker and Docker Compose

Prerequisites:
- Make sure you have Docker and Docker Compose installed on your machine.

Installation Steps:
1. Clone the Flowise repository:
   ```bash
   git clone https://github.com/FlowiseAI/Flowise.git
   ```

2. Change into the `docker` directory:
   ```bash
   cd Flowise/docker
   ```

3. Create a `.env` file` to specify the environment variables:
   ```bash
   nano .env
   ```
   Add the following variables to the `.env` file:
   ```
   PORT=3000
   DATABASE_PATH=/root/.flowise
   APIKEY_PATH=/root/.flowise
   SECRETKEY_PATH=/root/.flowise
   LOG_PATH=/root/.flowise/logs
   BLOB_STORAGE_PATH=/root/.flowise/storage
   ```
   You can also specify `FLOWISE_USERNAME` and `FLOWISE_PASSWORD` for app-level authorization if needed.

4. Press `Ctrl + X` to exit the editor, and `Y` to save the file.

5. Start Flowise using Docker Compose:
   ```bash
   docker-compose up -d
   ```
   This command will start the Flowise containers in detached mode.

6. Access the Flowise application by opening your web browser and navigating to `http://localhost:3000`.

7. To stop the Flowise containers, run:
   ```bash
   docker-compose stop
   ```

## 2. Cloning the Git repository and running it locally

Prerequisites:
- Make sure you have Node.js and npm installed on your machine.

Installation Steps:
1. Clone the Flowise repository:
   ```bash
   git clone https://github.com/FlowiseAI/Flowise.git
   ```

2. Change into the Flowise directory:
   ```bash
   cd Flowise
   ```

3. Install the dependencies:
   ```bash
   npm install
   ```

4. Start the Flowise server:
   ```bash
   npm start
   ```

5. Access the Flowise application by opening your web browser and navigating to `http://localhost:3000`.

## 3. Installing Flowise via npm

Prerequisites:
- Make sure you have Node.js and npm installed on your machine.

Installation Steps:
1. Install Flowise globally using npm:
   ```bash
   npm install -g @flowiseai/flowise
   ```

2. Start the Flowise server:
   ```bash
   flowise start
   ```

3. Access the Flowise application by opening your web browser and navigating to `http://localhost:3000`.

Choose the method that best suits your needs and environment. For more detailed information on configuration and deployment options, please refer to the official Flowise documentation at https://docs.flowiseai.com/ .
<img width="1425" alt="image" src="https://github.com/Harsha-Bhargav/prompt-engineering-project/assets/123515723/9993a9b4-640a-4159-9b70-f804e532ce6d">


# Setting up Pinecone Vector Database for Knowbot Application

To enable document embedding and retrieval for your Knowbot application, you need to set up a Pinecone vector database. Here are the steps to get started:

### Create a Pinecone Account
1. Go to the Pinecone website (https://www.pinecone.io/) and create a free account.
2. After signing up, you will be redirected to the Pinecone dashboard.

### Create an Index
1. In the Pinecone dashboard, click on "Create Index".
2. Choose a name for your index, such as "knowbot-index".
3. Set the DIMENSIONS to 1536, which is the default output size of the text-embedding-ada-002 model used by Flowise.
4. Leave the other settings as default and click "Create Index".

### Obtain API Key and Environment
1. In the Pinecone dashboard, go to the "API Keys" section.
2. Copy your API key and environment. You will need these for configuring the Pinecone client.

### Configure Pinecone Client
1. In your Flowise application, install the Pinecone client library:
   ```bash
   npm install @pinecone-database/pinecone
   ```

2. Import the Pinecone client and configure it with your API key and environment:
   ```javascript
   const pinecone = new PineconeClient();

   await pinecone.init({
     environment: 'YOUR_PINECONE_ENVIRONMENT',
     apiKey: 'YOUR_PINECONE_API_KEY',
   });
   ```

### Upsert Embeddings to Pinecone Index
1. After generating the embeddings for your documents using Flowise, you can upsert them to the Pinecone index:
   ```javascript
   const index = pinecone.Index('knowbot-index');

   await index.upsert({
     upsertRequest: {
       vectors: [
         { id: 'doc1', values: doc1Embedding },
         { id: 'doc2', values: doc2Embedding },
         // Add more documents
       ],
     },
   });
   ```

2. The `upsert` operation will add the embeddings to the Pinecone index, allowing for efficient vector similarity search.

By following these steps, you will have set up a Pinecone vector database to store and retrieve document embeddings for your Knowbot application. The Pinecone index will enable fast and accurate retrieval of relevant documents based on user queries [4].
<img width="1438" alt="image" src="https://github.com/Harsha-Bhargav/prompt-engineering-project/assets/123515723/41076b2c-e3fd-449d-87bd-67a4f5c0b05e">

Citations:
[1] https://docs.flowiseai.com/getting-started
[2] https://github.com/FlowiseAI/Flowise
[3] https://docs.flowiseai.com
[4] https://www.youtube.com/watch?v=ZjooYLnS2mQ
