import csv
import collections
import argparse

parser = argparse.ArgumentParser(description='Restructure MOOC CSV.')
parser.add_argument('input_csv', type=open)
args = parser.parse_args()

data_in = {}
with args.input_csv as csvin:
    reader = csv.reader(csvin)
    next(reader)  # skip titles
    for cid, author_id, parent_cid, step, txt, *x in reader:
        data_in[cid] = (author_id, parent_cid.strip(), txt)

data_out = {}
for source_author_id, parent_cid, txt in data_in.values():
    if len(parent_cid) > 0:
        k = (source_author_id, data_in[parent_cid][0])
        try:
            v = data_out[k]
            v[0] += 1
            v[1] += txt
        except KeyError:
            data_out[k] = [1, txt]

with open('output.csv', 'w') as csvout:
    writer = csv.writer(csvout)
    writer.writerow(['source', 'target', 'weight', 'comments'])
    writer.writerows(list(k) + v for k, v in data_out.items())
