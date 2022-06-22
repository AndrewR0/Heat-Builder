import numpy as np
import pandas as pd

#use to create/modify an excel sheet to have it have proper format
def createExcel(excelName: str):
    df = pd.read_excel(excelName, sheet_name=0, usecols=[0,1]) #Read the excel sheet
    danceList = df["Dances"].tolist()
    partnerList = df['Partners'].tolist() #make into list

    splitPartners = [i.replace(" ", "").split("+") for i in partnerList] #2D list of partners

    partner1 = [i[0] for i in splitPartners]
    partner2 = [j[1] for j in splitPartners]

    newDf = pd.DataFrame({'Dances': danceList,'Partner1': partner1, 'Partner2': partner2})

    with pd.ExcelWriter("output.xlsx", mode="w") as writer:
        newDf.to_excel(writer, sheet_name="Dance-Partner-List")

if __name__ == "__main__":
    createExcel("2021-10 Program.xlsx")