# -*- coding: utf-8 -*-
"""ROUGE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QZZhWBsiHfz3IkuuoBMGN8xJ9DbKLkw0
"""
import os
os.system('pip install rouge')
def rouge_score():
  import rouge
  from rouge import Rouge
  hypothesis=input('Enter the hypothesis sentences : ')
  reference=input('Enter the refrence sentence : ')
  rouge = Rouge()
  scores = rouge.get_scores(hypothesis, reference)
  print(scores)

if __name__=='__main__':
  rouge_score()

