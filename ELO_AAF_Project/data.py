#file_name: data.py
#author: Charles Emhardt (cemhardt@bu.edu)

BI = ["Birmingham Iron", 1300, 1, "0-0", 1]
ME = ["Memphis Express", 1300, 0, "0-0", 7]
AH = ["Arizona Hotshots", 1300, 1, "0-0", 2]
SLC = ["Salt Lake City Stallions", 1300, 0, "0-0", 5]
SA = ["San Antonio Commanders", 1300, 1, "0-0", 4]
SD = ["San Diego Fleet", 1300, 0, "0-0", 6]
OA = ["Orlando Apollos", 1300, 1, "0-0", 3]
AL = ["Atlanta Legends", 1300, 0, "0-0", 8]

#from elo import elo_calculation

#home team first
# 0 = what week, 1 = home team, 2 = away team, 3 = result of who won
w1_g1 = [1, SA, SD, 0]
w1_g2 = [1, OA, AL, 0]
w1_g3 = [1, BI, ME, 0]
w1_g4 = [1, AH, SLC, 0]
week_1 = [w1_g1, w1_g2, w1_g3, w1_g4]

w2_g1 = [2, BI, SLC, 0]
w2_g2 = [2, ME, AH, 0]
w2_g3 = [2, SA, OA, 0]
w2_g4 = [2, SD, AL, 0]
week_2 = [w2_g1, w2_g2, w2_g3, w2_g4]

w3_g1 = [3, SLC, AH, 0]
w3_g2 = [3, OA, ME, 0]
w3_g3 = [3, BI, AL, 0]
w3_g4 = [3, SD, SA, 0]
week_3 = [w3_g1, w3_g2, w3_g3, w3_g4]


season = [week_1, week_2, week_3]

def week_results(week):

    #pull out each game from the week list
    game1 = week[0]
    game2 = week[1]
    game3 = week[2]
    game4 = week[3]

    #pull out each team from the game list (needed to print out who is playing)
    team1 = game1[1]
    team2 = game1[2]
    team3 = game2[1]
    team4 = game2[2]
    team5 = game3[1]
    team6 = game3[2]
    team7 = game4[1]
    team8 = game4[2]

    #int input statements can only handle one comment, need to space
    print("The game was:", team2[0], "at", team1[0])
    game1_results = int(input("Please input 1 if the home team wins and 2 if the away team wins " ))
    print()
    game1[3] = game1_results

    print("The game was:", team4[0], "at", team3[0])
    game2_results = int(input("Please input 1 if the home team wins and 2 if the away team wins" ))
    print()
    game2[3] = game2_results

    print("The game was:", team6[0], "at", team5[0])
    game3_results = int(input("Please input 1 if the home team wins and 2 if the away team wins" ))
    print()
    game3[3] = game3_results

    print("The game was:", team8[0], "at", team7[0])
    game4_results = int(input("Please input 1 if the home team wins and 2 if the away team wins" ))
    print()
    game4[3] = game4_results

    week1_results = [game1, game2, game3, game4]

    return week1_results


#print(week_results(week_1))

#print(w1_g1)

#week_results(week_1)

#print(w1_g1[3], w1_g2[3], w1_g3[3], w1_g4[3],)

