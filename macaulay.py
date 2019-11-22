#blas lee and gabriel mihalache
#computing macaulay duration

import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def mac_duration(cash_flows, discount_rate):
#Macaulay duration of an asset involving of regular cash flows such as a bond

    if not isinstance(cash_flows,pd.DataFrame):
        cash_flows = pd.DataFrame(cash_flows)
        cash_flows.columns = [0]
    
    times = cash_flows.index
    
    # present value of single cash flows (discounted cash flows)
    discount_cf = discount( times, discount_rate ) * cash_flows
        
    # weights: the present value of the entire payment, i.e., discount_cf.sum() is equal to the principal 
    weights = (discount_cf / discount_cf.sum()).values
    
    # cannot make weights*cf.index as weights a dataframe while times is a series
    return np.sum( [w*t for w,t in zip(weights,times)] )
