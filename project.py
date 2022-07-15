import random
import numpy as np
import pandas as pd

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
#TODO: check for repeating partners in the same heat and remove them
def buildHeat(dancesByPartner: dict, danceOrder: list, partnerOrder: list):

    i = 1
    removed = False
    heats = []
    for danceKey in danceOrder:
        couplesPerHeat = []

        # index = 0
        # while index != len(partnerOrder):
        #     if danceKey in dancesByPartner[partnerOrder[index]]:
                
        #         #check if the about-to-be-added couple contains repeating partners in the same heat
        #         splitPartners = partnerOrder[index].split(" + ")
        #         for j in range(len(couplesPerHeat)):
        #             if splitPartners[0] in couplesPerHeat[j].split(" + ") or splitPartners[1] in couplesPerHeat[j].split(" + "):
        #                 saved = partnerOrder[index]
        #                 print(partnerOrder)
        #                 partnerOrder.remove(saved)
        #                 print("removed",saved)
        #                 print(partnerOrder)
        #                 partnerOrder.append(saved)
        #                 print("added",partnerOrder)
        #                 removed = True
        #                 break
        #         if removed:
        #             removed = False
        #             continue
        #         else:
        #             couplesPerHeat.append(partnerOrder[index])

        #     if len(couplesPerHeat) == 3:
        #         globals()[f"Heat{i}"] = Heat(danceKey, couplesPerHeat) #THIS IS A VERY BAD IDEA!!!!!!!!!!! but hey, Python allows it :)
        #         heats.append(globals()[f"Heat{i}"])
        #         couplesPerHeat = []

        #     index += 1

        #WIP solution where the spliting of heats is going to be handled after the big heats are created.
        #From these big heats, need to split up the couples for those dances based on repeating partners
        for partnerKey in partnerOrder:
            if danceKey in dancesByPartner[partnerKey]:
                couplesPerHeat.append(partnerKey)
            
        globals()[f"Heat{i}"] = Heat(danceKey, couplesPerHeat) #THIS IS A VERY BAD IDEA!!!!!!!!!!! but hey, Python allows it :)
        heats.append(globals()[f"Heat{i}"])
        couplesPerHeat = []

        #************************************************** WORKING SOLUTION FOR NOW
        # for partnerKey in partnerOrder:
        #     if danceKey in dancesByPartner[partnerKey]:
        #         couplesPerHeat.append(partnerKey)
        #     if len(couplesPerHeat) == 3:
        #         globals()[f"Heat{i}"] = Heat(danceKey, couplesPerHeat) #THIS IS A VERY BAD IDEA!!!!!!!!!!! but hey, Python allows it :)
        #         heats.append(globals()[f"Heat{i}"])
        #         couplesPerHeat = []


        # #checking if there are people left to add
        # if len(couplesPerHeat) != 0:
        #     globals()[f"Heat{i}"] = Heat(danceKey, couplesPerHeat)
        #     heats.append(globals()[f"Heat{i}"])
        #     couplesPerHeat = []
        #**************************************************
        
        i += 1
    return heats

#fuction to order the heats
def orderHeats():
    pass

