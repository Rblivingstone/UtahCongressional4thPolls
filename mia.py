# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:24:35 2018

@author: rbarnes
"""

import matplotlib.pyplot as plt
import scipy.stats as s
import numpy as np
result = 0.5
probs = [0.5]
polls = [0.03,0.04,0.06,0.09,0.02,0.03,0.09,0.00,-0.01,-0.02]
magics = [0.0,0.07373]
for magic in magics:
    probs=[0.5]
    i=0
    for poll in polls:
        i+=1
        #factor = result
        factor = (1-np.exp(-magic*(len(polls)-i)))*0.5+np.exp(-magic*(len(polls)-i))*result
        probs.append((1-s.norm(loc=poll, scale=0.025).cdf(0))*factor/((1-s.norm(loc=poll, scale=0.025).cdf(0))*factor+(s.norm(loc=poll, scale=0.025).cdf(0))*(1-factor)))
        print(result)
        result = (1-s.norm(loc=poll, scale=0.025).cdf(0))*factor/((1-s.norm(loc=poll, scale=0.025).cdf(0))*factor+(s.norm(loc=poll, scale=0.025).cdf(0))*(1-factor))
        
    plt.plot(range(len(probs)),probs,'k')
    plt.fill_between(range(len(probs)),0.5,color='b',alpha=0.5)
    plt.fill_between(range(len(probs)),y1=1.0,y2=0.5,color='r',alpha=0.5)
    plt.hlines(0.5,0,10,linestyle='--',colors='k')
    plt.text(4,0.4,'Ben Wins')
    plt.text(4,0.55,'Mia Wins')
    plt.ylabel('Probability Mia Love Holds Seat')
    plt.xlabel('Survey Number')
    plt.title('Probability that Mia Love Holds Her Seat In Congress')
    plt.show()
    print(result)