# Scouting Report Agent
from openai import OpenAI
import json

client = OpenAI(api_key="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")

prompt = """
You are a NBA scout. I want you to generate a scouting report based on a player and he's information.
You will be given a player and one or more existing players from a dataset with similar information.
Use the player's information with the help of existing players to create an authentic scouting report.
The scouting report should contain a rating section with Athleticism, Defense, Size, Shooting.
It should also contain sections for strength and weakness, which you have to write by analyzing 
information from the player and information from existing similar players.
"""

def SR_agent_response(player_info, existing_players):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": "Here is the player's information I want you to generate a scouting report: " + json.dumps(player_info, indent=2) + "\n"
            + "Here are the similar players information from a dataset: " + json.dumps(existing_players, indent=2)}
        ]
    )

    reply = response.choices[0].message.content.strip()
    return reply

if __name__ == "__main__":
    # unit test
    with open('data/Test.json', 'r') as file:
        player_info = json.load(file)

    with open('data/Reed_Sheppard.json', 'r') as file:
        existing_players = json.load(file)

    result = SR_agent_response(player_info, existing_players)

    print(result)