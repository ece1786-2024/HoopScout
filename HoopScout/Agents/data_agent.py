import pandas as pd
import json

def data_processing(profile_pth, asb_pth, os_pth, grs_pth, ds_pth, pt_pth, pf_pth, d_pth):
    with open(profile_pth, 'r') as file:
        Player_Profile = json.load(file)

    Advanced_Score_Boxes_df = pd.read_csv(asb_pth)
    Advanced_Score_Boxes_string = Advanced_Score_Boxes_df.to_string(index=False)

    Overall_Shooting_df = pd.read_csv(os_pth)
    Overall_Shooting_string = Overall_Shooting_df.to_string(index=False)

    General_Range_Shooting_df = pd.read_csv(grs_pth)
    General_Range_Shooting_string = General_Range_Shooting_df.to_string(index=False)

    Dribbles_Shooting_df = pd.read_csv(ds_pth)
    Dribbles_Shooting_string = Dribbles_Shooting_df.to_string(index=False)

    Pass_To_df = pd.read_csv(pt_pth)
    Pass_To_string = Pass_To_df.to_string(index=False)
 
    Pass_From_df = pd.read_csv(pf_pth)
    Pass_From_string = Pass_From_df.to_string(index=False)

    Tracking_Defense_df = pd.read_csv(d_pth)
    Tracking_Defense_string = Tracking_Defense_df.to_string(index=False)

    AVG_stats = average_stats(Advanced_Score_Boxes_df)

    return Player_Profile, Advanced_Score_Boxes_string, Overall_Shooting_string, General_Range_Shooting_string, Dribbles_Shooting_string, Pass_To_string, Pass_From_string, Tracking_Defense_string, AVG_stats

def team_data_processing(roster_pth, asb_pth, os_pth, grs_pth, ds_pth, pt_pth, pf_pth, s_pth):

    Roster_df = pd.read_csv(roster_pth)
    Roster_string = Roster_df.to_string(index=False)

    Advanced_Score_Boxes_df = pd.read_csv(asb_pth)
    Advanced_Score_Boxes_string = Advanced_Score_Boxes_df.to_string(index=False)

    Overall_Shooting_df = pd.read_csv(os_pth)
    Overall_Shooting_string = Overall_Shooting_df.to_string(index=False)

    General_Range_Shooting_df = pd.read_csv(grs_pth)
    General_Range_Shooting_string = General_Range_Shooting_df.to_string(index=False)

    Dribbles_Shooting_df = pd.read_csv(ds_pth)
    Dribbles_Shooting_string = Dribbles_Shooting_df.to_string(index=False)

    Pass_To_df = pd.read_csv(pt_pth)
    Pass_To_string = Pass_To_df.to_string(index=False)
 
    Pass_From_df = pd.read_csv(pf_pth)
    Pass_From_string = Pass_From_df.to_string(index=False)

    Stats_df = pd.read_csv(s_pth)
    Stats_string = Stats_df.to_string(index=False)

    AVG_stats = average_stats(Advanced_Score_Boxes_df)

    return Roster_string, Advanced_Score_Boxes_string, Overall_Shooting_string, General_Range_Shooting_string, Dribbles_Shooting_string, Pass_To_string, Pass_From_string, Stats_string


def average_stats(Advanced_Score_Boxes_df):
    """ 
    average PPG, RPG, APG, SPG, BPG, FG%, 3P%, FT%
    """
    avg_dict = {"PPG": round(Advanced_Score_Boxes_df["PTS"].mean(), 2),
    "RPG": round(Advanced_Score_Boxes_df["REB"].mean(), 2),
    "APG": round(Advanced_Score_Boxes_df["AST"].mean(), 2),
    "SPG": round(Advanced_Score_Boxes_df["STL"].mean(), 2),
    "BPG": round(Advanced_Score_Boxes_df["BLK"].mean(), 2),
    "FG%": round(Advanced_Score_Boxes_df["FG%"].mean(), 2),
    "3P%": round(Advanced_Score_Boxes_df["3P%"].mean(), 2),
    "FT%": round(Advanced_Score_Boxes_df["FT%"].mean(), 2)}
    
    return avg_dict