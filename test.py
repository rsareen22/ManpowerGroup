import os,json
from datetime import datetime,date
from matplotlib import pyplot as pl
import matplotlib.dates as mdates
import numpy as np
import csv

reload = False
if reload:
    loc = './data/json/validated'
    A = []
    for i in os.listdir(loc):
        if not i.endswith('.json'):
            continue
        with open(loc+f'/{i}') as f:
            A.append(json.load(f))
    with open('./data/json/merged.json','w') as f:
        json.dump(A, f, indent=1)
else:
    with open('./data/json/merged.json') as f:
        A = json.load(f)
    
days,months,year = 0,0,0
con1 = lambda x: all(i in x['timeline']['incident'] for i in ['year'])
con2 = lambda x: 'sub_source' not in x['plus']

def time(ind):
    timeline = ind['timeline']['incident']
    day = timeline['day']
    date_of = date(timeline['year'],6,1)
    return date_of.toordinal()

hacking,malware,social,error,misuse,physical,environmental,unknown = [],[],[],[],[],[],[],[]
for i in filter(lambda x: con1(x) and con2(x),A):
    try:
        if 'hacking' in i['action']:
            hacking.append(time(i))
        elif 'malware' in i['action']:
            malware.append(time(i))
        elif 'social' in i['action']:
            social.append(time(i))
        elif 'error' in i['action']:
            error.append(time(i))
        elif 'misuse' in i['action']:
            misuse.append(time(i))
        elif 'physical' in i['action']:
            physical.append(time(i))
        elif 'environmental' in i['action']:
            environmental.append(time(i))
        elif 'unknown' in i['action']:
            unknown.append(time(i))
    except:
        pass

def check(arg):
    return arg[0],arg[1]

axis = [733000,738000,0,300]

all_of = np.unique(np.concatenate((hacking,malware,social,error,misuse,physical,environmental,unknown)),return_counts=True)
    
pl.figure()
pl.axis(axis)
pl.plot(*check(np.unique(hacking,return_counts=True)),'.')
pl.figure()
pl.axis(axis)
pl.plot(*np.unique(malware,return_counts=True),'.')
pl.figure()
pl.axis(axis)
pl.plot(*np.unique(social,return_counts=True),'.')
pl.figure()
pl.axis(axis)
pl.plot(*np.unique(error,return_counts=True),'.')
pl.figure()
pl.axis(axis)
pl.plot(*np.unique(misuse,return_counts=True),'.')
pl.figure()
pl.axis(axis)
pl.plot(*np.unique(physical,return_counts=True),'.')
pl.figure()
pl.axis(axis)
pl.plot(*np.unique(environmental,return_counts=True),'.')
pl.figure()
pl.axis(axis)
pl.plot(*np.unique(unknown,return_counts=True),'.')
