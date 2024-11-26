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

    return Player_Profile, Advanced_Score_Boxes_string, Overall_Shooting_string, General_Range_Shooting_string, Dribbles_Shooting_string, Pass_To_string, Pass_From_string, Tracking_Defense_string
