# Scouting Report Agent
from openai import OpenAI
import json

client = OpenAI(api_key="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")

prompt = """ 
You are a professional NBA scout tasked with generating detailed and authentic scouting reports for NBA draft prospects. You are really good at using concise, professional language suitable for an NBA front office
and writing a scouting reports that are both informative and actionable. You have been provided with both player's stats and his background information, as well as a list of similar players from the knowledge base.
Use these information to generate a scouting report for the player. 

The structure of the scouting report should be as follows:
1. Strengths: A player’s primary strengths. Highlight skills that make the player an asset.
2. Weaknesses: Discuss areas where the player needs improvement, and their potential limitations.
3. Outlook: Offers a projection of the player’s growth and future role in the NBA.
4. Player Comparison: Compare the player to a current or past NBA player with a similar playstyle.
5. Mock Draft: Estimate the player's draft position.
5. Rating: Give rating of the player's different aspects, including "Athleticism", "Size", "Offense, "Defense", "Strength", "Quickness", "Shooting", "Passing", "Ball Handling", "Potential", each on a scale of 1-10.

When generating each section of the scouting report, the following instructions should be followed:
1. Use player's stats to back up claim and analysis about their strengths and weaknesses.
2. Be objective and constructive in identifying areas for improvement.
3. Focus on limitations in skill, physical attributes, or consistency, but avoid overly negative language.
4. Emphasize how their high-school and college performance reflects their growth and potential.
5. When a strong similarity exists between the player we want to generated and an existing player in our knowledge base, use existing report's tone, relevant attributes, contents, and analysis as inspiration while
staying objective and ensuring all content is derived from the new player's actual data.
6.Maintain a professional tone, avoid casual or speculative language.

Few shots prompting:
example 1:
example 2:
........
........
"""

def SR_agent_response(player_info, existing_players):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": "Given the player's information, please generate a professional, authentic, and accurate souting report for NBA draft prospects: " + json.dumps(player_info, indent=2)}
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