# Agent Development KIT (ADK) Course
## Getting Started
### Setup Environment

You only need to create one virtual environment for all examples in this Demo.  
Follow below steps to set it up:

```bash
# Create a virtual environment in the root directory
python -m venv myenv

# Activate (each new terminal)

# macOS / Linux
source myenv/bin/activate

# Windows CMD
myenv\Scripts\activate

# Windows PowerShell
myenv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### Create an agent project

Run the adk create command to start a new agent project.
```bash

adk create my_agent
```
Explore the agent project
The created agent project has the following structure, with the agent.py file containing the main control code for the agent.

```bash
my_agent/
    agent.py      # main agent code
    .env          # API keys or project IDs
    __init__.py

```
**YOu can also create the above folder structure manually or using CMD. As ADK follows the above folder structure.**

### Setting up API Keys

Most projects in this repo uses the Gemini API, which requires an API key. If you don't already have Gemini API key, create a key in Google AI Studio on the API Keys page.

1. Create an account in Google Cloud https://cloud.google.com/?hl=en
2. Create a new Project
3. Go to https://aistudio.google.com/apikey
4. Create an API key
5. Assign key to the project
6. Connect to a billing account



In a terminal window, write your API key into an .env file as an environment variable:
```bash
echo 'GOOGLE_API_KEY="YOUR_API_KEY"' > .env
```

OR you can manually update the GOOGLE_API_KEY with your API Key in the .env file


## Setting up API Keys for Non-Gemini Models

ADK also supports non-Google models such as OpenAI, Anthropic, Azure OpenAI, and others. These models are integrated using **wrapper classes**, which allow compatibility with different APIs, gateways, and client configurations.

### Wrapper Classes

Wrapper classes are required when using models outside the Gemini ecosystem or when special routing/configuration is needed (for example, Apigee or LiteLLM).

Instead of passing a model name string directly, you instantiate a wrapper class and pass it as the `model` parameter to your `LlmAgent`.

Common wrappers include:
- `LiteLlm` – OpenAI, Anthropic, Azure OpenAI, Cohere, Mistral, etc.
- `ApigeeLlm` – Models accessed through Apigee gateways

---

### OpenAI / Anthropic (LiteLLM)

#### Environment Variables

```bash
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
ANTHROPIC_API_KEY="YOUR_ANTHROPIC_API_KEY"
```


### Run your agent
You can run your ADK agent with an interactive command-line interface using the adk run command or the ADK web user interface provided by the ADK using the adk web command. Both these options allow you to test and interact with your agent.

**Run with command-line interface**
Run your agent using the adk run command-line tool.
```bash
adk run my_agent
```

**Run with web interface**
The ADK framework provides web interface you can use to test and interact with your agent. You can start the web interface using the following command:
```bash
adk web --port 8000
```