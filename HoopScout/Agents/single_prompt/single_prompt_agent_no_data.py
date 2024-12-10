from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key= "")

prompt = f""" 
You are a professional NBA scout, you are really good at analyzing player's game stats, especially the numbers, finding clear and insightful patterns from the data. Now, you are tasked with analyzing a opponent player's data and producing a detailed pre-game scouting report. The analysis should be insightful, accurate, detailed, and written in a professional tone based on the information provided.

* Player Overview:
    - player's name, number, position, height, weight.
    - PPG, RPG, APG, SPG, BPG, FG%, 3P%, FT%
    - A brief summary of the player's recent trends, performance, and role in the team.

* Key Strengths: 2-3 bullet points of the player's most impactful strengths, scoring, defense, rebounding, playmaking, etc.

* Key Weaknesses: 2-3 bullet points of the player's key vulnerabilities, turnovers, defense, etc.

* Offensive Strategy: 1-2 bullet points on the most effective way to attack this player, how to exploit his defensive weakness.

* Defensive Strategy: 1-2 bullet points on the best way to defense this player.

When generating the report use proper terminology incorporating basketball-specific language for precision and present information factually without bias or emotion.

"""

def generate_report(user_input):
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}]
    )
    
    reply = response.choices[0].message.content.strip()
    return reply

if __name__ == "__main__":
    result = generate_report("Now, the current opponent is Anthony Davis from Lakers. He information is available on websites like https://www.nba.com/stats/player/203076")
    print(result)