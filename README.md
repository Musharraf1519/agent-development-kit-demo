# Agent Development KIT (ADK) Course

## Getting Started

### Setup Environment

You only need to create one virtual environment for all examples in this course.  
Follow below steps to set it up:

```bash
# Create a virtual environment in the root directory
python -m venv myenv

# Activate (each new terminal)

# macOS / Linux
source myenv/bin/activate

# Windows CMD
myenv\Scripts\activate.bat

# Windows PowerShell
myenv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### Setting up API Keys

1. Create an account in Google Cloud https://cloud.google.com/?hl=en
2. Create a new Project
3. Go to https://aistudio.google.com/apikey
4. Create an API key
5. Assign key to the project
6. Connect to a billing account


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