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


w1_g1 = [1, SA, SD, 0]
w1_g2 = [1, OA, AL, 0]
w1_g3 = [1, BI, ME, 0]
w1_g4 = [1, AL, SLC, 0]
week_1 = [w1_g1, w1_g2, w1_g3, w1_g4]

def week_results(week):

    game1 = week[0]
    game2 = week[1]
    game3 = week[2]
    game4 = week[3]

    team1 = game1[1]
    team2 = game1[2]
    team3 = game2[1]
    team4 = game2[2]
    team5 = game3[1]
    team6 = game3[2]
    team7 = game4[1]
    team8 = game4[2]

    print("The game was: ", team2[0], "at", team1[0])
    game1_results = int(input("Please input 1 if the home team wins and 2 if the away team wins" ))
    print()
    game1[3] = game1_results

    print("The game was: ", team4[0], "at", team3[0])
    game2_results = int(input("Please input 1 if the home team wins and 2 if the away team wins" ))
    print()
    game2[3] = game2_results

    print("The game was: ", team6[0], "at", team5[0])
    game3_results = int(input("Please input 1 if the home team wins and 2 if the away team wins" ))
    print()
    game3[3] = game3_results

    print("The game was: ", team8[0], "at", team7[0])
    game4_results = int(input("Please input 1 if the home team wins and 2 if the away team wins" ))
    print()
    game4[3] = game4_results

    week1_results = [game1, game2, game3, game4]

    return week1_results

print(week_results(week_1))

print(w1_g1)

