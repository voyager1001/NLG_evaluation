from bleurt import score
checkpoint = "bleurt/test_checkpoint"
refrences=[]
candidates=[]
refrences.append(input('Enter the refrence sentences : '))
candidates.append(input('Enter the candidate sentences : '))
scorer = score.BleurtScorer(checkpoint)
scores = scorer.score(refrences, candidates)
assert type(scores) == list and len(scores) == 1
print(scores)