# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 13:29:49 2016

@author: Stew
"""

import random
import numpy as np

def payoff(strike, spot_T):
    if spot_T >= strike:
        return 1.0
    else:
        return 0.0

def gbm(S, v, r, T, z):
    z = np.random.normal(size=simulations)
    return S * exp((r - 0.5 * v**2) * T + v * sqrt(T) * z

#Here is where I can use oop

# parameters
#main()

S = 40.0 # asset price
v = 0.2 # vol of 20%
r = 0.01 # rate of 1%
maturity = 0.5 # 6 months
strike = 40.0 # ATM strike
simulations = 50000
payoffs = 0.0

    # run simultaion
for i in range(simulations):
    spot_T = gbm(S, v, r, maturity)
    payoffs += payoff(strike, spot_T)

        # find prices
option_price = exp(-r * maturity) * (payoffs / float(simulations))

print 'Price: %.4f' % option_price