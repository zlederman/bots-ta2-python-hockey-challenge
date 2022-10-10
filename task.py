import argparse

from src.ranking import rank_teams
from src.csv_io import read_csv, write_csv

def entrypoint() -> None:
    """Main entry point for the hockey ranker CLI.

    Raises:
        FileNotFoundError: If the input_file argument points to a file that does not exist.
        TypeError: If the input_file argument points to a non-file (eg, a directory).
    """
    parser = argparse.ArgumentParser(
        description="CLI to rank teams from a list of game results"
    )
    parser.add_argument("input_file", help="Location of input CSV")
    parser.add_argument("output_file", help="Location to write output CSV")

    # Parse out the input file
    args = parser.parse_args()

    # Here are your two arguments: the input CSV and the output CSV
    input_file = args.input_file
    output_file = args.output_file

    # TODO: Add your code here
    # (you may modify the line below)
    try:
        csv_data = read_csv(input_file=input_file)
        leader_board = rank_teams(csv_data)
        write_csv(leader_board,output_file)
    except FileNotFoundError as fe:
        print(fe)
        if fe.filename == input_file:
            print(f"input file {input_file} not found")
        else:
            print(f"an error occured while writing to {output_file}")

if __name__ == "__main__":
    entrypoint()
