import random
import numpy as np
import pandas as pd

def buildDatabases(excelName: str) -> list:
    df = pd.read_excel(excelName, usecols=[0,1])
    
    #create dictionary of the partners with their assigned dances
    dancesByPartner = df.groupby(["Partners"])["Dances"].apply(list).to_dict()
    
    #create dictionary of the dances in a random order
    allDances = df["Dances"].unique().tolist()
    randDanceOrder = random.sample(allDances, k = len(allDances))
    danceOrder = {key:value for key,value in enumerate(randDanceOrder)}

    #create a dictionary of the partners in a random order
    allPartners = df["Partners"].unique().tolist()
    randPartnerOrder = random.sample(allPartners, k = len(allPartners))
    partnerOrder = {key:value for key,value in enumerate(randPartnerOrder)}

    return [dancesByPartner, danceOrder, partnerOrder]

def buildHeat(dancesByPartner: dict, danceOrder: dict, partnerOrder: dict):    
    print(dancesByPartner)
    print(danceOrder)
    print(partnerOrder)
    pass

if __name__ == "__main__":
    dancesByPartner, danceOrder, partnerOrder = buildDatabases("2021-10 Program.xlsx")
    buildHeat(dancesByPartner, danceOrder, partnerOrder)