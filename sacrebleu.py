import os
os.system('pip3 install sacrebleu')
import sacrebleu
refs=input('Enter the refrence statements : ').split('.')
hyps=input('Enter the hypothesis statements : ').split('.')
refs=[refs[:-1]]
hyps=hyps[:-1]
bleu = sacrebleu.corpus_bleu(hyps, refs)
print(bleu.score)