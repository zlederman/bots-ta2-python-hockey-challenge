import csv
from typing import List,Tuple,Dict

def read_csv(input_path="input/league-sample-games.csv") -> List[Tuple]:
    """
        read csv takes a path and reads a game csv into a list of tuples
        
        Params:
            input_path: the path to the input file
        Returns:
            rows: A list of dictionaries ready to be interpreted
    """
    fieldnames = ['Team 1 Score', 'Team 2 Score']
    reader: csv.DictReader
    with open(input_path) as f:
        reader = csv.DictReader(f,fieldnames=fieldnames)
    return [tuple(row) for row in reader]
    