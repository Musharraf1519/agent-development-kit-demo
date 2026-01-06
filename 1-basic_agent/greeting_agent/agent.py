from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    model=LiteLlm(model="openai/gpt-4o"), # Using OpenAPI's GPT-4o as Gemini is exhausted.
    # model='gemini-1.5-flash',
    name='greeting_agent',
    description='Greeting Agent',
    instruction="""You are a friendly greeting agent.
                Ask the user their name and greet them by their name.""",
)
