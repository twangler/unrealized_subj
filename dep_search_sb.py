#!/usr/bin/env python

"""dep_search_sb.py searches a conll file for SB dependencies"""

__author__      = "Thomas Wangler"

import re


dep_file = open('tuebadz-10.0-conll2006.txt.parsed.conll')
out_file = open('tuebadz_v_greater_sb.conll', 'r+')

sb_pattern = re.compile("\w+\t.+\t.+\tV")
sep_pattern = re.compile("\w")

flag = 0;
curr_sentence = []

c_sb = 0
c_v = 0

for line in dep_file:
  sb_m = sb_pattern.match(line)
  sep_m = sep_pattern.match(line)
  toks = line.split("\t")
  
  
  
  if len(toks) > 1:
    if toks[3] == 'V':
      c_v += 1
    if toks[7] == 'SB':
      c_sb += 1
    
  
  if len(line) > 1:
    curr_sentence.append(line)
  if sb_m:
    flag = 1
  if not sep_m:
    if  c_sb < c_v:
      for element in curr_sentence:
	print 'gotcha'
	out_file.write(element)
      out_file.write('\n')
    curr_sentence = []
    flag = 0
    c_sb = 0
    c_v = 0
    
out_file.close()
