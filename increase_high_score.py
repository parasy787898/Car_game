import shelve
import os

score_file=os.path.join(os.path.dirname(__file__), "data","score")

score=150
try:
    d = shelve.open(score_file)   
    h_score  = d['score']        

except:
    d = shelve.open(score_file)   
    d['score']=150

d['score'] = score