import pandas as pd
from argparse import ArgumentParser
import json
import numpy as np

def main(args):
    df = pd.read_csv(args.csv_file)

    rejected_sub = []
    for idx, row in df.iterrows():
        if row['AssignmentStatus'] == "Rejected":
            rejected_sub.append(idx)
    df = df.drop(rejected_sub, axis=0)
    df = df.reindex()

    invalid_submission = []
    approve_cnt = 0
    for idx, row in df.iterrows():
        if row['AssignmentStatus'] == "Submitted":
            obj = json.loads(row['Answer.taskAnswers'][1:-1])
            cnt = 0
            for i in range(10):
                found = False
                for key, item in obj[f'image_{i+1}'].items():
                    if item:
                        found = True
                if not found:
                    cnt += 1
            if cnt > 0:
                df.loc[idx, "Reject"] = f"Sorry that you have {cnt} unanswer problem(s)."
                invalid_submission.append(f"{row['HITId']} {row['WorkerId']} {cnt}")
            else:
                df.loc[idx, "Approve"] = "x"
                approve_cnt += 1
    
    for s in invalid_submission:
        print(s)
    print("Total approve:", approve_cnt)
    print("Total reject:", len(invalid_submission))

    df.to_csv("Reject_" + args.csv_file.split("_")[1] + ".csv", index=False)
                    


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--csv_file", type=str, required=True)

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    main(args)