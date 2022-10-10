import csv
from typing import List,Tuple,Dict

def read_csv(input_path="input/league-sample-games.csv") -> List[Dict]:
    fieldnames = ['Team 1 Score', 'Team 2 Score']
    with open(input_path) as f:
        csv = csv.DictReader()