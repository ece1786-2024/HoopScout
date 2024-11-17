# Data Extration Agent
from openai import OpenAI
import json
import os
client = OpenAI(api_key="API_KEY")

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
            with open(os.path.join(database_path, file), 'r') as f:
                player_data.append(json.load(f))
    return player_data

def DE_agent_response(statement):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": statement}
        ]
    )

    reply = response.choices[0].message.content.strip()
    return reply

if __name__ == "__main__":
    print("Unit test here")