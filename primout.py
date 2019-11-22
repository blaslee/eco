#blas lee and gabriel mihalache 
#script for converting prim text files to .csv output

import os
import glob
import pandas as pd

indir =  "/Users/blas/Documents/Research/Prim"
outfile = "/Users/blas/Documents/Research/primout.csv"
fileList = glob.glob("*.txt")

def concatenate(indir,outfile):
    os.chdir(indir)
    dfList=[]
    #colnames=["ISIN", "ISSUE DATE", "INITIAL INTEREST", "ISSUE DATE", "LAST AMORTIZATION DATE", "SECTION NUMBER", "RETURN NUMBER", "DISIMBURSEMENT DATE", "NOMINAL OF COMPETITIVE PETIITONS", "NOMINAL OF NON-COMPETITIVE PETITIONS", "NOMINAL AWARDED", "NOMINAL ISSUED", "NOMINAL AWARDED TO THE MARGINAL", "MARGINAL PRICE", "MARGINAL TYPE", "HALF PRICE WEIGHTED", "MIDDLE TYPE WEIGHTED", "FIRST PRICE NOT ACCEPTED", "NOMINAL REQUESTED TO THAT PRICE"]
    
for filename in fileList:
        print(filename)
        df=pd.read_csv(filename,header=None, sep=";", skipinitialspace=True, encoding="latin-1")
        mask = [df[col].isnull().sum() < 0.1*len(df) for col in df.columns]
        df = df[df.columns[mask]]
        dfList.append(df)
        concatDf.columns=colnames
        concatDf=pd.concat(dfList,axis=0)  
        concatDf.to_csv(outfile,index=None)

concatenate(indir,outfile)
