import textstat
import pandas as pd


readability_prompt = ''' 
Extract the text from the given markdown format report output, so later readability of this text can be checked.
          
For example if the markdown format report output is:
<div style="text-align:center;">
  <span style="font-size: 32px; font-weight: bold;">Pre-Game Scouting Report</span>
</div>

<div style="margin: 20px 0;">
<img src="Data/Lakers/Anthony_Davis/Portrait.jpg" alt="Portrait" width="520" height="380" style="border: 1px solid #ddd; border-radius: 5px; padding: 5px;">
</div>

<div style="margin: 20px 0;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/66/Defense.png" alt="Defense Badge" width="92" height="104" style="margin: 0 5px;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/9f/Finisher.png" alt="Inside Scorer Badge" width="92" height="104" style="margin: 0 5px;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/d/d0/Rebound.png" alt="Rebounding Badge" width="92" height="104" style="margin: 0 5px;">
</div>

<div>
  <span style="font-size: 32px; font-weight: bold;">Anthony Davis</span><br>
  <span style="font-size: 24px;">Los Angeles Lakers | #3 | Power Forward/Center</span>
</div>

<div style="margin: 30px 0;">
  <table style="width: 100%; border-collapse: collapse; text-align: center;">
    <thead style="background-color: #eee;">
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
        <td style="padding: 10px; border: 1px solid #ddd;">30.13</td>
        <td style="padding: 10px; border: 1px solid #ddd;">11.13</td>
        <td style="padding: 10px; border: 1px solid #ddd;">2.8</td>
        <td style="padding: 10px; border: 1px solid #ddd;">1.33</td>
        <td style="padding: 10px; border: 1px solid #ddd;">1.93</td>
        <td style="padding: 10px; border: 1px solid #ddd;">56.55%</td>
        <td style="padding: 10px; border: 1px solid #ddd;">34.45%</td>
        <td style="padding: 10px; border: 1px solid #ddd;">77.08%</td>
      </tr>
    </tbody>
  </table>
</div>

<h2>Overview:</h2>
Anthony Davis is a dominant force for the Los Angeles Lakers, known for his scoring and defensive capabilities. Recently, he's been on an offensive surge, leading with high points against key teams. As both a primary scorer and significant defender, Davis's role is crucial on both ends.

<hr>

<h2>Key Strengths:</h2>
<ul>
  <li>Highly efficient around the basket, with a 56.55% FG%.</li>
  <li>Strong rebounding ability, averaging 11.13 RPG.</li>
  <li>Imposing defensive presence, particularly in blocking shots.</li>
</ul>
<hr>

<h2>Key Weaknesses:</h2>
<ul>
  <li>Limited consistency in three-point shooting.</li>
  <li>Prone to turnovers with 2.6 per game.</li>
  <li>Occasional variability in shooting efficiency under pressure.</li>
</ul>
<hr>

<h2>Offensive Strategy:</h2>
<ul>
  <li>Focus on perimeter shooting as Davis excels defending near the basket.</li>
  <li>Utilize quick ball movement to exploit his defensive positioning.</li>
</ul>
<hr>

<h2>Defensive Strategy:</h2>
<ul>
  <li>Double-team in the post to challenge lower percentage shots.</li>
  <li>Box out and limit his second-chance points from rebounds.</li>
</ul>


The following text should be extracted:
Pre-Game Scouting Report
Anthony Davis
Los Angeles Lakers | #3 | Power Forward/Center

Overview:
Anthony Davis is a dominant force for the Los Angeles Lakers, known for his scoring and defensive capabilities. Recently,
he's been on an offensive surge, leading with high points against key teams. As both a primary scorer and significant defender, Davis's role is crucial on both ends.

Key Strengths:
Highly efficient around the basket, with a 56.55% FG%.
Strong rebounding ability, averaging 11.13 RPG.
Imposing defensive presence, particularly in blocking shots.

Key Weaknesses:
Limited consistency in three-point shooting.
Prone to turnovers with 2.6 per game.
Occasional variability in shooting efficiency under pressure.

Offensive Strategy:
Focus on perimeter shooting as Davis excels defending near the basket.
Utilize quick ball movement to exploit his defensive positioning.

Defensive Strategy:
Double-team in the post to challenge lower percentage shots.
Box out and limit his second-chance points from rebounds.
'''

def create_readability_check_input(html_output):
    user_input = f''' Extract the relevant text from the given markdown format report output, so later readability of this text can be checked.
    {html_output}
    '''
    return user_input

def flesch_kincaid_grade_readability_check(client_key, user_input):
    client = client_key
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
            {"role": "system", "content": readability_prompt},
            {"role": "user", "content": user_input}]
    )

    # Print the response
    reply = response.choices[0].message.content.strip()
    grade_level = textstat.flesch_kincaid_grade(reply)

    return grade_level




