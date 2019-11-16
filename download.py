#blas lee and gabriel mihalache
#this code downloads data from the bank of spain website and unzips .txt files into three respective folders

#imports necessary libraries
import zipfile
import requests
import os
import glob

#Variables for files required
primfiles = [f"prim{year}.zip" for year in range (1998,2007)] #primary market data
carvfiles = [f"carv{year}.zip" for year in range (1998,2007)] #characteristics of outstanding securities  
saldfiles = [f"sald{year}.zip" for year in range (1998,2007)] #outstanding and 3rd party balanc
#target url for prim, carv, and sald files
baseurl = "http://www.bde.es/webbde/es/secciones/informes/banota/"

#downloads zipfiles from database
def download(filename,dir=""):
    path = os.path.join(baseurl, filename)
    with requests.get(path,stream=True) as res:
        res.raise_for_status()                                #halts compiling if there is an error
        local_path = os.path.join(dir, filename)
        with open(local_path,'wb') as file:
            for chunk in res.iter_content(chunk_size=4096):
                file.write(chunk)
#unzips the .zip files
def unzip(file, dir=""):
    with zipfile.ZipFile(file, 'r') as zip_ref:
        subdir = os.path.basename(file).split('.')[0]
        path = os.path.join(dir, subdir)
        zip_ref.extractall(path)

#loop for downloading Prim files from 1988 to 2006
for primfile in primfiles:
    download(primfile, "Prim")
    print(primfile)
#loop for downloading Carv files from 1988 to 2006
for carvfile in carvfiles:
    download(carvfile, "Carv")
    print(carvfile)
#loop for downloading Sald files from 1988 to 2006
for saldfile in saldfiles:
    download(saldfile, "Sald")
    print(saldfile)

print("Unzipping...")

#Unzipped files inserted into their respective directories
for dir in ("Prim", "Carv", "Sald"):
    for file in glob.glob(os.path.join(dir, "*.zip")):
        unzip(file, dir)
