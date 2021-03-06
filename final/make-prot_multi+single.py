#!/usr/bin/python
import os
import sys

filename_fa = sys.argv[1]

seq_list = dict()
seq_h = ''
f_seq = open(filename_fa,'r')
for line in f_seq:
    if( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append( line.strip() )
f_seq.close()

seq_map = dict()
for tmp_h in seq_list.keys():
    tmp_seq = ''.join(seq_list[tmp_h])
    if( not seq_map.has_key(tmp_seq) ):
        seq_map[tmp_seq] = []
    seq_map[tmp_seq].append( tmp_h )

count_single = 0 
count_multi = 0
filename_base = filename_fa.replace('.fa','')
filename_base = filename_base.replace('.sorted_fa','')

exc_list = dict()
f_nr = open('%s.NR_fa'%filename_base,'w')
f_single = open('%s.single_fa'%filename_base,'w')
f_multi = open('%s.multi_fa'%filename_base,'w')
f_nr_log = open('%s.NR_log'%filename_base,'w')
for tmp_seq in seq_map.keys():
    tmp_h_list = seq_map[tmp_seq]
    
    if( exc_list.has_key(tmp_seq) ):
        continue

    tmp_h = tmp_h_list[0]
    f_nr.write('>%s\n%s\n'%(tmp_h,tmp_seq))
    if( len(tmp_h_list) > 1 ):
        f_nr_log.write('%s\t%s\n'%(tmp_h,';;'.join(tmp_h_list)))
        f_multi.write('>%s\n%s\n'%(tmp_h,tmp_seq))
        count_multi += 1
    else:
        f_single.write('>%s\n%s\n'%(tmp_h,tmp_seq))
        count_single += 1
f_nr_log.write('#total seq: %d\n'%len(seq_list))
f_nr_log.write('#total nr seq: %d\n'%len(seq_map))
f_nr_log.write('#single seq: %d, multi seq:%d\n'%(count_single, count_multi))
f_nr_log.close()
f_nr.close()

f_single.close()
f_multi.close()
