tot=[]
from sr.sacrerouge.metrics import  SIMetrix
def score(a,b):  
  summary = a
  reference = b
  simetrix = SIMetrix()
  a=(simetrix.score([summary],[reference]))
  tot.append(a['smoothedJSD'])
import pandas as pd
train=pd.read_csv('/home/parth/NLG_evaluation/datasets/SICK_train - SICK_train.csv')
ref_list=[]
for i in range(4500):
  if (train['sentence_A'][i]).endswith('.'):
    ref_list.append((train['sentence_A'][i]))
  else :
    ref_list.append((train['sentence_A'][i]+'.'))
hyp_list=[]
for i in range(4500):
  if (train['sentence_B'][i]).endswith('.'):
    hyp_list.append((train['sentence_B'][i]))
  else :
    hyp_list.append((train['sentence_B'][i]+'.'))
for i in range(4500):
  score(ref_list[i],hyp_list[i])
print(tot)
anno=(train['relatedness_score'])
anno=anno/5
import scipy.stats as ap
coeff=ap.pearsonr(tot,anno)
print(coeff)
scoff=ap.spearmanr(tot,anno)
print(scoff)
tot=[]
from sr.sacrerouge.metrics import  SIMetrix
import pandas as pd
train=pd.read_csv('/home/parth/NLG_evaluation/datasets/SICK_test_annotated - SICK_test_annotated.csv')
ref_list=[]
for i in range(4927):
  if (train['sentence_A'][i]).endswith('.'):
    ref_list.append((train['sentence_A'][i]))
  else :
    ref_list.append((train['sentence_A'][i]+'.'))
hyp_list=[]
for i in range(4927):
  if (train['sentence_B'][i]).endswith('.'):
    hyp_list.append((train['sentence_B'][i]))
  else :
    hyp_list.append((train['sentence_B'][i]+'.'))
for i in range(4927):
  score(ref_list[i],hyp_list[i])
anno=(train['relatedness_score'])
anno=anno/5
import scipy.stats as ap
coeff=ap.pearsonr(tot,anno)
print(coeff)
scoff=ap.spearmanr(tot,anno)
print(scoff)