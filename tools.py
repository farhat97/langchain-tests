from langchain.tools import tool
import requests

# Example tool
@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    
    print('accessing get_weather tool')
    return f"It's always sunny in {city}!"

@tool
def get_all_wizards() -> str:
    """Get all available wizards"""
    
    print('accessing get_all_wizards tool')
    response = requests.get("https://wizard-world-api.herokuapp.com/Wizards")
    
    if response.status_code == 200:
        wizards_names = get_wizards_names(response.json())
        # return response.json()
        return "The available wizards are: \n" + wizards_names

    return "Could not get available wizards"

@tool
def get_wizard_potions(wizard_name):
    """Get available potions for a particular wizard"""

    print("acessing get_wizard_potions tool")
    # TODO: pending
    response = requests.get("")


# utility functions
def get_wizards_names(wizards): 
    names = ""
    for wizard in wizards:
        if wizard["firstName"]:
            names += "- " + wizard["firstName"] + " " + wizard["lastName"]
        else:
            names += "- " + wizard["lastName"]
    return names

