import os
os.system('pip install skipthoughts')
import torch
tot=[]
from torch.autograd import Variable
import sys
import numpy as np

def process_input(ref_list,cand_list):
  max_score=0
  score_sum=0
  vocab_list=[]

  for i,hyp in enumerate(cand_list[:-1]):
    hyp=hyp.strip()
    for t in hyp.split(' '):
      vocab_list.append(t)
    for j,ref in enumerate(ref_list[:-1]):
      ref=ref.strip()
      i1=[]
      i2=[]
      for t in ref.split(' '):
        vocab_list.append(t)
      vocab_list=list(set(vocab_list))
      for t in hyp.split(' '):
        i1.append(vocab_list.index(t)+1)
      for t in ref.split(' '):
        i2.append(vocab_list.index(t)+1)
      result=get_embeddings(vocab_list,i1,i2)
      cosine=calculate_similarity(result)
      max_score=max(max_score,cosine)
    score_sum += max_score
    max_score=0
  return score_sum

def get_embeddings(vocab_list,i1,i2):
  padd=[0] * abs(len(i1)-len(i2))
  if (len(i1) > len(i2)):
    i2 += padd
  elif len(i2) > len(i1):
    i1 += padd
  sys.path.append('skip-thoughts.torch/pytorch')
  from skipthoughts import BiSkip
  dir_st = 'data/skip-thoughts'
  biskip = BiSkip(dir_st, vocab_list)
  input = Variable(torch.LongTensor([i1,i2]))
  output_seq2seq = biskip(input)
  return output_seq2seq

def calculate_similarity(result):
  output_seq2seq=result.detach().numpy()
  s1 = np.array(output_seq2seq[0]).reshape(2400,1)
  s2 = np.array(output_seq2seq[1]).reshape(2400,1)
  c=0
  for i in range(0,s1.shape[0]):
    c+=s1[i,0]*s2[i,0]
  cosine = c/np.sqrt(np.sum(np.multiply(s1,s1),axis=0)*np.sum(np.multiply(s2,s2),axis=0))
  return cosine

import pandas as pd
train=pd.read_csv('/home2/NLG_evaluation/datasets/paws/paws-train .csv',engine='python',error_bad_lines=False)
ref_list=[]
for i in range(49401):
  if (train['sentence1'][i]).endswith('.'):
    ref_list.append((train['sentence1'][i]))
  else :
    ref_list.append((train['sentence1'][i]+'.'))
hyp_list=[]
for i in range(49401):
  if (train['sentence2'][i]).endswith('.'):
    hyp_list.append((train['sentence2'][i]))
  else :
    hyp_list.append((train['sentence2'][i]+'.'))
for i in range(49401):
  tot.append(process_input(ref_list[i].split('.'),hyp_list[i].split('.')))

print(tot)