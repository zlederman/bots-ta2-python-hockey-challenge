from tempfile import tempdir
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
    """
        intermediary class for storing and determing outcomes of a game
    """
    team_one: Tuple[str,int]
    team_two: Tuple[str,int]

    def is_tie(self):
        return self.team_one[SCORE_IDX] == self.team_two[SCORE_IDX]
    
    def calc_points(self):
        """
            returns the largest score first then the smallest of the two items
        """
        winner = max(self.team_one,self.team_two,key=lambda tup: tup[SCORE_IDX])
        loser = min(self.team_one,self.team_two,key=lambda tup: tup[SCORE_IDX])
            
        return (winner[NAME_IDX],loser[NAME_IDX])
        
def parse_row(row: Tuple[str,str])-> Game:
    """
        extracts the team name and the score into a tuple 
        then takes both teams and moves them into a game object
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

def insert_or_add(k:str,v:int,leader_board: Dict) -> Dict:
    if k in leader_board:
        leader_board[k] += v
    else:
        leader_board[k] = v
    return leader_board

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
            team_score_map = insert_or_add(game.team_one[NAME_IDX],TIE_POINTS,team_score_map)
            team_score_map = insert_or_add(game.team_two[NAME_IDX],TIE_POINTS,team_score_map)
        else:
            winner,loser = game.calc_points()
            team_score_map = insert_or_add(winner,WINNING_POINTS,team_score_map)
            team_score_map = insert_or_add(loser,LOSING_POINTS,team_score_map)

    return sorted(team_score_map.items(),key=lambda tup: (-tup[1],tup[0]))