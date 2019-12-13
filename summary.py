#blas lee and gabriel mihalache
#This file moves important columns from other output files and consilidates them into one csv file. 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from_carvout = pd.read_csv('carvout.csv', skiprows=0, usecols=['0','9'])
from_primout = pd.read_csv('primout.csv', skiprows=0, usecols=['ISIN', 'ISSUE DATE', 
                                                               'LAST AMORTIZATION DATE', 'MARGINAL PRICE'])
carvout_matrix = from_carvout.as_matrix()
primout_matrix = from_primout.as_matrix()

isbn_c = carvout_matrix[:,0]
isbn_p = primout_matrix[:,0]

paid_coupon = carvout_matrix[:,1]
paid_principal = primout_matrix[:,3]

start_month = []
end_month = []

for i in range(540):
    _,month,_ = primout_matrix[i,1].split('/')
    _,month1,_ = primout_matrix[i,2].split('/')
    start_month.append(month)
    end_month.append(month1)

output = []

for i in range(len(isbn_c)):
    for j in range(len(isbn_p)):
        if isbn_c[i] == isbn_p[j]:
            output.append([isbn_c[i], start_month[j], end_month[j], paid_coupon[i],
                           paid_principal[j]])


total = pd.DataFrame(output)
total.columns=['ISIN' , 'Start Month', 'End Month', 'Paid Coupon', 'Paid Principal']
total.to_csv('sum.csv', sep=',')
