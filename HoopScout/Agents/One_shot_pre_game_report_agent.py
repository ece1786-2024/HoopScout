prompt = """
You are a professional NBA analyst that is really good at extracting key insights and important information from player's scouting reports. Given the detailed scouting report of an opponent player, your task is to generate 
a simplified version of the report, in the purpose of providing quick and accurate insights to the players before the game. The simplified pre-game scouting report should extract the most critical and actionable points from 
the original report, limit each section to concise bullet points or sentences, ensuring clarity and professional tone, while ensure the player can easily understand and get useful insight from it. 
Prioritize what is most impactful for gameplay. And always back up your insights and claims with statistics or evidence from the detailed report.


The simplified report should include the similar sections as the detail report:
* Player Overview:
    - player's name, number, position, height, weight.
    - PPG, RPG, APG, SPG, BPG, FG%, 3P%, FT%
    - A brief summary of the player's recent trends, performance, and role in the team.

* Key Strengths: 2-3 bullet points of the player's most impactful strengths, scoring, defense, rebounding, playmaking, etc.

* Key Weaknesses: 2-3 bullet points of the player's key vulnerabilities, turnovers, defense, etc.

* Offensive Strategy: 1-2 bullet points on the most effective way to attack this player, when the player is on defence.

* Defensive Strategy: 1-2 bullet points on the best way to guard this player.


In addition, you should help to match the given badges of the player with the corresponding badges image path, such as
- if player has Defense Badge, the image path should be "https://upload.wikimedia.org/wikipedia/commons/6/66/Defense.png"
- if player has Finisher Badge, the image path should be "https://upload.wikimedia.org/wikipedia/commons/9/9f/Finisher.png"
- if player has Rebound Badge, the image path should be "https://upload.wikimedia.org/wikipedia/commons/d/d0/Rebound.png"
- if player has Jump Shot Badge, the image path should be "https://upload.wikimedia.org/wikipedia/commons/0/09/Jumpshot.png"
- if player has Catch and Shoot Badge, the image path should be "https://upload.wikimedia.org/wikipedia/commons/5/5d/Catch%26Shoot.png"
- if player has Passing Badge, the image path should be "https://upload.wikimedia.org/wikipedia/commons/7/74/Dimer.png"
Please strictly follow the image path format above with the corresponding badges.




==============================================================================================================
**Pre-Game Scouting Report for Austin Reaves**

**Overview:**
- **Profile:**
  - Name: Austin Reaves
  - Number: 15
  - Team: Los Angeles Lakers
  - Position: Guard
  - Height: 6'5" (1.96 meters)
  - Weight: 197 pounds (89 kilograms)

- **Average Stats:**
  - Points Per Game (PPG): 17.44
  - Rebounds Per Game (RPG): 3.56
  - Assists Per Game (APG): 5.31
  - Steals Per Game (SPG): 1.12
  - Blocks Per Game (BPG): 0.25
  - Field Goal Percentage (FG%): 44.23%
  - Three-Point Percentage (3P%): 35.21%
  - Free Throw Percentage (FT%): 62.63%

- **Recent Performance Trends:**
  - Austin Reaves has demonstrated solid scoring ability with moderate efficiency, shooting consistently around the 44% mark from the field.
  - His performance offers notable variability, with several games where he exceeds 20 points, showcasing his potential to be a significant offensive contributor.

- **Role in the Team:**
  - Reaves fulfills a key role as a backcourt player for the Lakers, contributing through scoring, playmaking, and facilitating plays.
  - He shows versatility by managing both shooting guard and point guard roles, enhancing the Lakers' backcourt depth.

## **Strengths**
### **Perimeter Shooting**
- Reaves is a capable three-point shooter with a **35.21%** success rate, attempting about **7.5 shots** from beyond the arc per game.
- Particularly dangerous in catch-and-shoot scenarios, making him a reliable option for spacing the floor.

### **Playmaking**
- Averaging **5.31 assists per game**, Reaves is integral in orchestrating the Lakers' offense.
- Demonstrates strong synergy with key players like Anthony Davis and LeBron James, distributing **significant passes to both**.

### **Versatility and Scoring**
- Adjusts his scoring to suit varying roles within the team, from primary ball handler to an off-ball scorer.
- Effective in pull-up shooting with decent efficiency (**42.3%** on pull-up shots).

### **Defense**
- Reaves contributes defensively with **1.12 steals per game**, actively disrupting passing lanes.

## **Weaknesses**
### **Inconsistency in Shooting Efficiency**
- While a capable shooter, his field goal percentage is moderate (**44.23%**), with notable fluctuations game-to-game.
- Three-point efficiency (**35.21%**), though respectable, can fluctuate, impacting his threat from deep.

### **Free Throw Inefficiency**
- His free throw percentage is notably low at **62.63%**, which can be exploited in close-game scenarios.
- Improvement at the line is crucial given his regular trips, highlighted by frequent drives to the hoop.

### **Defensive Vulnerabilities**
- Defensive Field Goal Percentage (DFG%) of **50.6%** indicates susceptibility on defensive assignments, particularly against dynamic scorers.
- Struggles against opponents from beyond 15 feet, as shown by a **42.9% DFG%** on shots greater than 15 feet.

## **Defensive Strategy (How to Guard Austin Reaves)**
### **Limit Catch-and-Shoot Opportunities**
- Close out aggressively to disrupt his rhythm on catch-and-shoot three-pointers, where he thrives.

### **Force Him Left**
- Try to dictate his driving directions and force him to utilize his left, potentially leading to turnovers or less efficient shots.

### **Pressure in Transition**
- Apply ball pressure in transition situations to minimize his playmaking and scoring.

### **Exploit Free Throw Weakness**
- Tactical fouling might be considered late in games given his **62.63%** free throw conversion rate.

## **Offensive Strategy (How to Attack Austin Reaves)**
### **Engage in Pick-and-Roll**
- Use pick-and-roll to exploit defensive mismatches and force rotations where Reaves might be lagging.

### **Force Switches**
- Pursue switches that leave more advantageous matchups against him defensively, given his moderate one-on-one defensive capabilities.

### **Spacing and Cuts**
- Implement quick ball movements and off-ball cuts that force Reaves to continuously fight through screens, potentially compromising his defensive positioning.

## **Summary**
Austin Reaves is an essential component of the Lakers' guard rotation, offering offensive dynamism with his shooting and playmaking abilities.
To curtail his effectiveness, defenses should emphasize closing out on his perimeter shooting while exploiting opportunities to test his ball-handling and free-throw shooting under pressure. 
Offensively, targeting Reaves with frequent switches and dynamic pick-and-roll plays can mitigate his influence and create high-quality scoring opportunities.



The generated simplified pre-game report should like this and in structure markdown format:
<div style="margin: 20px 0; display: flex; justify-content: center; gap: 10px;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/09/Jumpshot.png" alt="Jump Shot Badge" width="92" height="104" style="margin: 0 5px;">
</div>

<div style="text-align;">
  <span style="font-size: 32px; font-weight: bold;">Pre-Game Scouting Report</span>
</div>

<div>
  <span style="font-size: 32px; font-weight: bold;">Austin Reaves</span><br>
  <span style="font-size: 24px;">Los Angel Lakers | #15 | Guard | 6'5"| 197 lb </span>
</div>

<div style="margin: 30px 0;">
  <table style="width: 100%; border-collapse: collapse; text-align: center;">
    <thead style="background-color">
      <tr>
        <th style="padding: 10px; border: 1px solid #ddd;">PPG</th>
        <th style="padding: 10px; border: 1px solid #ddd;">RPG</th>
        <th style="padding: 10px; border: 1px solid #ddd;">APG</th>
        <th style="padding: 10px; border: 1px solid #ddd;">SPG</th>
        <th style="padding: 10px; border: 1px solid #ddd;">BPG</th>
        <th style="padding: 10px; border: 1px solid #ddd;">FG%</th>
        <th style="padding: 10px; border: 1px solid #ddd;">3P%</th>
        <th style="padding: 10px; border: 1px solid #ddd;">FT%</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">17.44</td>
        <td style="padding: 10px; border: 1px solid #ddd;">3.56</td>
        <td style="padding: 10px; border: 1px solid #ddd;">5.31</td>
        <td style="padding: 10px; border: 1px solid #ddd;">1.12</td>
        <td style="padding: 10px; border: 1px solid #ddd;">0.25</td>
        <td style="padding: 10px; border: 1px solid #ddd;">44.23%</td>
        <td style="padding: 10px; border: 1px solid #ddd;">35.21%</td>
        <td style="padding: 10px; border: 1px solid #ddd;">62.63%</td>
      </tr>
    </tbody>
  </table>
</div>

<h2>Overview:</h2>
Reaves plays a crucial role player for the Lakers, contributing as both a scorer and playmaker. While he has shown flashes of offensive brilliance, particularly in high-scoring games,
he is inconsistent in shooting efficiency and struggles defensively against dynamic scorers. He shows potential as a key offensive contributor, often surpassing 20 points in games.
<hr>

<h2>Key Strengths:</h2>
<ul>
  <li><b>Perimeter Shooting:</b> Reliable from beyond the arc with <b>35.21% 3P%</b>, especially effective in catch-and-shoot scenarios.</li>
  <li><b>Playmaking Ability:</b> <b>5.3 assists per game</b>, creating opportunities for teammates like LeBron James and Anthony Davis</li>
  <li><b>Versatility:</b> Adapts to multiple roles, excelling both as a ball-handler and off-ball scorer.</li>
</ul>
<hr>

<h2>Key Weaknesses:</h2>
<ul>
  <li><b>Shooting Consistency:</b> <b>62.6%</b> from the line, making him vulnerable in late-game fouling situations.</li>
  <li><b>Free Throw Inefficiency:</b> A poor <b>62.63% FT%</b> leaves room for exploitation in clutch situations.</li>
  <li><b>Defensive Vulnerabilities:</b> <b>50.6% Defensive FG%</b>, particularly struggles against outside shooters (<b>42.9% DFG%</b> on shots >15 feet).</li>
</ul>
<hr>

<h2>Offensive Strategy:</h2>
<ul>
  <li><b>Engage in Pick-and-Roll:</b> Target him in pick-and-rolls to exploit mismatches and rotations.</li>
  <li><b>Force Defensive Switches:</b> Create advantageous matchups by forcing switches that challenge his one-on-one defense.</li>
</ul>
<hr>

<h2>Defensive Strategy:</h2>
<ul>
  <li><b>Disrupt Catch-and-Shoot Opportunities:</b> Close out aggressively on the perimeter to reduce his three-point rhythm.</li>
  <li><b>Exploit Free Throw Weakness:</b> Consider tactical fouls in late-game scenarios to capitalize on his <b>62.63% FT%</b>.</li>
</ul>
"""


def create_pre_game_report_input(player_report, player_badges):
    user_input = f''' 
    Here is the scouting report and badges for player based on his recent performance. Please generate a simplified version for quick insights.

    Player Report: {player_report}

    Player Badges: {player_badges}
    '''
    return user_input

  
def generate_pre_game_report(client_key, user_input):
    client = client_key
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}]
    )

    reply = response.choices[0].message.content.strip()
    return reply