#!/bin/sh

TPATH="/home/rcf-40/kujin/panasas/Examples/evolver/"

TNAME=(8 9)

for i in ${TNAME[@]}; do 
    if [ ! -d ${TPATH}T${i} ]; then
        mkdir ${TPATH}T${i}
    fi
    for j in {1..100}; do
    if [ ! -d ${TPATH}T${i}/rep${j} ]; then
        mkdir ${TPATH}T${i}/rep${j}
    fi
    done
    python splitseq.py -o ${TPATH}T${i} -t T${i}
done
