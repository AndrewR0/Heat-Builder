import numpy as np
import pandas as pd

def buildDict(excelName: str):
    df = pd.read_excel(excelName, usecols=[0,1])
    dancesByPartner = df.groupby(["Partners"])["Dances"].apply(list).to_dict()
    

if __name__ == "__main__":
    buildDict("2021-10 Program.xlsx")