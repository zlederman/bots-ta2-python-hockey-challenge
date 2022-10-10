import unittest
from src.csv_io import read_csv
class CsvIOTests(unittest.TestCase):
    def test_load_csv(self):
        """
            it should consume a csv from the input folder into a list of tuples (rows)
            only testing the structure of data
        """
        rows = read_csv()
        all_tuples = all([isinstance(row,tuple) for row in rows])
        self.assertTrue(all_tuples)

    def test_dump_hockey(self):
        pass
if __name__ == "__main__":
    unittest.main()