def badges_check(player_pth):
    asb_pth = player_pth + "Advanced_Score_Boxes.csv"
    os_pth = player_pth + "Overall_Shooting.csv"
    grs_pth = player_pth + "General_Range_Shooting.csv"
    ds_pth = player_pth + "Dribbles_Shooting.csv"
    pt_pth = player_pth + "Pass_To.csv"
    pf_pth = player_pth + "Pass_From.csv"
    d_pth =  player_pth + "Tracking_Defense.csv"


    Advanced_Score_Boxes_df = pd.read_csv(asb_pth)
    General_Range_Shooting_df = pd.read_csv(grs_pth)
    Dribbles_Shooting_df = pd.read_csv(ds_pth)
    Tracking_Defense_df = pd.read_csv(d_pth)


    ppg = Advanced_Score_Boxes_df["PTS"].mean()
    rpg = Advanced_Score_Boxes_df["REB"].mean()
    apg = Advanced_Score_Boxes_df["AST"].mean()
    spg = Advanced_Score_Boxes_df["STL"].mean()
    bpg = Advanced_Score_Boxes_df["BLK"].mean()
    fgp = Advanced_Score_Boxes_df["FG%"].mean()
    tpp = Advanced_Score_Boxes_df["3P%"].mean()
    ftp = Advanced_Score_Boxes_df["FT%"].mean()
    total_min= Advanced_Score_Boxes_df['MIN'].apply(lambda x: sum(float(t) * 60 ** i for i, t in enumerate(reversed(x.split(':')))) / 60)
    minutes_per_game = total_min.mean()
    fta = Advanced_Score_Boxes_df["FTA"].mean()
    turnovers = Advanced_Score_Boxes_df["TOV"].mean()
    orb = Advanced_Score_Boxes_df["OREB"].mean()
    drb = Advanced_Score_Boxes_df["DREB"].mean()


    overall_diff = Tracking_Defense_df.loc[Tracking_Defense_df['Category'] == "Overall", "DIFF%"].values[0]
    pull_up_fg = General_Range_Shooting_df.loc[General_Range_Shooting_df['Category'] == "Pull Ups", 'FG%'].values[0]
    pull_up_freq = General_Range_Shooting_df.loc[General_Range_Shooting_df['Category'] == "Pull Ups", 'Freq%'].values[0]
    dribbles_2_fg = Dribbles_Shooting_df.loc[Dribbles_Shooting_df['Category'] == "2 Dribbles", 'FG%'].values[0]
    dribbles_3_6_fg = Dribbles_Shooting_df.loc[Dribbles_Shooting_df['Category'] == "3-6 Dribbles", 'FG%'].values[0]
    dribbles_2_freq = Dribbles_Shooting_df.loc[Dribbles_Shooting_df['Category'] == "2 Dribbles", 'Freq%'].values[0]
    dribbles_3_6_freq = Dribbles_Shooting_df.loc[Dribbles_Shooting_df['Category'] == "3-6 Dribbles", 'Freq%'].values[0]
    cs_fg = General_Range_Shooting_df.loc[General_Range_Shooting_df['Category'] == "Catch and Shoot", 'FG%'].values[0]
    cs_3fg = General_Range_Shooting_df.loc[General_Range_Shooting_df['Category'] == "Catch and Shoot", '3P%'].values[0]
    cs_freq = General_Range_Shooting_df.loc[General_Range_Shooting_df['Category'] == "Catch and Shoot", 'Freq%'].values[0]
    cs_2fgm = General_Range_Shooting_df.loc[General_Range_Shooting_df['Category'] == "Catch and Shoot", '2FGM'].values[0]
    cs_3fgm = General_Range_Shooting_df.loc[General_Range_Shooting_df['Category'] == "Catch and Shoot", '3PM'].values[0]
    cs_3fg = pd.to_numeric(cs_3fg, errors='coerce')
    cs_3fgm = pd.to_numeric(cs_3fgm, errors='coerce')
    cs_2fgm = pd.to_numeric(cs_2fgm, errors='coerce')
    cs_pts = cs_3fgm * 3 + cs_2fgm * 2
    cs_fga = General_Range_Shooting_df.loc[General_Range_Shooting_df['Category'] == "Catch and Shoot", 'FGA'].values[0]
    fg_10feet = General_Range_Shooting_df.loc[General_Range_Shooting_df['Category'] == "Less than 10 ft", 'FG%'].values[0]
    freq_10feet = General_Range_Shooting_df.loc[General_Range_Shooting_df['Category'] == "Less than 10 ft", 'Freq%'].values[0]
    fgm_10feet = General_Range_Shooting_df.loc[General_Range_Shooting_df['Category'] == "Less than 10 ft", 'FGM'].values[0]
    pts_paint = fgm_10feet * 2
    at_rate = apg/turnovers


    badges = []
    if minutes_per_game <= 25:
        return badges
    
    if (overall_diff <= -2.5) & (bpg >= 1.5 or spg >= 1.5):
        badges.append("Defense Badge")

    if (pull_up_fg >= 40) & (pull_up_freq >= 20) & ((dribbles_3_6_fg >= 40) or (dribbles_2_fg >= 40) or (dribbles_3_6_freq >= 30) or (dribbles_2_freq >= 30)) & (ppg >= 15):
        badges.append("Jump Shot Badge")

    if (cs_fg >= 45) & (cs_3fg >= 38) & (cs_freq >= 40) & (cs_pts >= 6) & (cs_fga >= 3):
        badges.append("Catch and Shoot Badge")

    if fg_10feet >= 60 and freq_10feet >= 50 and pts_paint >= 10 and fta >= 5 and ppg >= 15:
        badges.append("Inside Scorer Badge")

    if apg >= 5 and at_rate >= 2.3 and turnovers <= 3:
        badges.append("Passing Badge")

    if  rpg >= 8 and orb >= 2 and drb >= 6:
        badges.append("Rebounding Badge")

    return badges

