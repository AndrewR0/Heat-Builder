import random
import numpy as np
import openpyxl
import pandas as pd
from openpyxl import load_workbook
import openpyxl

class Couple:
    def __init__(self, first: str, second: str):
        self.first = first
        self.second = second

class Heat:
    def __init__(self, dance: str, couples: list):
        self.dance = dance
        self.couples = couples
    def has(self, person: str) -> bool:
        for c in self.couples:
            if person == c.first or person == c.second:
                return True

class CoupleAndDances:
    def __init__(self, couple: Couple, dances: list):
        self.couple = couple
        self.dances = dances

def buildDatabases(excelName: str) -> list:
    df = pd.read_excel(excelName, usecols=[0,1])
    
    #create dictionary of the partners with their assigned dances
    dancesByPartner = df.groupby(["Partners"])["Dances"].apply(list).to_dict()
    
    #create list of the dances in a random order
    allDances = df["Dances"].unique().tolist()
    danceOrder = random.sample(allDances, k = len(allDances))

    #create a list of the partners in a random order
    allPartners = df["Partners"].unique().tolist()
    partnerOrder = random.sample(allPartners, k = len(allPartners))

    return [dancesByPartner, danceOrder, partnerOrder]

#function to create the heats based on dances and partners
def buildHeat(dancesByPartner: dict, danceOrder: list, partnerOrder: list):

    coupleAndDancesList = [] #of type CoupleAndDances

    #for dancers in dancesByPartner:
    for dancers in partnerOrder:
        #print(dancers)
        splitPartners = dancers.split(" + ")
        first = splitPartners[0]
        second = splitPartners[1]
        dances = dancesByPartner[dancers]
        
        coupleAndDancesList.append(CoupleAndDances(Couple(first, second), dances))

    heats = [] #of type Heat

    while len(coupleAndDancesList) != 0:
        coupleAndDance = coupleAndDancesList[0]
        couple = coupleAndDance.couple
        dance = coupleAndDance.dances.pop(0)
        if len(coupleAndDance.dances) == 0: #if couple has no more dances they are scheduled for, remove Couple
            coupleAndDancesList.pop(0)
        
        found = False

        for h in heats:
            if h.dance == dance and (not h.has(couple.first)) and (not h.has(couple.second)):
                h.couples.append(couple)
                found = True
                break

        if not found:
            heats.append(Heat(dance, [couple]))

    return heats

#fuction to order the heats
def orderHeats(heatList: list) -> list:
    ordered = {}
    for i in heatList:
        if i.dance in ordered:
            ordered[i.dance].append(i)
        else:
            ordered[i.dance] = [i]
    
    merged = [x for _ in list(ordered.values()) for x in _]

    return merged

#function to save the heats into the desired workbook
def saveToSheet(fileName: str, sheetName: str, heatList: list):

    excelBook = load_workbook(fileName)
    with pd.ExcelWriter(fileName, engine='openpyxl') as writer:
        writer.book = excelBook
        startRow = 1
        startCol = 1
        currentDance = heatList[0].dance
        for i,v in enumerate(heatList):
            df = pd.DataFrame({
                f'Heat {i+1}': [np.nan]*len(v.couples),
                'Dance': [v.dance]*len(v.couples),
                'Partners': [f'{x.first} + {x.second}' for x in v.couples]
            })
            
            if currentDance != v.dance:
                startRow = 1
                startCol += 5
                currentDance = v.dance

            df.to_excel(
                excel_writer=writer,
                sheet_name=sheetName,
                columns=['Dance', 'Partners'],
                index=False,
                header=False,
                startrow=startRow,
                startcol=startCol,
            )
            startRow += len(v.couples) + 1
        
        writer.save()


if __name__ == "__main__":

    fileName = input("Enter the file you want to save this data to: ")
    #fileName = "2021-10 Program.xlsx"
    #sheetName = "heat"
    sheetName = input("Enter the sheetname you want to save this data to: ")

    dancesByPartner, danceOrder, partnerOrder = buildDatabases(fileName)

    # danceCheck = {}
    # for dancer in dancesByPartner:
    #     for dance in dancesByPartner[dancer]:
    #         if dancer not in danceCheck:
    #             danceCheck[dancer] = {dance: 1}
    #         else:
    #             if dance not in danceCheck[dancer]:
    #                 danceCheck[dancer][dance] = 1
    #             else:
    #                 danceCheck[dancer][dance] += 1
    # print(danceCheck)
    
    heatList = buildHeat(dancesByPartner, danceOrder, partnerOrder)
    orderedList = orderHeats(heatList)

    # for i in orderedList:
    #     for j in i.couples:
    #         print(i.dance, j.first, j.second)

    saveToSheet(fileName, sheetName, orderedList)