# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:08:31 2020

@author: utilisateur
"""

# PB WF1 - 2018 --> indoor

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import datetime
import time
"""
dates = np.arange(1891 , 2019)

final_tab = []
events = ['MA1', 'MA0', 'MA2', 'MA3', 'MA4', 'MA5', 'MA6', 'MA7', 'MA8', 'MA9', 'MB1',
          'MB2', 'MB3', 'MC1', 'MC2', 'MC3', 'ME1', 'ME2', 'MF1', 'MF2', 'MF3', 'MF4',
          'MF5', 'MF6', 'MF7', 'MF8', 'MF9', 'WA1', 'WA2', 'WA3', 'WA4', 'WA5', 'WA6',
          'WA7', 'WA8', 'WA9', 'WB1', 'WB2', 'WB3', 'WC1', 'WC2', 'WE1', 'WE2', 'WE3',
          'WF1', 'WF2', 'WF3', 'WF4', 'WF5', 'WF6', 'WF7', 'WF8', 'WF9']

print(len(events)* len(dates)) -- > 6784

90 boucles -- > 4 min 13 == 253 sec
"""
records = []
approx = []
no_results = []
events = ['MF9', 'WF1', 'WA1', 'WC2', 'MF5', 'MF6', 'MF7', 'MF8', 'MF9', 'WA1', 'WA2', 'WA3', 'WA4', 'WA5', 'WA6']
dates = [1993, 1897, 1900, 1940, 1989, 2018]
count = 0

x = datetime.datetime.now()

for epreuve in events :
    for annee in dates : 
        count+=1
        time.sleep(2)
        print(epreuve)
        print(str(annee))
        URL = 'http://trackfield.brinkster.net/More.asp?Year={}&EventCode={}'.format(annee, epreuve)
        if epreuve.startswith("W"):
            sexe = "Woman"
        else :
            sexe = "Man"
        page = requests.get(URL)
        
        soup = BeautifulSoup(page.content, 'html.parser')
        tableau = soup.find('table')
        
        tab_25_best = tableau.find_all('td')
        
        #Cas de tableau sans resultat
        if len(tab_25_best) > 2:
            #print(tab_25_best[2].text) #--> "* - 120 y" ou "1 "
            #Certain tableau contienne une ligne en-tete en plus (aproximation de la conversion yard - metre ?)
            #on enregistre cette ligne en attendant de savoir si elle sert et on la retire de notre tableau final
            if len(tab_25_best[2].text) > 2 :
                print("in")
                mon_tab = tab_25_best[3:]
                approx.append([epreuve, annee, tab_25_best[2].text])
            else :
                mon_tab = tab_25_best[2:]
        #sauvegarde des cas sans résultat
        else :
            no_results.append([annee, epreuve, sexe])
            continue
        sport = tab_25_best[1].text

        #recuperation du contenu text des td dans un tab unidimensionnel
        tab_str = []
        for elt in mon_tab :
            #verification et non-prise en compte de la ligne indoor
            if elt.text != "Indoor Results" :
                tab_str.append(elt.text)



            
            
    
        #formatage du tableau
        tab_str = np.reshape(tab_str,(int(len(tab_str)/8), 8))
        for row in range (0, len(tab_str)): 
            temp_tab = np.array([sport, annee, sexe])
            new_tab = np.append(temp_tab, tab_str[row, :])
            print("j'ajoute a record")
            records.append(new_tab)
    
records_df = pd.DataFrame(records, 
                          columns=['Discipline', 'Année', 'Sexe', 'Classement', 'Athlète', 'Nationalité', 'Resultat', '1 - ????', '2- ????', 'Lieu', 'date' ])



y = datetime.datetime.now()
print(str(count))
print(str(y-x))






    
    