# AUTOSUMM, MEGOG AND NPOWER
import os
def install_maven():
    os.system('sudo apt update')
    os.system('sudo apt install maven')

def setup_metric():
    os.system('pip install sacrerouge')
    os.system('sacrerouge setup-metric autosummeng')

def get_score():
    from sr.sacrerouge.metrics import  AutoSummENG
    summary = input('Enter the test summary : ')
    reference = input('Enter the refrence sentences : ')
    autosummeng = AutoSummENG()
    print(autosummeng.score(summary, [reference]))

if __name__=='__main__':
    install_maven()
    setup_metric()
    get_score


