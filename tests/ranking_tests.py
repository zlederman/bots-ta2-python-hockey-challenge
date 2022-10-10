import unittest
from src.ranking import rank_teams, parse_row

class RankingTests(unittest.TestCase):
    
    def test_parse_row(self):
        """
            it should consume a tuple of strings and output a list of name,value pairs
        """
        row = ("panthers 1","capitals 2")
        game = parse_row(row)
        self.assertEqual(game.team_one,("panthers",1))
        self.assertEqual(game.team_two,("capitals",2))

    def test_load_ranking(self):
        """
            it should consume a list of tuples creating a list of games
            and a dictionary team_name -> total score
        """
        csv_output = [
            ("panthers 1","capitals 2"),
            ("Dragons 2","The Kraken 2"),
            ("Otters 1","Dragons 2"),
            ("Bulls 1","Sluggers 1"),
            ("Dragons 0","Bulls 3"),
            ("Sluggers 3","The Kraken 2")]
        team_leaderboard = rank_teams(csv_output)
        