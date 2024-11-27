prompt = '''
You are a basketball analytics expert tasked with evaluating a player's performance based on their statistics. Your goal is to determine  which skill badges the player qualifies for, according to predefined criteria. 
The badges reflect specific abilities, there are 6 types of badges.

Here are the predefined criteria and thresholds for each badge:

* Defense Badge
Defensive Impact Differential (DIFF%): ≤ -5%
Blocks Per Game (BLK): ≥ 1.5
Steals Per Game (STL): ≥ 1.5 (alternative if BLK criterion isn't met)
Minutes Played: ≥ 25 minutes per game

* Jump Shot Badge
Pull-Up Field Goal Percentage: ≥ 40%
Frequency of Pull-Up Shots (Freq%): ≥ 20%
Field Goal Percentage with 3+ Dribbles: ≥ 40%
Points Per Game (PPG): ≥ 15

* Catch and Shoot Badge
Catch and Shoot FG%: ≥ 45%
Catch and Shoot 3P%: ≥ 38%
Frequency (Freq%): ≥ 40%
Points from Catch and Shoot: ≥ 6 PPG
Attempts Per Game: ≥ 3

* Inside Scorer Badge
FG% Less Than 10 Feet: ≥ 60%
Frequency of Shots Less Than 10 Feet: ≥ 50%
Points in the Paint Per Game: ≥ 10 PPG
Free Throw Attempts Per Game (FTA): ≥ 5
Points Per Game (PPG): ≥ 15

* Passing Badge
Assists Per Game (APG): ≥ 5
Assist-to-Turnover Ratio (A/T): ≥ 2.5
Turnovers Per Game (TOV): Below league average for primary ball-handlers

* Rebounding Badge
Rebounds Per Game (RPG): ≥ 8
Offensive Rebounds Per Game (OREB): ≥ 2
Defensive Rebounds Per Game (DREB): ≥ 6
Minutes Played: ≥ 25 minutes per game
'''


def create_badge_input(profile_pth, asb_pth, os_pth, grs_pth, ds_pth, pt_pth, pf_pth, d_pth, avg_stats):
    user_input = f'''
    Given the player's information and stats, please list the badgese he has. Only list the name of each badge the player has.

    Player's profile:
    {profile_pth}

    Advanced Score Boxes:
    {asb_pth}

    Overall Shooting stats: 
    {os_pth}

    General Range Shooting stats: 
    {grs_pth}

    Dribbles Shooting stats: 
    {ds_pth}

    Pass TO stats: 
    {pt_pth}

    Pass From stats: 
    {pf_pth}

    Tracking Defense stats: 
    {d_pth}

    Player Average Stats:
    {avg_stats}
    '''
    return user_input


def generate_badge(client_key, user_input):
    client = client_key
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}]
    )

    # Print the response
    reply = response.choices[0].message.content.strip()
    return reply