#file_name: elo.py
#author: Charles Emhardt (cemhardt@bu.edu)

def elo_calculation(team1_elo, team2_elo, k = 20):
    ''' This function runs the basic elo formula and returns the updated elo'''
    team1_R = 10**(team1_elo/400)
    team2_R = 10**(team2_elo/400)

    team1_win_prob = team1_R/(team1_R + team2_R)
    team2_win_prob = team2_R/(team1_R + team2_R)

    team1_elo_new = team1_elo + k * (1 - team1_win_prob)
    team2_elo_new = team2_elo + k * (0 - team2_win_prob)

    return team1_elo_new, team2_elo_new

#def elo_update(team1_elo, team2_elo, k = 32):

    #updated_elo = (elo_calculation(team1_elo, team2_elo, k))

from data import season
from data import BI, ME, AH, SLC, SA, SD, OA, AL

team1_process= []
team2_process = []

for x in season:

    for y in x:
        team1_process = y[1]
        elo1 = team1_process[1]
        team2_process = y[2]
        elo2 = team2_process[1]
        result = elo_calculation(elo1, elo2)
        team1_process[1] = result[0]
        team2_process[1] = result[1]
        


#print(elo_calculation(1300, 1300, 20))
#print(elo_calculation(1300, 1300))

#updated_elo = elo_calculation(team1_elo, team2_elo)

#BI[1] = updated_elo[0]
#ME[1] = updated_elo[1]

print(BI)
print(ME)
print(AH)
print(SLC)
print(SA)
print(AL)
print(SD)
print(OA)

