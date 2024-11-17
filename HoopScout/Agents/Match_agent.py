# Data Extration Agent
from openai import OpenAI
import json
import os
client = OpenAI(api_key="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")

prompt = """
You are a professional basketball analyst tasked with finding players from a knowledge base who are most similar to a new NBA draft prospect based on their stats and background information.
Following tasks are required:
1. Compare the new player’s information to each player in the knowledge base.
3. Identify the most similar player(s) by considering:
    - Statistical similarity (e.g., PPG, RPG, APG, shooting percentages, etc).
    - Background similarity (e.g., college, position, achievements, physical attributes).
4. Provide a list of the most similar players.
5. If no strong similarity exists, state: "No sufficiently similar players found in the knowledge base."
"""

def load_player_data(database_path):
    player_data = []
    for file in os.listdir(database_path):
        if file.endswith(".json"):
            with open(os.path.join(database_path, file), 'r', encoding='utf-8') as f:
                player_data.append(json.load(f))
    return player_data

def Match_agent_response(player_info, player_KB):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Given player's information{json.dumps(player_info)}" +
             f"From the existing knowledge base, {player_KB}" +
             "Please find the most similar players from the knowledge base to the given player if any."},
        ]
    )

    reply = response.choices[0].message.content.strip()
    return reply

if __name__ == "__main__":
    with open('Input/Test.json', 'r', encoding='utf-8') as file:
        player_info = json.load(file)
        
    player_KB = load_player_data('data/test')

    result = Match_agent_response(player_info, player_KB)
    print(result)