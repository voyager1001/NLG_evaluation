tot=[]
def scoress(a,b):
    from bleurt import score
    checkpoint = "bleurt/test_checkpoint"
    refrences=[b]
    candidates=[a]
    scorer = score.BleurtScorer(checkpoint)
    scores = scorer.score(refrences, candidates)
    assert type(scores) == list and len(scores) == 1
    tot.append(scores)

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
  scoress(ref_list[i],hyp_list[i])
anno=(train['relatedness_score'])
anno=anno/5
f=open('results_test.txt','w')
f.write(tot)
f.write('   ')
f.write(anno)
f.close()
import scipy.stats as ap
coeff=ap.pearsonr(tot,anno)
print(coeff)
scoff=ap.spearmanr(tot,anno)
print(scoff)