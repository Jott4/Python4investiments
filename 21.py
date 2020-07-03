import urllib.request
import os
import time
import pandas as pd
path = r"C:\Users\jvgcu\Desktop\Python4Investiments\intraQuarter"
df = pd.read_csv('key_stats.csv')
stock_list = df['Ticker'].unique()
def Check_Yahoo():
    print(stock_list[0])
    ## Added a counter to call out how many files we've already added
    counter = 0
    for e in stock_list[1:]:
        try:
            e = e.replace("C:\\Users\\jvgcu\\Desktop\\Python4Investiments\\intraQuarter/_KeyStats\\","")
            ## Changed the URL & added the modules
            link = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/"+e.upper()+"?modules=assetProfile,financialData,defaultKeyStatistics,calendarEvents,incomeStatementHistory,cashflowStatementHistory,balanceSheetHistory"
            resp = urllib.request.urlopen(link).read()
            ## We go by Bond. JSON Bond
            save = "forward_json/"+str(e)+".json"
            store = open(save,"w")
            store.write(str(resp))
            store.close()
            ## Print some stuff while working. Communication is key
            counter +=1
            print("Stored "+ e +".json")
            print("We now have "+str(counter)+" JSON files in the directory.")


        except Exception as e:
            print(str(e))
            time.sleep(2)
Check_Yahoo()