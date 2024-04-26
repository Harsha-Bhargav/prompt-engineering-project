# Setting up Flowise Locally

There are three main ways to set up Flowise on your local system:

1. **Using Docker and Docker Compose**
2. **Cloning the Git repository and running it locally**
3. **Installing Flowise via npm**

### 1. Using Docker and Docker Compose

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

### 2. Cloning the Git repository and running it locally

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

### 3. Installing Flowise via npm

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
