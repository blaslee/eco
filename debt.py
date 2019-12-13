import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from_saldout = pd.read_csv('saldout.csv', skiprows=0, usecols=['BALANCES IN CIRCULATION'
                                                               ,'BALANCE OF THIRD PARTIES', 
                                                               'DATE', 'ASSET CLASS'])
saldout_matrix = from_saldout.as_matrix()

circulation = saldout_matrix[:,2]
third_party = saldout_matrix[:,3]

debt = (circulation - third_party)

asset_class = saldout_matrix[:,1]

date, year = [], []
for i in range(len(circulation)):
    if len(str(saldout_matrix[i,0]).split('/')) < 3:
        continue
    else:
        _,month,year1 = str(saldout_matrix[i,0]).split('/')
        date.append(year1 + month)
        year.append(year1)

debt2 = [x for x in debt if str(x) != 'nan']
debt1, date1, year1 = [], [], []
for i in range(len(debt2)):
    if asset_class[i] == 'LET' or asset_class[i] == "BON":
        if debt2[i] != 0 and int(year[i]) < 1997:
            debt1.append(debt2[i])
            date1.append(float(date[i]))
            year1.append(float(year[i]))



data_fitfunc = np.poly1d(np.polyfit(date1,debt1,1))

plt.plot(date1, data_fitfunc(date1))
plt.title("Debt Over Time")
plt.xlabel('Time (years)')
plt.ylabel('Debt')
plt.savefig('Debt.png')


j1988 = []
n = 0
data = []
for i in range(len(date1)):
    if year1[i] == 1988:
        j1988.append(debt1[i])
        n = n+1
data.append([1988, np.mean(j1988)])

j1989 = []
n = 0
for i in range(len(date1)):
    if year1[i] == 1989:
        j1989.append(debt1[i])
        n = n+1
data.append([1989, np.mean(j1989)])

j1990 = []
n = 0
for i in range(len(date1)):
    if year1[i] == 1990:
        j1990.append(debt1[i])
        n = n+1
data.append([1990, np.mean(j1990)])

j1991 = []
n = 0
for i in range(len(date1)):
    if year1[i] == 1991:
        j1991.append(debt1[i])
        n = n+1
data.append([1991, np.mean(j1991)])
        
j1992 = []
n = 0
for i in range(len(date1)):
    if year1[i] == 1992:
        j1992.append(debt1[i])
        n = n+1
data.append([1992, np.mean(j1992)])

j1993 = []
n = 0
for i in range(len(date1)):
    if year1[i] == 1993:
        j1993.append(debt1[i])
        n = n+1
data.append([1993, np.mean(j1993)])

j1994 = []
for i in range(len(date1)):
    if year1[i] == 1994:
        j1994.append(debt1[i])
data.append([1994, np.mean(j1994)])

j1995 = []
for i in range(len(date1)):
    if year1[i] == 1995:
        j1995.append(debt1[i])
data.append([1995, np.mean(j1995)])

j1996 = []
for i in range(len(date1)):
    if year1[i] == 1996:
        j1996.append(debt1[i])
data.append([1996, np.mean(j1996)])

DM_num, DM_dom = 0,0
for i in range(len(data)):
    DM_num = DM_num + (i+1)*data[i][1]*(1/1.03)**i
    DM_dom = DM_dom + data[i][1]*(1/1.03)**i

#DM_num/DM_dom

end_all = []
for i in range(len(data)):
    end_all.append([data[i][0], (i+1)*data[i][1]*(1/1.03)**i / data[i][1]*(1/1.03)**i])

#end_all.append

endall = pd.DataFrame(end_all)
endall.columns = ['Year', 'MD']
endall.to_csv('MD.csv', sep = ',')

avgdata = pd.DataFrame(data)
avgdata.columns = ['Year', 'Average Debt']
avgdata.to_csv('Average_debt.csv', sep = ',')


