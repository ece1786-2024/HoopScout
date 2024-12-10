# File Structure
1. ```Agents``` Include the agents used or tested in the project.
2. ```Badges``` Include the badge images.
3. ```Data``` Include input data. A total of two teams: Celtics and Lakers, a total of 18 NBA players, one team data, and one test person.
4. ```Evaluation``` Include the evaluation metrics and python script to run the evaluation.
5. ```HoopScout_single_prompt``` Include a single prompt test file.
6. ```HoopScout_team``` Include the code to generate team reports.
7. ```Output``` Include the pre-game reports for all 18 players.

# How to run (Gradio)
0. Make sure the OpenAI key is valid before proceeding.
1. Clone the project into local
2. ```python3 HoopScout_Gradio_FrontEnd.py``` to open a local web server
3. Open a browser, go to ```http://127.0.0.1:7860```
4. Click the left box "Click to Upload", go to the data folder, select a team folder and click into a player's folder
5. Select all 9 files inside the player folder and comfirm, then click the submit button
6. After 30s to 1min, the pre-game scouting report will be displayed on the right hand side of the interface
