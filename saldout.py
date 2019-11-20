#blas lee and gabriel mihalache        
#script for converting sald text files to .csv output                                                                 
import os
import glob
import pandas as pd

indir =  "/Users/blas/Documents/Research/Sald"
outfile = "/Users/blas/Documents/Research/saldout.csv"
def concatenate(indir,outfile):
    os.chdir(indir)
    fileList=glob.glob("*.txt")
    dfList=[]
    colnames=["DATE", "ISIN", "ASSET CLASS", "BALANCES IN CIRCULATION", "BALANCE OF THIRD PARTIES"]

    for filename in fileList:
        print(filename)
        df=pd.read_csv(filename,header=None, sep=";", skipinitialspace=True, encoding="latin-1")
        #mask = [df[col].isnull().sum() < 0.1*len(df) for col in df.columns]
        #df = df[df.columns[mask]]
        dfList.append(df)
    concatDf=pd.concat(dfList,axis=0)
    concatDf.columns=colnames                                                                                       
    concatDf.to_csv(outfile,index=None)

concatenate(indir,outfile)
