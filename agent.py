from langchain.agents import create_agent
from tools import *
from langchain.messages import AIMessage, ToolMessage

# API key stuff
import getpass
import os

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")


SYSTEM_PROMPT = """
You are a helpful assistant. You have access to the following tools:

- get_weather: use this to get the weather
- get_all_wizards: use this to get the list of all wizards
- get_wizard_potions: use this to get the types of potions that a wizard can use. This requires the user to enter a wizard's name - if no name is provided, request the user to enter a name
"""

agent = create_agent(
    model="gpt-5-nano",
    tools=[get_weather, get_all_wizards, get_wizard_potions],
    system_prompt=SYSTEM_PROMPT
)


def print_response(result_messages): 
    for msg in result_messages:
        if isinstance(msg, AIMessage):
            print("AI: " + msg.content)
        if isinstance(msg, ToolMessage):
            print("Tool: " + msg.content)


# Run the agent via user prompts

while True:
    print("What would you like me to check?\n")

    request = input()
    result = agent.invoke({"messages": [{"role": "user", "content": request}]})
    
    print_response(result["messages"])

