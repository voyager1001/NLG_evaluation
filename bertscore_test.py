import os
os.system('pip install bert-embedding')
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from bert_embedding import BertEmbedding
bert_embedding = BertEmbedding(model='bert_24_1024_16', dataset_name='book_corpus_wiki_en_cased')
def get_embedding_matrix(ref_sent,cand_sent):
  ref_array=np.ones((len(ref_sent),1024))
  cand_array=np.ones((len(cand_sent),1024))
  for index,ref in enumerate(ref_sent):
    b=np.array(ref[1])
    if b.shape[0] != 1:
      b=(np.sum(np.array(ref[1]),axis=0))/(np.array(ref[1])).shape[0]
    ref_array[index,:]=np.array(b)
  for index,cand in enumerate(cand_sent):
    b=np.array(cand[1])
    if b.shape[0] != 1:
      b=(np.sum(np.array(cand[1]),axis=0))/(np.array(cand[1])).shape[0]
    cand_array[index,:]=np.array(b)
  return ref_array,cand_array
def get_weights(l):
  resp = 'q'
  if (resp=='q'):
    weights=np.ones((1,l))
    return weights
  else :
    weights=(list(map(float,resp.split(' '))))
    assert len(weights)==l , "Please enter the required number of weights"
    return np.array(weights)
def cos_similarity(ref_array,cand_array):
  result=cosine_similarity(cand_array,Y=ref_array)
  return result
def fscore(ref_array,cand_array):
  res_array = np.zeros((ref_array.dot(cand_array.transpose()).shape))
  for i in range(0,ref_array.shape[0]):
    for j in range(0,cand_array.shape[0]):
      res_array[i][j] = cos_similarity(ref_array[i,:].reshape(1,1024),cand_array[j,:].reshape(1,1024))
  pres = np.sum(np.max(res_array, axis = 0)) / (np.linalg.norm(cand_array)) 
  re = np.sum(np.max(res_array,axis = 1)) / (np.linalg.norm(ref_array))
  f_score = ( 2 * pres * re)/(pres+ re)
  return f_score 
def final_score(result,weights):
  final_score=np.sum(np.multiply(result,weights))/(np.sum(weights))
  return final_score
def bertt(a,b):
  ref_sent_list = list(a.split('.'))[:-1]
  cand_sent_list = list(b.split('.'))[:-1]
  dem1 = ''
  if len(ref_sent_list) > 1 :
    for alpha in ref_sent_list:
      dem1 = dem1 +','+ alpha
    ref_sent_list = [dem1]
  if len(cand_sent_list) > 1 :
    dem2 = ''
    for alpha in cand_sent_list:
      dem2 = dem2 +','+ (alpha)
    cand_sent_list = [dem2]
  assert len(ref_sent_list)==len(cand_sent_list) , "Number of refrence and candidate sentences should be equal"
  for i in range(0,len(ref_sent_list)):
    ref_sent=((ref_sent_list[i]).strip()).split(' ')
    cand_sent=((cand_sent_list[i]).strip()).split(' ')
    # GETTING THE EMBEDDINGS IN A MATRIX
    ref_array,cand_array = get_embedding_matrix(bert_embedding(ref_sent),bert_embedding(cand_sent)) 
    # GETTING THE PAIR-WISE COSINE SIMILARITY
    result = cos_similarity(ref_array,cand_array)
    # APPLY MAX-POOLING ON THE RESULT
    result=(np.max(result,axis=1))
    # TAKING WEIGHTS INPUT
    weights=get_weights(len(cand_sent))  
    #CALCULATING FINAL SCORE
    cos_score = final_score(result,weights)
    f_score = fscore(ref_array,cand_array)
    return f_score,cos_score
  tot = []
cos = []
import pandas as pd
train=pd.read_csv('/datasets/paws/paws-train .csv',engine='python')
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
  val = (bertt(ref_list[i],hyp_list[i]))
  tot.append(val[0])
  cos.append(val[1])
print(tot)
print(cos)