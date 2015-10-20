#!/bin/bash

cd /home/rcf-40/kujin/panasas/SequencesGenerator
for i in {1..6};do
    for j in {1..100};do
        if [ ! -d /home/rcf-40/kujin/panasas/Examples/T$i/rep$j ];then
            mkdir /home/rcf-40/kujin/panasas/Examples/T$i/rep$j
        fi 
        echo T$i/rep$j
        python ./generateseq.py -i T${i}treefile -n 1500 -o T$i
        python ./splittree.py -s T${i}sequences -o /home/rcf-40/kujin/panasas/Examples/T$i/rep$j 
    done
done
