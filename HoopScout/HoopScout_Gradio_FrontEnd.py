import gradio as gr
import json
from Agents import data_agent, badge_agent, report_agent, pre_game_report_agent
from openai import OpenAI
import pandas as pd
import os
import shutil

# Initialize the OpenAI client
client = OpenAI(api_key= "")

# Define the function to process inputs and generate output
# def generate_pre_game_report(profile_json, asb_file, os_file, grs_file, ds_file, pt_file, pf_file, d_file):
#     # DATA Processing
#     with open(profile_json, 'r') as file:
#             player_profile = json.load(file)

#     Advanced_Score_Boxes_df = pd.read_csv(asb_file)
#     stats_1 = Advanced_Score_Boxes_df.to_string(index=False)

#     Overall_Shooting_df = pd.read_csv(os_file)
#     stats_2 = Overall_Shooting_df.to_string(index=False)

#     General_Range_Shooting_df = pd.read_csv(grs_file)
#     stats_3 = General_Range_Shooting_df.to_string(index=False)

#     Dribbles_Shooting_df = pd.read_csv(ds_file)
#     stats_4 = Dribbles_Shooting_df.to_string(index=False)

#     Pass_To_df = pd.read_csv(pt_file)
#     stats_5 = Pass_To_df.to_string(index=False)
 
#     Pass_From_df = pd.read_csv(pf_file)
#     stats_6 = Pass_From_df.to_string(index=False)

#     Tracking_Defense_df = pd.read_csv(d_file)
#     stats_7 = Tracking_Defense_df.to_string(index=False)

    # stats_8 = {"PPG": round(Advanced_Score_Boxes_df["PTS"].mean(), 2),
    # "RPG": round(Advanced_Score_Boxes_df["REB"].mean(), 2),
    # "APG": round(Advanced_Score_Boxes_df["AST"].mean(), 2),
    # "SPG": round(Advanced_Score_Boxes_df["STL"].mean(), 2),
    # "BPG": round(Advanced_Score_Boxes_df["BLK"].mean(), 2),
    # "FG%": round(Advanced_Score_Boxes_df["FG%"].mean(), 2),
    # "3P%": round(Advanced_Score_Boxes_df["3P%"].mean(), 2),
    # "FT%": round(Advanced_Score_Boxes_df["FT%"].mean(), 2)}
    
#     Portrait_path = "https://upload.wikimedia.org/wikipedia/commons/7/7d/Portrait_AD.jpg"

#     # Generate Badges
#     badge_user_input = badge_agent.create_badge_input(player_profile, stats_1, stats_2, stats_3, stats_4, stats_5, stats_6, stats_7, stats_8)
#     badge_result = badge_agent.generate_badge(client, badge_user_input)

#     # Generate detail analysis
#     report_user_input = report_agent.create_report_input(player_profile, stats_1, stats_2, stats_3, stats_4, stats_5, stats_6, stats_7, stats_8)
#     report_result = report_agent.generate_report(client, report_user_input)

#     # Generate Pre-Game Report
#     pre_game_report_user_input = pre_game_report_agent.create_pre_game_report_input(report_result, badge_result, Portrait_path)
#     pre_game_report_result = pre_game_report_agent.generate_pre_game_report(client, pre_game_report_user_input)

#     # Return the HTML result
#     cleaned_html = pre_game_report_result.replace("```markdown", "").replace("```", "")
#     return cleaned_html

expected_files = [
        "portrait.jpg",
        "profile.json",
        "advanced_score_boxes.csv",
        "overall_shooting.csv",
        "general_range_shooting.csv",
        "dribbles_shooting.csv",
        "pass_to.csv",
        "pass_from.csv",
        "tracking_defense.csv"]
data_dict = {}
temp_path = "temp_folder"

def generate_pre_game_report(files):
    if(len(files) != 9):
        print("incorrect file numbers")
        exit(0)

    os.makedirs(temp_path, exist_ok=True)

    stats_8 = {}

    for file in files:
        file_name = os.path.basename(file.name).lower()
        # print(file_name)
        if file_name in expected_files:
            if file_name == "portrait.jpg":
                data_dict[file_name] = file.name
                # save_path = os.path.join(temp_path, file_name)
                # shutil.copy(file.name, save_path)
                # data_dict[file_name] = save_path #os.path.abspath(save_path)
            if file_name == "profile.json":
                with open(file, 'r') as f:
                    data_dict[file_name] = json.load(f)
            if file_name.endswith(".csv"):
                df = pd.read_csv(file)
                if file_name == "advanced_score_boxes.csv":
                    stats_8 = {"PPG": round(df["PTS"].mean(), 2),
                               "RPG": round(df["REB"].mean(), 2),
                               "APG": round(df["AST"].mean(), 2),
                               "SPG": round(df["STL"].mean(), 2),
                               "BPG": round(df["BLK"].mean(), 2),
                               "FG%": round(df["FG%"].mean(), 2),
                               "3P%": round(df["3P%"].mean(), 2),
                               "FT%": round(df["FT%"].mean(), 2)}
                data_dict[file_name] = df.to_string(index=False)


    # print(data_dict.keys())
    print(data_dict["portrait.jpg"])

    # Generate Badges
    badge_user_input = badge_agent.create_badge_input(data_dict["profile.json"], 
                                                      data_dict["advanced_score_boxes.csv"], 
                                                      data_dict["overall_shooting.csv"], 
                                                      data_dict["general_range_shooting.csv"],
                                                      data_dict["dribbles_shooting.csv"], 
                                                      data_dict["pass_to.csv"], 
                                                      data_dict["pass_from.csv"],
                                                      data_dict["tracking_defense.csv"], 
                                                      stats_8)
    badge_result = badge_agent.generate_badge(client, badge_user_input)
    print("badge finished.")

    # Generate detail analysis
    report_user_input = report_agent.create_report_input(data_dict["profile.json"], 
                                                         data_dict["advanced_score_boxes.csv"], 
                                                         data_dict["overall_shooting.csv"], 
                                                         data_dict["general_range_shooting.csv"],
                                                         data_dict["dribbles_shooting.csv"], 
                                                         data_dict["pass_to.csv"], 
                                                         data_dict["pass_from.csv"],
                                                         data_dict["tracking_defense.csv"], 
                                                         stats_8)
    report_result = report_agent.generate_report(client, report_user_input)
    print("report finished.")

    # Generate Pre-Game Report
    pre_game_report_user_input = pre_game_report_agent.create_pre_game_report_input(report_result, badge_result)

    pre_game_report_result = pre_game_report_agent.generate_pre_game_report(client, pre_game_report_user_input)
    print("pre game report finished.")

    # Return the HTML result
    cleaned_html = pre_game_report_result.replace("```markdown", "").replace("```", "")
    return data_dict["portrait.jpg"], cleaned_html

# Gradio Interface
interface = gr.Interface(
    fn=generate_pre_game_report,
    inputs=gr.Files(file_types=[".json", ".csv", ".jpg"], label="Upload Player Data Files"),
    outputs= [gr.Image(label="Portrait") ,gr.HTML(label="Generated Pre-Game Report")],
    title="Pre-Game Report Generator",
    description="Upload the required player data files to generate a detailed pre-game report. The JSON file should contain the player's profile."
)

# with gr.Blocks() as demo:
#     img1 = gr.Image(label="Portrait")
#     with gr.Row():
#         img2 = gr.Image(label="badge")

# Launch the Gradio app
if __name__ == "__main__":
    interface.launch()
    # os.remove(temp_path + "/portrait.jpg")
    # os.remove(temp_path)