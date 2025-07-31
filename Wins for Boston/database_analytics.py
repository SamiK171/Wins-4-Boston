from database_connector import get_cursor
from tkinter import *
from tkinter import ttk
import tkinter as tk

mycursor = get_cursor()

def viewing_data():

    new_window = Toplevel()
    new_window.geometry("1000x1000")
    
    databaseViewer = "SELECT * From celtics2425stat"

    mycursor.execute(databaseViewer)

    myresult = mycursor.fetchall()

    tree = ttk.Treeview(new_window, columns=("Opponent", "Game Result", "Points (Tm)", "Opponent Points (Opp)", "Wins (W)"
    , "Losses (L)", "id"))
    tree.heading("Opponent", text="Opponent Team")
    tree.heading("Game Result", text="Game Result")
    tree.heading("Points (Tm)", text="Points (Tm)")
    tree.heading("Opponent Points (Opp)", text="Opponent Points (Opp)")
    tree.heading("Wins (W)", text="Wins (W)")
    tree.heading("Losses (L)", text="Losses (L)")
    tree.heading("id", text="id")
    tree.pack(fill=tk.BOTH, expand=True)

    for row in myresult:
        tree.insert("", "end", values=row)

def win_nextyear(): #comparison of total seasonal wins and losses using if statements to anticipate chance of winning

    new_window = Toplevel()
    new_window.geometry = ("1000x1000")

    winGrabber = "SELECT MAX(`Wins (W)`) From celtics2425stat"
    mycursor.execute(winGrabber)
    winnerResult = mycursor.fetchone() #fetches the MAX value
    total_wins = winnerResult[0] #takes the 0th index of the value. without the index, a tuple value would be returned (eg. 61, )

    lossGrabber = "SELECT MAX(`Losses (L)`) From celtics2425stat"
    mycursor.execute(lossGrabber)
    lossResult = mycursor.fetchone()
    total_loss = lossResult[0]

    pointGrabber = "SELECT SUM(`Points (Tm)`) From celtics2425stat"
    mycursor.execute(pointGrabber)
    pointResult = mycursor.fetchone()
    total_season_points = pointResult[0]
    
    oppPointGrabber = "SELECT SUM(`Opponent Points (Opp)`) From celtics2425stat"
    mycursor.execute(oppPointGrabber)
    opp_point_result = mycursor.fetchone()
    total_opp_points = opp_point_result[0]

    Label(new_window, text="Boston Celtics' Total Wins, Losses and Points in the 2024-2025 Regular Season:", font=("Arial", 30, "bold")).pack()
    Label(new_window, text="Total Wins: " + str(total_wins), font=("Arial", 23)).pack()
    Label(new_window, text="Total Losses: " + str(total_loss), font=("Arial", 23)).pack()

    Label(new_window, text="Total Seasonal Points: " + str(total_season_points), font=("Arial", 23)).pack()
    Label(new_window, text="Total Opposing Teams Seasonal Points: " + str(total_opp_points), font=("Arial", 23)).pack()
    
    if total_wins > total_loss and total_season_points > total_opp_points:
        Label(new_window, text="Therefore, the Boston Celtics have a greater chance of winning next year!", font=("Arial", 23)).pack()
    else:
        Label(new_window, text="Therefore, the Boston Celtics have a lower chance of winning next year!", font=("Arial", 23)).pack()

