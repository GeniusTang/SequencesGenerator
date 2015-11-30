#!/bin/python

import optparse
import os

parser = optparse.OptionParser()

parser.add_option('-o', action='store', dest='outdir')
parser.add_option('-t', action='store', dest='treename')

options, reminder = parser.parse_args()

outdir = options.outdir
treename = options.treename


f = open(treename + '_sequences')
lines = f.readlines()
f.close()


for i in range(1, 101):
    filehandle = open(os.path.join(outdir, 'rep' + str(i), "file"), 'wt')
    for j in range(4, 12):
        line = lines[(i-1)*14 + j].split()
        filename = line[0]
        filehandle.write(os.path.abspath(os.path.join(outdir, 'rep' + str(i),  filename)) + ' ' + filename + '\n')
        f = open(os.path.join(outdir, 'rep' + str(i), filename), 'wt')
        f.write(''.join(line[1:]))
        f.close() 
    print os.path.join(outdir, 'rep' + str(i), "file")
    filehandle.close()
