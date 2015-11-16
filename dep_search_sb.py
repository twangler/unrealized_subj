#!/usr/bin/env python

"""dep_search_sb.py searches a conll file for SB dependencies"""

__author__      = "Thomas Wangler"

import re


dep_file = open('tuebadz_conll06_sample.conll')

sb_pattern = re.compile("..\t.+\t.+\t.+\t.+\t.+\tSB")
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
    curr_sentence.append(line.split("\t")[1])
  if sb_m:
    flag = 1
  if not sep_m:
    if  c_sb < c_v and flag == 0:
      print curr_sentence
    curr_sentence = []
    flag = 0
    c_sb = 0
    c_v = 0
