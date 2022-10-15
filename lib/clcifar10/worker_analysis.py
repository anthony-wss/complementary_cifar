import pandas as pd
from argparse import ArgumentParser
import json
import numpy as np

def main(args):
    df = pd.read_csv(args.csv_file)

    for idx, row in df.iterrows():
        if row['Number of HITs approved or rejected - Lifetime'] - row['Number of HITs approved - Lifetime'] >= 5:
            print(row['Worker ID'], row['Number of HITs approved or rejected - Lifetime'], row['Number of HITs approved - Lifetime'])
    
                    


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--csv_file", type=str, required=True)

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    main(args)