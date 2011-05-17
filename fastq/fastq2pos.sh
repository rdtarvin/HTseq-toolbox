#!/bin/bash
for FASTQ in $(ls *.called.fastq)
do
  echo $FASTQ
  ~/git/HTseq-toolbox/fastq/fastq2pos.py $FASTQ
done

for FASTQz in $(ls *called.fastq.gz)
do
  echo $FASTQz
  ~/git/HTseq-toolbox/fastq/fastq2pos.py $FASTQz
done
