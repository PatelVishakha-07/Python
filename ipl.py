""" (a)  Write a Python function load_ipl_data(filename) using pandas that: reads the CSV, drops rows where winner is NaN (abandoned matches), converts team1_score and team2_score to integers handling any non-numeric values by setting them to 0, and returns the cleaned DataFrame. Print the shape before and after cleaning 

Write a function season_report(df) that computes and prints: (i) the team with most wins in the season, (ii) the player who won Player of the Match most times, (iii) the highest-scoring match (maximum of team1_score + team2_score) with venue and teams, (iv) win percentage for each team (wins / total matches played × 100), sorted descending.

Write a function plot_and_export(df, output_path) that: creates a bar chart of wins per team using matplotlib (with proper title, x-label, y-label, and team colors if possible), saves it as ipl_2026_wins.png, and exports the season_report as a formatted ipl_2026_report.txt file with today's date in the header. Handle all file I/O exceptions
"""

import pandas as pd
import matplotlib.pyplot as plt
import math

def plot_and_export(df, output_path):
    wins = df["winner"].value_counts()
    
    plt.xlabel("Team Name")
    plt.ylabel("No of Wins")
    plt.title("Wins Per Team")

    colors = {
        "Mumbai Indians": "blue",
        "Chennai Super Kings": "yellow",
        "Royal Challengers Bengaluru": "red",
        "Kolkata Knight Riders": "purple",
        "Delhi Capitals": "dodgerblue",
        "Punjab Kings": "crimson",
        "Rajasthan Royals": "pink",
        "Sunrisers Hyderabad": "orange",
        "Lucknow Super Giants": "cyan",
        "Gujarat Titans": "navy"
    }

    bar_colors = [colors.get(team, "gray") for team in wins.index]
    wins.plot(kind="bar", color=bar_colors)
    
    plt.show()


def season_report(df):
    most_wins = df.groupby(["season", "winner"]).size().sort_values(ascending=False)
    max_win = most_wins.max()
    print(most_wins[most_wins == max_win])

    mom = df.groupby("player_of_match").size()
    print(mom[mom == mom.max()])

    df["total_score"] = df["team1_score"] + df["team2_score"]
    highest_score = df[df["total_score"] == df["total_score"].max()]
    print(highest_score[["team1", "team2", "venue", "total_score"]])

    matches_played = pd.concat([df["team1"], df["team2"]]).value_counts()
    wins = df["winner"].value_counts()
    win_percenatge = (wins / matches_played).fillna(0) * 100
    win_percenatge = win_percenatge.sort_values(ascending = False)
    print(win_percenatge)

def load_ipl_data(filename):
    df = pd.read_csv(filename)

    print("Shape before cleaning: ", df.shape)
    df.dropna(subset="winner", inplace=True)

    df["team1_score"] = pd.to_numeric(df["team1_score"], errors='coerce').fillna(0).astype(int)

    df["team2_score"] = pd.to_numeric(df["team2_score"]).fillna(0).astype(int)
   
    print("Shape After cleaning: ", df.shape)
    # print(df)    
    # season_report(df)
    plot_and_export(df, "abc")

load_ipl_data("file_ipl_2026.csv")
