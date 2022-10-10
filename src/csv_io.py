import csv
from typing import List,Tuple,Dict

def read_csv(input_file) -> List[Tuple]:
    """
        read_csv takes a path and reads a game csv into a list of tuples
        
        Params:
            input_path: str the input file
        Returns:
            rows: A list of dictionaries ready to be interpreted
    """
    fieldnames = ['Team 1 Score', 'Team 2 Score']
    data: List = None
    with open(input_file,'r') as f:
        reader = csv.DictReader(f,fieldnames=fieldnames)
        next(reader)
        return [tuple(row.values()) for row in reader]
    
def write_csv(leader_board: List[Tuple[str,int]],output_file):
    """
        write_csv takes a filename and a leaderboard and writes it to a csv 
        of format place,team and score
        
        Params:
            leader_board: List[Tuple[str,int]]
            output_file: str filename to write to
        Returns:
            rows: A list of dictionaries ready to be interpreted
    """
    fieldnames = ["Place","Team","Score"]
    with open(output_file,'w') as f:
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        for place,team_score in enumerate(leader_board):
            writer.writerow({"Place":place + 1,"Team":team_score[0],"Score":team_score[1]})