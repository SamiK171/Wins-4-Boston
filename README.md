# Wins-4-Boston
Wins 4 Boston is a database-driven application centered around NBA's Boston Celtics. Using a modified 2024-2025 regular season database from Basketball-Reference.com, Wins 4 Boston predicts the team's chances of winning the next season and against other teams through database results, and also presents comparative graphs of database elements.

Starting Notes 📑:
- database_connector.py connects the MySQL Database to the code
- front_screen.py is the main code that runs the application (front-end GUI) [this file should be ran]
- database_analytics is where the database is primarily used (eg. viewing database, if-statements to compare wins/losses, points/opponent points)
- graphing utilizes matplotlib to graph database queries and create comparative graphs 

Steps 🔋:
1) Clone the repository 
2) Set up the Python Environment (install the current version of Python, install the required packages, use a Python-supported IDE)
   - Packages required are imports at the top of the different modules such as...
      - Tkinter
      - Matplotlib
      - NumPy
      - MySQL.connector
      - Also ensure that the .png images provided exist in the folder the .py file is located 
3) Install and Log-In into MySQL (create an account if you have not already)
4) Create a database for the project, and import the .csv file onto MySQL
5) Open the Python scripts, and update the user info in the code that connects to the MySQL server, replacing the
credentials with your own
6) Run the application!
