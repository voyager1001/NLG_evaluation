import os
os.system('pip install nltk')
from nltk.translate.gleu_score import corpus_gleu
ref_final = []
hyp_final = []
ref_list = input('Enter the list of refrences : ').split('.')
hyp_list = input('Enter the list of hypothesis : ').split('.')
for r in ref_list[:-1]:
    ref_final.append(r.split(' '))
for h in hyp_list[:-1]:
    hyp_final.append(h.split(' '))
print(corpus_gleu(ref_final,hyp_final))