if __name__ == "__main__":
    # dancesByPartner, danceOrder, partnerOrder = buildDatabases("2021-10 Program.xlsx")
    # heatList = buildHeat(dancesByPartner, danceOrder, partnerOrder)
    # dancesByPartner = {'Annie Murphy + Alex': ['Waltz', 'Tango', 'Foxtrot', 'Cha-Cha', 'Rumba', 'Swing', 'Bolero', 'WCSw', 'Pasodoble'], 
                        # 'Annie Zhang + Dmitry': ['Waltz', 'Tango', 'Foxtrot', 'Cha-Cha', 'Rumba', 'Swing', 'Salsa', 'Hustle', 'Waltz', 'Tango', 'Foxtrot', 'Cha-Cha', 'Rumba', 'Swing', 'Salsa', 'Hustle'], 
                        # 'Carrie Heffner + Sergei': ['Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Bolero', 'WCSw', 'Salsa', 'Hustle'], 
                        # 'Cindy Moore + Dmitry': ['Bachata', 'Int.Cha-Cha', 'Int.Samba', 'Int.Rumba', 'Jive', 'Int.Cha-Cha', 'Int.Samba', 'Int.Rumba', 'Jive', 'Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Bolero', 'Mambo', 'WCSw', 'Merengue', 'Pasodoble', 'Salsa', 'Hustle'], 
                        # 'Diana Yin + Alex': ['Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Bolero', 'Mambo', 'Arg.Tango', 'Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Bolero', 'Mambo', 'Arg.Tango', 'Open Mambo', 'Open Mambo', 'Int.Cha-Cha', 'Int.Samba', 'Int.Rumba', 'Pasodoble', 'Quickstep', 'Int.Cha-Cha', 'Int.Samba', 'Int.Rumba', 'Pasodoble', 'Quickstep'], 
                        # 'Donna Reed + Sergei': ['Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing'], 
                        # 'Ellie Konovalova + Dmitry': ['Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Bolero', 'Samba', 'Merengue', 'Pasodoble', 'Hustle'], 
                        # 'Jackie Tarr + Alex': ['Int.Cha-Cha', 'Int.Samba', 'Int.Rumba', 'Pasodoble', 'Jive', 'Int.Cha-Cha', 'Int.Samba', 'Int.Rumba', 'Pasodoble', 'Jive'], 
                        # 'Jackie Tarr + Dmitry': ['Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Quickstep', 'Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Quickstep'], 
                        # 'Jane DiCecco + Dmitry': ['Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Bolero', 'Merengue', 'Hustle', 'Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Bolero', 'Merengue', 'Hustle'], 
                        # 'Jeanne-Marie Blystone + Alex': ['Waltz', 'Foxtrot', 'Cha-Cha', 'Rumba', 'Bolero', 'WCSw', 'Waltz', 'Foxtrot', 'Cha-Cha', 'Rumba', 'Bolero', 'WCSw'], 
                        # 'Karol Giannantonio + Sergei': ['Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Merengue', 'Salsa', 'Hustle', 'Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Merengue', 'Salsa', 'Hustle', 'Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Merengue', 'Salsa', 'Hustle'], 
                        # 'Pam Liu + Dmitry': ['Waltz', 'Tango', 'Foxtrot', 'Cha-Cha', 'Rumba', 'Bolero', 'Arg.Tango'], 'Patrick Seyler + Dasha': ['Arg.Tango', 'Arg.Tango'], 
                        # 'Rebecca Jordan + Sergei': ['Waltz', 'Tango', 'Foxtrot', 'Cha-Cha', 'Rumba', 'Swing', 'Mambo', 'Merengue', 'Waltz', 'Tango', 'Foxtrot', 'Cha-Cha', 'Rumba', 'Swing', 'Mambo', 'Merengue'], 
                        # 'Shuai Wang + Alex': ['Waltz', 'Tango', 'Foxtrot', 'Cha-Cha', 'Rumba', 'Swing', 'Mambo'], 'Sophia Kogay + Alex': ['Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Bolero', 'Mambo', 'Samba'], 
                        # 'Sophia Kogay + Sergei': ['Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Bolero', 'Mambo', 'Samba']}

    # danceOrder = ['Bolero', 'Tango', 'Int.Samba', 'Hustle', 'V.Waltz', 'Jive', 'Pasodoble', 'Rumba', 'Salsa', 'Open Mambo', 'Foxtrot', 'Bachata', 'Mambo', 'Arg.Tango', 'Swing', 'Merengue', 'Cha-Cha', 'Int.Cha-Cha', 'Samba', 'Quickstep', 'Waltz', 'WCSw', 'Int.Rumba']
    # partnerOrder = ['Patrick Seyler + Dasha', 'Rebecca Jordan + Sergei', 'Donna Reed + Sergei', 'Annie Zhang + Dmitry', 'Karol Giannantonio + Sergei', 'Carrie Heffner + Sergei', 'Jeanne-Marie Blystone + Alex', 'Jackie Tarr + Alex', 'Cindy Moore + Dmitry', 'Sophia Kogay + Sergei', 'Annie Murphy + Alex', 'Shuai Wang + Alex', 'Pam Liu + Dmitry', 'Diana Yin + Alex', 'Jackie Tarr + Dmitry', 'Ellie Konovalova + Dmitry', 'Jane DiCecco + Dmitry', 'Sophia Kogay + Alex']

    dancesByPartner = {'Pam Liu + Dmitry': ['Waltz', 'Tango', 'Foxtrot', 'Cha-Cha', 'Rumba', 'Bolero', 'Arg.Tango'], 
                        'Diana Yin + Alex': ['Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Bolero', 'Mambo', 'Arg.Tango', 'Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Bolero', 'Mambo', 'Arg.Tango', 'Open Mambo', 'Open Mambo', 'Int.Cha-Cha', 'Int.Samba', 'Int.Rumba', 'Pasodoble', 'Quickstep', 'Int.Cha-Cha', 'Int.Samba', 'Int.Rumba', 'Pasodoble', 'Quickstep'], 
                        'Patrick Seyler + Dasha': ['Arg.Tango', 'Arg.Tango'], 'Annie Zhang + Dmitry': ['Waltz', 'Tango', 'Foxtrot', 'Cha-Cha', 'Rumba', 'Swing', 'Salsa', 'Hustle', 'Waltz', 'Tango', 'Foxtrot', 'Cha-Cha', 'Rumba', 'Swing', 'Salsa', 'Hustle'],
                        'Carrie Heffner + Sergei': ['Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Bolero', 'WCSw', 'Salsa', 'Hustle'],
                        'Karol Giannantonio + Sergei': ['Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Merengue', 'Salsa', 'Hustle', 'Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Merengue', 'Salsa', 'Hustle', 'Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Merengue', 'Salsa', 'Hustle'],
                        'Cindy Moore + Dmitry': ['Bachata', 'Int.Cha-Cha', 'Int.Samba', 'Int.Rumba', 'Jive', 'Int.Cha-Cha', 'Int.Samba', 'Int.Rumba', 'Jive', 'Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Cha-Cha', 'Rumba', 'Swing', 'Bolero', 'Mambo', 'WCSw', 'Merengue', 'Pasodoble', 'Salsa', 'Hustle'],
                        'Jackie Tarr + Dmitry': ['Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Quickstep', 'Waltz', 'Tango', 'Foxtrot', 'V.Waltz', 'Quickstep']
                        }
    
    danceOrder = ['Arg.Tango', 'Salsa', 'Quickstep']
    partnerOrder = ['Pam Liu + Dmitry', 'Diana Yin + Alex', 'Patrick Seyler + Dasha', 'Annie Zhang + Dmitry', 'Carrie Heffner + Sergei', 'Karol Giannantonio + Sergei', 'Cindy Moore + Dmitry', 'Jackie Tarr + Dmitry']

    heatList = buildHeat(dancesByPartner, danceOrder, partnerOrder)

    for i in heatList:
        print(i.dance, i.couples)

