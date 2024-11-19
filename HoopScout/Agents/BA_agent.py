from openai import OpenAI
import json

client = OpenAI(api_key="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")

prompt = """ You are an expert basketball analyst tasked with generating a professional pre-game scouting report for an NBA player. Based on the player's last 15 games' stats and performance data, provide a clear, concise, and actionable report divided into the following sections:

Overview:

Summarize the player's recent performance trends, role in their team, and overall impact on games. Highlight any noticeable patterns, such as scoring averages, shooting efficiency, or playmaking contributions.
Strengths:

Identify the player's key strengths and skills (e.g., shooting, defense, passing, rebounding). Use specific examples or metrics from the data to support your analysis.
Weaknesses:

Highlight areas where the player struggles or is less effective. Provide details backed by stats, such as inefficiency in certain play types or defensive vulnerabilities.
Offensive Strategy:

Provide specific recommendations for defending this player when they are on offense. Include insights into how to limit their scoring, disrupt their rhythm, or force them into less efficient situations.
Defensive Strategy:

Analyze how to exploit the player’s defensive tendencies. Suggest offensive plays or matchups that could take advantage of their weaknesses.
"""

def SR_agent_response(player_info):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": "Given the player's last 15 games stats, please generate a pre-game scouting report. Here is his stats: " + player_info}
        ]
    )

    reply = response.choices[0].message.content.strip()
    return reply

if __name__ == "__main__":
    import pandas as pd
    giannis_stats = pd.read_csv("Giannis_stats.csv")
    player_info = ""
    for index, row in giannis_stats.iterrows():
        player_info += (
        f"Matchup: {row['Match Up']}, Result: {row['W/L']}, Minutes Played: {row['MIN']}, "
        f"Points: {row['PTS']}, Field Goals: {row['FGM']}/{row['FGA']} ({row['FG%']}%), "
        f"Three-Pointers: {row['3PM']}/{row['3PA']} ({row['3P%']}%), Free Throws: {row['FT%']}%, "
        f"Rebounds: {row['REB']} (Off: {row['OREB']}, Def: {row['DREB']}), Assists: {row['AST']}, "
        f"Steals: {row['STL']}, Blocks: {row['BLK']}, Turnovers: {row['TOV']}, "
        f"Personal Fouls: {row['PF']}, Plus/Minus: {row['+/-']}.\n"
    )
   
    result = SR_agent_response(player_info)
    print(result)