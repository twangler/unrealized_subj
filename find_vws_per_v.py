#!/usr/bin/env python
#-*- coding: iso-8859-15 -*-


__author__      = "Thomas Wangler"

import re

dep_file = open('tuebadz_rbg_preproc.parsed.conll')
out_file = open('tuebadz_verbstats.conll', 'r+')

lemmalist = ['verwalten', 'trinken', 'verstehen', 'hören', 'werfen', 'singen', 'verlassen']


sb_pattern = re.compile("\w+\t.+\t.+\tV")
sep_pattern = re.compile("\w")


curr_sentence = []
count_overall = 0
count_wsub = 0

for lemma in lemmalist:
  dep_file = open('tuebadz_rbg_preproc.parsed.conll')
  out_file.write('#Sentences w/o subj-dep to lemma (' + lemma + ') :\n') 
  
  
  
  for line in dep_file:
    
    flag = 0
    
    sb_m = sb_pattern.match(line)
    sep_m = sep_pattern.match(line)

    if len(line) > 1:
      curr_sentence.append(line)
    #if sb_m:
      #flag = 1
    if not sep_m:
      for element in curr_sentence:
	toks = element.split("\t")
	if toks[2] == lemma and toks[3] == 'V':
	  lemmanum = toks[0]
	  is_oc = toks[7]
	  count_overall += 1
	
	  for ele in curr_sentence:
	    toks = ele.split('\t')
	    if is_oc == 'OC':
	      count_wsub += 1
	      flag = 1
	      break
	    if toks[6] == lemmanum and toks[7] == 'SB':
	      count_wsub += 1
	      flag = 1
	      break
	    
	  if flag == 0:
	     out_str = ''
	     for i in curr_sentence:
	      out_str += i.split('\t')[1] + ' '
	     out_file.write(out_str + '\n')

      flag == 0
      curr_sentence = []
  print 'Lemma: ' + lemma + ', total: ' + str(count_overall) + ', w/ subj-dep: ' + str(count_wsub)
  out_file.write('\n' + 'Lemma: ' + lemma + ', total: ' + str(count_overall) + ', w/ subj-dep: ' + str(count_wsub) + '\n\n')
  count_overall = 0
  count_wsub = 0

    
out_file.close()
