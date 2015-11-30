#!/bin/sh

for i in {8..9};
do 
    BASE="T${i}_base"
    evolver 5 ${BASE}
    mv mc.paml T${i}_sequences
    mv ancestral.txt T${i}_ancestral.txt
    mv siterates.txt T${i}_siterates.txt
done
    
