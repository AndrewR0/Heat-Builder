import random
import numpy as np
import openpyxl
import pandas as pd
from openpyxl import load_workbook
import openpyxl

class Heat:
    def __init__(self, dance, couples):
        self.dance = dance
        self.couples = couples

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

    i = 1 #Heat number count
    skip = False #Flag to skip to next index in list
    heats = []
    for danceKey in danceOrder:
        couplesPerHeat = [] #list of unique partners to add to the heat
        repeatPartners = False #check for repeat partners while scanning the list to avoid one partner dancing with two partners in one heat
        
        tempPartnerOrder = list(partnerOrder)
        index = 0
        while index != len(tempPartnerOrder):# or repeatPartners != 0:
            if danceKey in dancesByPartner[tempPartnerOrder[index]]:

                #check if the about-to-be-added couple contains repeating partners in the same heat
                splitPartners = tempPartnerOrder[index].split(" + ")

                for j in range(len(couplesPerHeat)):
                    if splitPartners[0] in couplesPerHeat[j].split(" + ") or splitPartners[1] in couplesPerHeat[j].split(" + "):
                        repeatPartners = True
                        index += 1 #if either of the partners are already in this heat, skip adding them
                        skip = True
                        break
                
                #Found repeat couple, skip over them (maybe this and 'repeatPartners' are the same thing)
                if skip:
                    skip = False
                    continue

                couplesPerHeat.append(tempPartnerOrder[index])
                tempPartnerOrder.remove(tempPartnerOrder[index])

            #Reached the end of the list and all unique couples are found
            elif index == len(tempPartnerOrder)-1:
                
                globals()[f"Heat{i}"] = Heat(danceKey, couplesPerHeat) #THIS IS A VERY BAD IDEA!!!!!!!!!!! but hey, Python allows it :)
                heats.append(globals()[f"Heat{i}"])
                couplesPerHeat = []
                index += 1

                if repeatPartners:
                    repeatPartners = False
                    index = 0
                    i += 1

            else: #current couple is not doing the current dance
                index += 1

        #In case the end of the list is reached and the couple is participating in the current dance but they have repeating partners
        if len(couplesPerHeat) != 0:
            globals()[f"Heat{i}"] = Heat(danceKey, couplesPerHeat)
            heats.append(globals()[f"Heat{i}"])

        i += 1
    
    #Edge case
    if len(couplesPerHeat) != 0:
        globals()[f"Heat{i}"] = Heat(danceKey, couplesPerHeat)
        heats.append(globals()[f"Heat{i}"])
    return heats

#fuction to order the heats
def orderHeats():
    pass

#function to save the heats into the desired workbook
def saveToSheet(fileName: str, sheetName: str, heatList: list):

    excelBook = load_workbook(fileName)
    with pd.ExcelWriter(fileName, engine='openpyxl') as writer:
        writer.book = excelBook
        startRow = 1
        startCol = 1
        for i in heatList:
            df = pd.DataFrame({
                f'Heat {i}': [np.nan]*len(i.couples),
                'Dance': [i.dance]*len(i.couples),
                'Partners': [x for x in i.couples]
            })
            
            df.to_excel(
                excel_writer=writer,
                sheet_name=sheetName,
                columns=['Dance', 'Partners'],
                index=False,
                header=False,
                startrow=startRow,
                startcol=startCol,
            )
            startRow += len(i.couples) + 1
        
        writer.save()


if __name__ == "__main__":

    fileName = input("Enter the file you want to save this data to: ")
    sheetName = input("Enter the sheetname you want to save this data to: ")

    dancesByPartner, danceOrder, partnerOrder = buildDatabases(fileName)
    heatList = buildHeat(dancesByPartner, danceOrder, partnerOrder)

    #for i in heatList:
    #    print(i.dance, i.couples)
    saveToSheet(fileName, sheetName, heatList)