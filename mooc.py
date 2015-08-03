import csv

import argparse

parser = argparse.ArgumentParser(description='Restructure MOOC CSV.')
parser.add_argument('input_csv', type=open)
args = parser.parse_args()

data_in = {}
with args.input_csv as csvin:
    reader = csv.reader(csvin)
    next(reader)  # skip titles
    for cid, author_id, parent_cid in reader:
        data_in[cid] = (author_id, parent_cid.strip())

with open('output.csv', 'w') as csvout:
    writer = csv.writer(csvout)
    for source_author_id, parent_cid in data_in.values():
        if len(parent_cid) > 0:
            writer.writerow([source_author_id, data_in[parent_cid][0]])
