from langchain.agents import create_agent
from tools import get_weather, get_all_wizards, get_wizard_elixirs
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
- get_wizard_elixirs: use this to get the types of elixirs that a wizard can use. Use the wizard ID from get_all_wizards results. The result for this query should include the name of the Elixir and the description for it, separated by a colon ":"

When you call get_all_wizards, remember the wizard information for subsequent get_wizard_elixirs calls.
"""

agent = create_agent(
    model="gpt-5-nano",
    tools=[get_weather, get_all_wizards, get_wizard_elixirs],
    system_prompt=SYSTEM_PROMPT,
    # state_schema=WizardState
)

while True:
    print("What would you like me to check?\n")

    request = input()
    result = agent.invoke({"messages": [{"role": "user", "content": request}]})
    
    # print_response(result["messages"])
    print(result["messages"][-1].content)

