# Tool Agent Example

## What is Tool Agent?

A tool agent is an AI agent where the language model is not restricted to only replying with text. While it is processing your request, it is allowed to stop, call an external function or API, get the real result, and then continue its response using that result. The key point is that the decision to call the tool is made by the model itself, not hard-coded by the developer. This is what turns the model from a “talking system” into a system that can actually do things—fetch live data, run code, query databases, or trigger actions—and then respond based on what actually happened, not what it guessed.


## Core Components

### 1. LLM (Reasoning Engine)
The LLM interprets user input, performs reasoning, and decides whether a tool is required. It determines *when* to act and *which* tool to use but does not execute tools itself.

### 2. Agent
The `Agent` binds the model, instructions, and tools together. An agent becomes a **tool agent** once tools are attached and the model is allowed to invoke them during execution.

### 3. Tools
Tools are external executable units, typically Python functions or API wrappers. They perform deterministic operations such as:
* data fetching
* computation
* database queries
* service calls. 
Tools always run outside the LLM.

### 4. Tool-Calling Interface
This interface allows the LLM to request a tool invocation in a structured format. It ensures:
* correct tool selection
* input validation
* safe execution.

### 5. Execution Runtime
The runtime executes the requested tool, captures its output, and feeds the result back into the LLM so it can complete the final response using real execution results.

## Types of Tools in Google ADK

In Google ADK, tools define the actions an agent can perform. They are categorized based on how they are provided and executed.

### Built-in Tools
Built-in tools are tools provided directly by the ADK runtime. They handle common system-level or platform-level capabilities and require no custom implementation by the developer. These tools are tightly integrated with the ADK execution loop and are typically used for standard operations such as platform utilities or predefined capabilities exposed by the framework.

### Custom Tools
Custom tools are developer-defined tools, usually implemented as Python functions or API wrappers. They encapsulate application-specific logic such as calling external services, querying databases, running business rules, or triggering workflows. Custom tools run outside the LLM and return deterministic results back to the agent.

### External Service Tools
External service tools are a subset of custom tools that act as adapters to third-party systems. These tools handle authentication, request formatting, and response parsing for services such as REST APIs, cloud services, or internal enterprise systems.

### Summary
Google ADK tool agents can use built-in tools for common framework capabilities and custom or external tools for domain-specific actions. Together, these tool types allow agents to combine LLM reasoning with real-world execution.
