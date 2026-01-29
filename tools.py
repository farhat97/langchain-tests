from langchain.tools import tool, ToolRuntime
import requests
import json

# Example tool
@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    
    print('accessing get_weather tool')
    return f"It's always sunny in {city}!"

@tool
def get_all_wizards(runtime: ToolRuntime) -> str:
    """Get all available wizards"""
    
    print('[Tool] Accessing get_all_wizards')
    response = requests.get("https://wizard-world-api.herokuapp.com/Wizards")
    
    if response.status_code == 200:
        wizard_data = response.json()
        wizards_names = get_wizards_names(wizard_data)
        wizard_elixir_map = {}

        for wizard in wizard_data:
            full_name = f"{wizard.get('firstName', '')} {wizard.get('lastName', '')}".strip()

            if full_name:
                elixir_ids = [elixir['id'] for elixir in wizard.get('elixirs', [])]
                wizard_elixir_map[full_name] = elixir_ids

        return f"""Available wizards: {wizards_names} [WIZARD_ELIXIR_MAP: {json.dumps(wizard_elixir_map)}]"""

    return "Could not get available wizards"

@tool
def get_wizard_elixirs(wizard_name, wizard_elixirs_ids) -> str:
    """Get available elixirs for a particular wizard"""

    print("[Tool] Acessing get_wizard_elixirs tool for wizard = " + wizard_name)

    elixirs_info = [] 

    for elixir_id in wizard_elixirs_ids:
        elixirs_info.append(get_elixir_by_id(elixir_id))

    return elixirs_info

# utility functions
def get_wizards_names(wizards): 
    names = ""
    for wizard in wizards:
        if wizard["firstName"]:
            names += "- " + wizard["firstName"] + " " + wizard["lastName"] + "\n"
        else:
            names += "- " + wizard["lastName"]
    return names

def get_elixir_by_id(elixir_id: str) -> str:
    response = requests.get("https://wizard-world-api.herokuapp.com/Elixirs/" + elixir_id)

    if response.status_code == 200:
        return response.json()
    
    return "Could not get elixir"

