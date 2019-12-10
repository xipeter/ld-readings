# -*- encoding=utf8
#
#      Filename: dpp.py
#
#        Author: weijieding - weijieding@tencent.com
#   Description: ---
#        Create: 2019-12-09 10:21:42
# Last Modified: 2019-12-09 10:21:42

import logging
import unittest
import math
import itertools

import numpy as np
from scipy.spatial import distance

def jaccard_sim(a, b):
    unions = len(set(a).union(set(b)))
    intersections = len(set(a).intersection(set(b)))
    return 1. * intersections / unions

def dpp(qs, diss, alpha, sigma, k):
  L = np.zeros([qs.shape[0], qs.shape[0]])
  for i in range(qs.shape[0]):
    L[i,i] = qs[i]
  for i in range(qs.shape[0]):
    for j in range(i+1, qs.shape[0]):
      d = diss[i,j]
      L[i,j] = L[j,i] = alpha * qs[i] * qs[j] * math.exp( - d / (2*sigma*sigma) )
  det = np.linalg.det(L)
  print 'alpha[%s] sigma[%s] k[%s] det[%s] L\n%s\n'%(alpha, sigma, k, det, L)
  
  for sub in itertools.combinations(range(qs.shape[0]), k):
    L_sub = np.zeros((k,k))
    for i,i_ori in enumerate(sub):
      for j,j_ori in enumerate(sub):
        L_sub[i,j] = L[i_ori, j_ori]
    det_sub = np.linalg.det(L_sub)
    print sub,det_sub
  print 

 
  
def test():
  qs = np.array([0.1, 0.095, 0.085, 0.075])
  titles = [
    'How do you do'.split(),
    'Hello How old are you'.split(),
    'Hello world'.split(),
    'Today is a good day'.split(','),
  ]
  words = set([ word for title in titles for word in title])
  words = dict(zip(words, range(len(words))))
  print words
  embs = np.zeros([len(titles), len(words)])
  for i,title in enumerate(titles):
    for word in title:
      embs[i, words[word]] += 1
  print embs
  diss = np.zeros([qs.shape[0], qs.shape[0]])
  for i in range(qs.shape[0]):
    for j in range(i+1, qs.shape[0]):
      diss[i,j] = diss[j,i] = distance.jaccard(embs[i], embs[j])
  print diss
  k = 3
  dpp(qs, diss, alpha=10.0, sigma=1, k=3)
  #dpp(qs, diss, alpha=1.5, sigma=1, k=2)
  dpp(qs, diss, alpha=1,   sigma=1, k=3)
  #dpp(qs, diss, alpha=0.5, sigma=1, k=2)
  dpp(qs, diss, alpha=0.01, sigma=1, k=3)


def main():
  import pandas as pd
  pd.set_option("display.width", 1200); pd.set_option("display.unicode.ambiguous_as_wide", True); pd.set_option("display.unicode.east_asian_width", True)
  logging.basicConfig(level=logging.INFO,format="%(asctime)s T%(thread)d %(funcName)s@%(filename)s#%(lineno)d %(levelname)s %(message)s")
  #unittest.main()
  test()


if __name__ == "__main__":
  main()