def against_team(): #comparison of total seasonal wins and losses against specific teams using if statements to anticipate winning chances
    new_window = Toplevel()
    new_window.geometry("1000x1000")

    Label(new_window, text="Select an NBA Team", font=('Arial', 23)).pack()  

    teams_nba_query = "SELECT Opponent FROM celtics2425stat"
    mycursor.execute(teams_nba_query)
    teams_fetcher = mycursor.fetchall()
    teams_list = [item[0] for item in teams_fetcher]

    option_var = tk.StringVar()
    option_var.set(teams_list[0])  

    dropdown_menu = ttk.Combobox(new_window, textvariable=option_var, values=teams_list, state='readonly')
    dropdown_menu.pack(pady = 15)

    wins_label = Label(new_window, text="", font=('Arial', 23))
    wins_label.pack()

    loss_label = Label(new_window, text="", font=('Arial', 23))
    loss_label.pack()

    pts_label = Label(new_window, text="", font=('Arial', 23))
    pts_label.pack()

    opps_label = Label(new_window, text="", font=('Arial', 23))
    opps_label.pack()

    chance_label = Label(new_window, text="", font=('Arial', 23))
    chance_label.pack()

    def against_logic():

        opposing_team = option_var.get()

        if opposing_team in teams_list: #checks if user's input is a team name or not
            win_grabber_against_team = "SELECT COUNT(*) AS wins_against_team From celtics2425stat WHERE Opponent = %s AND `Game Result` = 'W'"
            mycursor.execute(win_grabber_against_team, (opposing_team,))
            win_grab_fetcher = mycursor.fetchone()
            wins_against_opps = win_grab_fetcher[0]

            loss_grabber_against_team = "SELECT COUNT(*) AS loss_against_team From celtics2425stat WHERE Opponent = %s AND `Game Result` = 'L'"
            mycursor.execute(loss_grabber_against_team, (opposing_team,))
            loss_grab_fetcher = mycursor.fetchone()
            loss_against_opps = loss_grab_fetcher[0]

            points_against_team_grabber = "SELECT SUM(`Points (Tm)`) FROM celtics2425stat WHERE Opponent = %s"
            mycursor.execute(points_against_team_grabber, (opposing_team,))
            points_against_team_fetcher = mycursor.fetchone()
            points_against_team = points_against_team_fetcher[0]

            opp_team_point_grabber = "SELECT SUM(`Opponent Points (Opp)`) FROM celtics2425stat WHERE Opponent = %s"
            mycursor.execute(opp_team_point_grabber, (opposing_team,))
            opp_team_point_fetcher = mycursor.fetchone()
            opp_team_points = opp_team_point_fetcher[0]

            wins_label.config(text="Wins Against {}: ".format(opposing_team) + str(wins_against_opps), font=("Arial", 17))
            loss_label.config(text="Losses Against {}: ".format(opposing_team) + str(loss_against_opps), font=("Arial", 17))

            pts_label.config(text="Total Points Against {}: ".format(opposing_team) + str(points_against_team), font=("Arial", 17))
            opps_label.config(text="Total Opponent Points: " + str(opp_team_points), font=("Arial", 17))

            if wins_against_opps > loss_against_opps and points_against_team > opp_team_points:
                chance_label.config(text="Boston Celtics have a greater chance of winning against {} next season!".format(opposing_team), font=("Arial", 17))
            elif wins_against_opps > loss_against_opps and points_against_team < opp_team_points:
                chance_label.config(text="Boston Celtics have a greater chance of winning against {} next season!".format(opposing_team), font=("Arial", 17))
            elif wins_against_opps < loss_against_opps and points_against_team > opp_team_points:
                chance_label.config(text="Boston Celtics have a lower chance of winning against {} next season!".format(opposing_team), font=("Arial", 17))
            elif wins_against_opps == loss_against_opps and points_against_team > opp_team_points:
                chance_label.config(text="Boston Celtics have a greater chance of winning against {} next season!".format(opposing_team), font=("Arial", 17))
            elif wins_against_opps == loss_against_opps and points_against_team < opp_team_points:
                chance_label.config(text="Boston Celtics have a lower chance of winning against {} next season!".format(opposing_team), font=("Arial", 17))
            else:
                chance_label.config(text="Boston Celtics have a lower chance of winning against {} next season!".format(opposing_team), font=("Arial", 17))
        elif opposing_team == "Boston Celtics":
            chance_label.config(text="You must enter the name of an OPPOSING NBA Team!", font=("Arial", 23))
        else:
            chance_label.config(text="You must enter the name of an NBA team!", font=("Arial", 23))
    submit_button = Button(new_window, text="Submit", command=against_logic)
    submit_button.pack()