#file_name: elo.py
#author: Charles Emhardt (cemhardt@bu.edu)

from data import BI, ME

team1_elo = BI[1]
team2_elo = ME[1]

def elo_calculation(team1_elo, team2_elo, k = 32):

    team1_R = 10**(team1_elo/400)
    team2_R = 10**(team2_elo/400)

    team1_win_prob = team1_R/(team1_R + team2_R)
    team2_win_prob = team2_R/(team1_R + team2_R)

    team1_elo_new = team1_elo + k * (1 - team1_win_prob)
    team2_elo_new = team2_elo + k * (0 - team2_win_prob)

    return team1_elo_new, team2_elo_new

#def elo_update(team1_elo, team2_elo, k = 32):

    #updated_elo = (elo_calculation(team1_elo, team2_elo, k))




if __name__ == '__main__':
    print(elo_calculation(1300, 1300, 20))
    print(elo_calculation(1300, 1300))

    updated_elo = elo_calculation(team1_elo, team2_elo)

    BI[1] = updated_elo[0]
    ME[1] = updated_elo[1]

    print(BI)
    print(ME)
