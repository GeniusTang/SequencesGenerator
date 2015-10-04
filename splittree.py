#!/bin/python

import optparse
import os

parser = optparse.OptionParser()

parser.add_option('-s', action='store', dest='sequences')

parser.add_option('-o', action='store', dest='outdir')

options, reminder = parser.parse_args()

sequences = options.sequences
outdir = options.outdir

f = open(sequences)
lines = f.readlines()
f.close()
specieslist = []

for line in lines[1:]:
    species, sequence = line.split()
    specieslist.append(species)
    f = open(os.path.join(outdir, species), 'wt')
    f.write(sequence)
    f.close()

f = open(os.path.abspath(os.path.join(outdir, 'file')), 'wt')

for spe in specieslist:
    f.write(os.path.abspath(os.path.join(outdir, spe)) + ' ' + spe + '\n')

f.close()


