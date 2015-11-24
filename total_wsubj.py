#!/usr/bin/env python


__author__      = "Thomas Wangler"

import re

dep_file = open('tuebadz_rbg_preproc.parsed.conll')
#out_file = open('tuebadz_v_greater_sb.conll', 'r+')

lemma = 'auf#fallen'


sb_pattern = re.compile("\w+\t.+\t.+\tV")
sep_pattern = re.compile("\w")

flag = 0;
curr_sentence = []

dummy = 0

count_overall = 0
count_wsub = 0

for line in dep_file:
  sb_m = sb_pattern.match(line)
  sep_m = sep_pattern.match(line)
  
  
    
  
  if len(line) > 1:
    curr_sentence.append(line)
  if sb_m:
    flag = 1
  if not sep_m:
    for element in curr_sentence:
      toks = element.split("\t")
      if toks[2] == lemma and toks[3] == 'V':
	lemmanum = toks[0]
	count_overall += 1
	#print lemmanum
	for ele in curr_sentence:
	  toks = ele.split('\t')
	  if toks[6] == lemmanum and toks[7] == 'SB':
	    count_wsub += 1
	    break
    
    curr_sentence = []
print 'Lemma: ' + lemma + ', total: ' + str(count_overall) + ', w/ subj-dep: ' + str(count_wsub)
count_overall = 0
count_wsub = 0
      #out_file.write(element)
    #out_file.write('\n')

    
#out_file.close()
