# Class: CIST 2742 Python Programming I
# Term: Fall 2024
# Instructor: Saima Suleman
# Description: Solution to Lab #6
# Author: Mauricio Arriaga

def main():

    winner_list = []
    with open ("WorldSeriesWinners.txt",'r') as file:
        for line in file:
            winner_list.append(line.strip())

    unique_teams = []
    for team in winner_list:
        if team not in unique_teams:
            unique_teams.append(team)

    print("list of unique teams: from 2003 until 2021")
    for team in unique_teams:
        print(team)

    team_name = input("enter team names: ")
    win_count = 0
    for winner in winner_list:
        if winner in team_name:
            win_count += 1

    if win_count > 0:
        print(f'the team {team_name} the winner is {win_count} times between 1903 to 2021')

if __name__ == '__main__':
   # main()
