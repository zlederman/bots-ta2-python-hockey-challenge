import unittest
from src.csv_io import read_csv, write_csv
class CsvIOTests(unittest.TestCase):
    def test_load_csv(self):
        """
            it should consume a csv from the input folder into a list of tuples (rows)
            only testing the structure of data
        """
        rows = read_csv("input/league-sample-games.csv")
        all_tuples = all([isinstance(row,tuple) for row in rows])
        self.assertTrue(all_tuples)

    def test_dump_hockey(self):
        """
            it should consume a list of tuples and then write it to a csv
        """
        leader_board = [("bobcats",3),("tomcats",2),("elephants",1)]
        write_csv(leader_board,"output/test_output.csv")
if __name__ == "__main__":
    unittest.main()