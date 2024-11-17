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
6. Focus on available strengths, and add disclaimers for incomplete sections if information is not avaliable.
7. Maintain a professional tone, avoid casual or speculative language.


Below is an example of the player's information and his scouting report:
-- Given player's information
"Profile": {
        "Name": "Brandon Miller",
        "Height": "6'9\"",
        "Weight": "200 lbs",
        "Wingspan": "7'0\"",
        "Position": "Small Forward",
        "Birthdate": "November 22, 2002",
        "Nationality": "American"
    },
    "Statistics": {
        "Points Per Game (PPG)": 18.8,
        "Field Goal Percentage (FG%)": 43.0,
        "Three-Point Percentage (3P%)": 38.4,
        "Free Throw Percentage (FT%)": 85.9,
        "Assists Per Game (APG)": 2.1,
        "Turnovers Per Game (TOV)": 2.0,
        "Rebounds Per Game (RPG)": 8.2,
        "Offensive Rebounds Per Game (ORB)": 1.0,
        "Defensive Rebounds Per Game (DRB)": 7.2,
        "Steals Per Game (SPG)": 0.9,
        "Blocks Per Game (BPG)": 0.9,
        "Effective Field Goal Percentage (eFG%)": 53.3,
        "Player Efficiency Rating (PER)": 23.4
    },
    "Background": {
        "College": "Following high school, Miller committed to the University of Alabama, where he played for the Crimson Tide during the 2022–2023 season. In his freshman year, he averaged 18.8 points, 8.2 rebounds,
        and 2.1 assists per game, shooting 38.4 from three-point range. His outstanding performance led Alabama to secure the No. 1 overall seed in the 2023 NCAA Tournament. Miller received several accolades,
        including SEC Player of the Year, SEC Rookie of the Year, and First-team All-SEC honors",
        "High School": "Miller attended Cane Ridge High School in Antioch, Tennessee, where he distinguished himself as a standout basketball player. His exceptional performance earned him the title of
        Tennessee Mr. Basketball in 2022.",
        "Work Ethic": "Known for his dedication and consistent improvement throughout his college career.",
        "Mentality": "Competitive and unselfish, willing to make the right play and take big shots in crucial moments."
    }

-- Player's scouting report
**Strength**:
    "An extremely talented 6’9 SF/PF with a lanky frame and very good length and athleticism … Has an intriguing scoring arsenal (leads all Fr with 18.8 ppg while shooting 45 from the field)
… Can shoot over many wings due to his size and can also operate in the mid-range and occasionally in the post as well … A sniper from distance (44 3FG on 7 attempts per game)
with a quick release and range well past the NBA 3-point line whether spotting up, through screens or pulling up off the dribble … His size on the perimeter makes him effective at sticking contested shots
… Has times when he can really get hot and take over games; as of now Miller has made 5 or more 3s in a game 5 times this season … Handles the ball adequately and is a threat creating offense for himself;
needs little space to get his shots off … Makes good use of combo dribbles to free himself in the mid-range … Excellent transition player; runs the floor well and is an above the rim finisher in the open court
… Versatility allows him to play as a SF or a ‘smallball’ PF … Good rebounding skills (8.2 rpg) and is much more physical than his slender frame would suggest … Competes on the defensive end and is able
to guard effectively on the perimeter and along the frontcourt as well … Length and awareness allows him to be a pest shooting into passing lanes at times (1.1 spg), and he offers some resistance as a help 
side defender by swatting shots occasionally (nearly 1 bpg) … Unselfish player who’s willing to give the ball to open teammates … Makes hustle plays and works to get himself back in the action when out of position 
… Not afraid to take big shots down the stretch of games … Draws fouls at a decent rate and is solid when he gets there (82 FT on 4.5 FTA per game) …",

**Weakness**:
    "Though he has solid athleticism, he lacks great burst and explosiveness … Sometimes has a hard time separating off the dribble and has to take contested shots … Doesn’t get to the rim that much in half
court offense … Nothing more than decent as a leaper, and Miller doesn’t convert amongst the trees at a great rate (46 FG inside the arc) … Needs to add some muscle to his frame; not great at finishing through
contact at the moment … At times falls in love with the jump shot; can stand to improve on picking his spots … Could look to add a little more arch to his shot which can be flat … Has moments when aggressive 
pressure throws him off his game, but he usually does a good job adjusting to the defense … Won’t realize his true defensive potential until he adds the muscle needed to defend bigger PFs … Willing to pass the ball,
but isn’t much of a playmaker for others and is more so wired to score … Tough to see him posting up much at the NBA level given his lack of strength currently; can use his size to his advantage down low in college
at times but that will be more difficult against longer NBA defenders … Will be 21 years old as a rookie; is older than your typical one-and-done prospect …",

**Rating**:
    Athleticism: 9,
    Size: 9,
    Defense: 8,
    Strength: 8,
    Quickness: 8,
    Leadership: 7,
    Jump Shot: 7,
    NBA Ready: 8,
    Ball Handling: 7,
    Potential: 9,
    Passing: 8,
    Intangibles: 7

**NBA Comparison**: "Paul George"

**Mock Draf**: 2
"""

def SR_agent_response(player_info, existing_players):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": "Given the player's information, please generate a professional, authentic, and accurate scouting report for NBA draft prospects: " +
              f"Given Player: {json.dumps(player_info, indent=2)}"}
        ]
    )

    reply = response.choices[0].message.content.strip()
    return reply

if __name__ == "__main__":
    with open('Input/Test2.json', 'r', encoding='utf-8') as file:
        player_info = json.load(file)

    with open('data/Reed_Sheppard.json', 'r', encoding='utf-8') as file:
        existing_players = json.load(file)
        
    result = SR_agent_response(player_info, existing_players)

    print(result)