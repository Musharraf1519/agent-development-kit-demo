from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.0-flash',
    name='greeting_agent',
    description='Greeting Agent',
    instruction="""You are a friendly greeting agent.
                Ask the user their name and greet them by their name.""",
)
