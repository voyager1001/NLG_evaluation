import os
os.system('sudo apt install default-jre')
os.system('sudo apt install maven')
os.system('sacrerouge setup-metric simetrix')
from sr.sacrerouge.metrics import  SIMetrix
summary = input('Enter the test summary : ')
reference = input('Enter the refrence sentences : ')
simetrix = SIMetrix()
print(simetrix.score([summary],[reference]))