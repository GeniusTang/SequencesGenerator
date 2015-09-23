#!/bin/python

import optparse
import random
import math

#Create a parser to analyze the input argumetns.
parser = optparse.OptionParser()

#File that stores the structure of tree.
parser.add_option('-i', action="store", dest="treefile")
#The length of sequences.
parser.add_option('-n', action="store", dest="length")
#The output file prefix
parser.add_option('-o', action="store", dest="outputprefix", default="./")

options, reminder= parser.parse_args()

treefile =  options.treefile
length = int(options.length)
prefix = options.outputprefix
outfile = prefix + "sequences"
checkfile = prefix  + "check"
 
#Set x, y1, y2 values from treefile
f = open(treefile)
for line in f.readlines():
    exec(line.strip())
f.close()


#Generate a root sequence with certain length
ALPHA = 'ATCG' 
branch = []
branch.append(''.join([random.choice(ALPHA) for i in range(length)]))

#Generate a child sequence based on root sequence and mutation rate.
def mutate(root, rate):
    new = ""
    for letter in root:
        if random.random() < rate:
            new += random.choice(ALPHA.replace(letter, ''))
        else:
            new += letter
    return new
    
for i in range(1, 15):
    if i <= 6:
        rate = 1 - math.exp(-x)
    elif i in [7, 8, 11, 12]:
        rate  = 1 - math.exp(-y1)
    else:
        rate = 1 - math.exp(-y2)

    root = (i - 1) / 2
    rootseq = branch[root]
    newseq = mutate(rootseq, rate)
    branch.append(newseq)

#Check the mutation rate between each sequences.
def check(seq1, seq2):
    return(len([i for i in zip(seq1, seq2) if i[0] != i[1]]))

SPECIES = 'ABCDEFGH'

#Write sequences into outputfile
f = open(outfile, 'wt')
f.write('8   ' + str(length) + '\n')
for i in range(7, 15):
    f.write('%-10s'%SPECIES[i-7] + branch[i] + '\n')
f.close()

#Write check results
f = open(checkfile, 'wt')
difference = [[check(branch[i], branch[j]) for i in range(7, 15)] for j in range(7, 15)]
for spe in difference:
    for i in spe:
        f.write('%-4d'%i)
    f.write('\n')
for spe in difference:
    for i in spe:
        f.write('%-7.3f'%(i/float(length)))
    f.write('\n')
f.close()
