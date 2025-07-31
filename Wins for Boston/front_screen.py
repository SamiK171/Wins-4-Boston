from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from database_connector import get_cursor
from database_connector import get_connection
import database_analytics
import graphing

mydb = get_connection()
mycursor = get_cursor()

root = Tk()
root.title("Wins 4 Boston")

def quit_application():
    mycursor.close()
    mydb.close()
    root.destroy() 

def frontend_display():

    try:
        app_logo = Image.open("wins_4_boston_matching_logo.png")
        resized_logo = app_logo.resize((450, 450))
        tk_logo = ImageTk.PhotoImage(resized_logo)

        logo_label = tk.Label(root, image=tk_logo)
        logo_label.pack()

        iconimg = PhotoImage(file = 'wins_4_Boston_exe_logo.png')
        root.iconphoto(True, iconimg)

    except FileNotFoundError:
        error_label = tk.Label(root, text="Error: Image file not found!")
        error_label.pack()

    #viewing database button
    view_db_button = Button(root, text="View Celtics 2024-2025 Regular Season Database", command=database_analytics.viewing_data, padx=25, pady=25)
    view_db_button.pack()

    #next season button
    next_season_button = Button(root, text="Will the Celtics Win Next Season?", command=database_analytics.win_nextyear, padx=25, pady=25)
    next_season_button.pack()

    #against certain team button
    against_team_button = Button(root, text="Will the Celtics Win Against X Team Next Season?", command = database_analytics.against_team, padx=25, pady=25)
    against_team_button.pack()

    graph_button = Button(root, text="Data Graphs", command=graphing.graph_display, padx=25, pady=25)
    graph_button.pack()

    quit_button = Button(root, text="Quit", command=quit_application, padx=25, pady=25)
    quit_button.pack()

    root.mainloop()

frontend_display()