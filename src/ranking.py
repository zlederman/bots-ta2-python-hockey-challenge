from typing import Tuple,Dict,List
import re
from dataclasses import dataclass

WINNING_POINTS = 3
LOSING_POINTS = 0
TIE_POINTS = 1
NAME_IDX = 0
SCORE_IDX = 1
@dataclass
class Game:
    team_one: Tuple[str,int]
    team_two: Tuple[str,int]

    def is_tie(self):
        return self.team_one[SCORE_IDX] == self.team_two[SCORE_IDX]
    
    def calc_points(self):
        winner = max(self.team_one,self.team_two,key=lambda tup: tup[SCORE_IDX])
        loser = min(self.team_one,self.team_two,key=lambda tup: tup[SCORE_IDX])
            
        return (winner,loser)
        
def parse_row(row: Tuple[str,str])-> Game:
    """
    
    """    
    team_name_regex = re.compile("[A-Za-z\s]+[A-Za-z]")
    score_regex = re.compile("[0-9]+")
    team_one_raw: str = row[0]
    team_two_raw: str = row[1]

    t1_name = re.search(team_name_regex,team_one_raw).group()
    t1_score = re.search(score_regex,team_one_raw).group()
    t2_name = re.search(team_name_regex,team_two_raw).group()
    t2_score = re.search(score_regex,team_two_raw).group()

    return Game(
        team_one=(t1_name,int(t1_score)),
        team_two=(t2_name,int(t2_score))
    ) 

def rank_teams(game_scores: List[Tuple[str,str]]) -> List[Tuple[str,int]]:
    """
        consumes a list of tuples which are name and score strings parsing the
        name and score out into a list that has the first team and the second team

        Params:
            game_scores: List[Tuple[str,str]] rows from read_csv
        Returns:
            leaderboard: a sorted list of name,score pairs
    """
    team_score_map: Dict[str,int] = {}
    for row in game_scores:
        game: Game = parse_row(row)
        if game.is_tie():
            team_score_map[game.team_one[NAME_IDX]] = 1
            team_score_map[game.team_one[NAME_IDX]] = 1
        else:
            winner,loser = game.calc_points()
            team_score_map[winner] = WINNING_POINTS
            team_score_map[loser] = LOSING_POINTS
     
    return sorted(team_score_map.items(),key=lambda tup: (tup[1],tup[0]))