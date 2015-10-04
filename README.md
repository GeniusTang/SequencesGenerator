# SequencesGenerator
Generate 8 sequences based on iid model and their evolutionary distances.

In treefile, set branch length of x, y1, y2.

Run as:
python generate.py -i [treefile] -n [sequence length] -o [output prefix]

Output will be:
[outputprefix]seqeunces
[outputprefix]check

For splittree.py, run as:
python splittree.py -s [sequences] -o [output directory]

Output will be:
[output directory]file
[output directory]species


