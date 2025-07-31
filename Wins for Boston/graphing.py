import matplotlib.pyplot as plt
import numpy as np
from database_connector import get_cursor
from tkinter import *

mycursor = get_cursor()

def graph_display():

    new_selection_window = Toplevel()
    new_selection_window.geometry("1000x1000")

    def wins_loss_bar():
        #loss list conversion
        loss_nba_query = "SELECT (`Losses (L)`) FROM celtics2425stat"
        mycursor.execute(loss_nba_query)
        loss_fetcher = mycursor.fetchall()
        loss_list = [item[0] for item in loss_fetcher]

        #wins list conversion
        wins_nba_query = "SELECT (`Wins (W)`) FROM celtics2425stat"
        mycursor.execute(wins_nba_query)
        wins_fetcher = mycursor.fetchall()
        wins_list = [item[0] for item in wins_fetcher]

        #x-and-y coordinates
        wins_np = np.array(wins_list)
        loss_np = np.array(loss_list)

        plt.bar(wins_np, loss_np) #teams is the x-axis, wins is the y-axis
        plt.xlabel("Wins")
        plt.ylabel("Losses")

        plt.title("Boston Celtics' Wins vs Losses")
        
        plt.show()

    def wins_loss_line():
            loss_nba_query = "SELECT (`Losses (L)`) FROM celtics2425stat"
            mycursor.execute(loss_nba_query)
            loss_fetcher = mycursor.fetchall()
            loss_list = [item[0] for item in loss_fetcher]

            #wins list conversion
            wins_nba_query = "SELECT (`Wins (W)`) FROM celtics2425stat"
            mycursor.execute(wins_nba_query)
            wins_fetcher = mycursor.fetchall()
            wins_list = [item[0] for item in wins_fetcher]

            #x-and-y coordinates
            wins_np = np.array(wins_list)
            loss_np = np.array(loss_list)

            plt.xlabel("Wins")
            plt.ylabel("Losses")

            plt.plot(wins_np, loss_np, marker='o', linestyle='-', color='green')

            plt.title("Boston Celtics' Wins vs Losses")
            
            plt.grid(True)
            plt.tight_layout()
            plt.show()
    
    def teams_vs_opp_bar():

        #team points list conversion
        team_pts_nba_query = "SELECT (`Points (Tm)`) FROM celtics2425stat"
        mycursor.execute(team_pts_nba_query)
        team_pts_fetcher = mycursor.fetchall()
        team_pts_list = [item[0] for item in team_pts_fetcher]

        #opp points list conversion
        opp_pts_query = "SELECT (`Opponent Points (Opp)`) FROM celtics2425stat"
        mycursor.execute(opp_pts_query)
        opp_pts_fetcher = mycursor.fetchall()
        opp_pts_list = [item[0] for item in opp_pts_fetcher]

        #x-and-y coordinates
        teams_np = np.array(team_pts_list)
        opps_np = np.array(opp_pts_list)

        plt.bar(teams_np, opps_np) #teams is the x-axis, wins is the y-axis
        plt.xlabel("Team Points (Boston Celtics)")
        plt.ylabel("Opponent Points")

        plt.title("Boston Celtics' Team Points vs Opponent Points")
        
        plt.show()

    def teams_vs_opp_line():
        teams_pts_query_2 = "SELECT (`Points (Tm)`) FROM celtics2425stat"
        mycursor.execute(teams_pts_query_2)
        teams_pts_fetcher_2 = mycursor.fetchall()
        teams_pts_list_2 = [item[0] for item in teams_pts_fetcher_2]

        opps_pts_query_2 = "SELECT (`Opponent Points (Opp)`) FROM celtics2425stat"
        mycursor.execute(opps_pts_query_2)
        opps_pts_fetcher_2 = mycursor.fetchall()
        opps_pts_list_2 = [item[0] for item in opps_pts_fetcher_2]

        teams_np = np.array(teams_pts_list_2) #x-axis
        opps_np = np.array(opps_pts_list_2) #y-axis

        plt.xlabel("Team Points (Boston Celtics)")
        plt.ylabel("Opponent Points")

        plt.plot(teams_np, opps_np, marker='o', linestyle='-', color='green')
        plt.grid(True)
        plt.tight_layout
        plt.title("Boston Celtics' Team Points vs Opponent Points")
        plt.show()

    def season_point_trend():
        game_number_query = "SELECT id FROM celtics2425stat"
        mycursor.execute(game_number_query)
        game_number_fetcher = mycursor.fetchall()
        game_number_list = [item[0] for item in game_number_fetcher]

        teams_pts_query_3 = "SELECT (`Points (Tm)`) FROM celtics2425stat"
        mycursor.execute(teams_pts_query_3)
        teams_pts_fetcher_3 = mycursor.fetchall()
        teams_pts_list_3 = [item[0] for item in teams_pts_fetcher_3]

        opps_pts_query_3 = "SELECT (`Opponent Points (Opp)`) FROM celtics2425stat"
        mycursor.execute(opps_pts_query_3)
        opps_pts_fetcher_3 = mycursor.fetchall()
        opps_pts_list_3 = [item[0] for item in opps_pts_fetcher_3]

        game_number_array = np.array(game_number_list)
        teams_array = np.array(teams_pts_list_3)
        opps_array = np.array(opps_pts_list_3)

        plt.xlabel("Game #")
        plt.ylabel("Celtics Points and Opponent Points")

        teams_y_axis = plt.plot(game_number_array, teams_array, marker = 'o', linestyle= '-', color='green')
        opps_y_axis = plt.plot(game_number_array, opps_array, marker = 'o', linestyle= '-', color='red')

        axis_combo = teams_y_axis + opps_y_axis

        plt.legend(axis_combo, ['Team Points (Celtics)', 'Opponent Points'])

        plt.tight_layout
        plt.grid(True)
        plt.title("Seasonal Point Trend (Game # vs. Celtics/Opponent Team Points)")
        plt.show()

    def win_loss_growth():
        game_number_query_2 = "SELECT id FROM celtics2425stat"
        mycursor.execute(game_number_query_2)
        game_number_fetcher_2 = mycursor.fetchall()
        game_number_list_2 = [item[0] for item in game_number_fetcher_2]

        loss_nba_query_2 = "SELECT (`Losses (L)`) FROM celtics2425stat"
        mycursor.execute(loss_nba_query_2)
        loss_fetcher_2 = mycursor.fetchall()
        loss_list_2 = [item[0] for item in loss_fetcher_2]
        
        wins_nba_query_2 = "SELECT (`Wins (W)`) FROM celtics2425stat"
        mycursor.execute(wins_nba_query_2)
        wins_fetcher_2 = mycursor.fetchall()
        wins_list_2 = [item[0] for item in wins_fetcher_2]

        game_number_array = np.array(game_number_list_2)
        loss_array = np.array(loss_list_2)
        wins_array = np.array(wins_list_2)

        plt.xlabel("Game #")
        plt.ylabel("Wins and Losses")
        plt.title("Boston Celtics Win/Loss Growth per Game Number")

        wins_y_axis = plt.plot(game_number_array, wins_array, marker='o', linestyle='-', color='green')
        loss_y_axis = plt.plot(game_number_array, loss_array, marker='o', linestyle='--', color='red')
        axis_combination = wins_y_axis + loss_y_axis

        plt.legend(axis_combination, ['Wins', 'Losses'])

        plt.grid(True)
        plt.tight_layout
        plt.show()

    Label(new_selection_window, text="Wins vs. Losses", font=('Arial', 23)).pack()
    wins_loss_bar_button = Button(new_selection_window, text="Bar Graph", command=wins_loss_bar, padx=25, pady=25)
    wins_loss_bar_button.pack()

    wins_loss_line_button = Button(new_selection_window, text="Line Graph", command=wins_loss_line, padx=25, pady=25)
    wins_loss_line_button.pack()

    Label(new_selection_window, text="Team Points vs. Opponent Points", font=('Arial', 23)).pack()
    team_opp_points_bar_button = Button(new_selection_window, text="Bar Graph", command=teams_vs_opp_bar, padx=25, pady=25)
    team_opp_points_bar_button.pack()

    team_opp_points_line_button = Button(new_selection_window, text="Scatter Plot", command=teams_vs_opp_line, padx=25, pady=25)
    team_opp_points_line_button.pack()

    Label(new_selection_window, text="Season Point Trend", font=('Arial', 23)).pack()
    season_pts_button = Button(new_selection_window, text='Line Graph', command=season_point_trend, padx=25, pady=25)
    season_pts_button.pack()

    Label(new_selection_window, text="Win/Loss Growth", font=('Arial', 23)).pack()
    win_loss_growth_button = Button(new_selection_window, text='Line Graph', command=win_loss_growth, padx=25, pady=25)
    win_loss_growth_button.pack()
