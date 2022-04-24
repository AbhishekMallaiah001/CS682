import sys
import pandas as pd
import requests
import datetime
import geocoder
from json2html import *
import json
import webbrowser
from beautifultable import BeautifulTable
import warnings

loc = ""

def get_location(zipcode):
    ip = 0
    if(zipcode == "me"):
        ip = geocoder.ip("me")
        g = geocoder.osm(ip.city)
        loc = g.state+', '+ip.city+' ,'+g.county
        print("\n"+loc)
        return g.state+', '+g.county.replace(" County",'')
    else:
        ip = geocoder.osm(zipcode)
        loc = ip.state+', '+ip.city+' ,'+ip.county
        print("\n"+loc)
        return ip.state+', '+ip.county.replace(" County",'')   

def read_csv_from_date_time(numOfDays):
    file_names = []
    d = datetime.datetime.now()
    currYear = d.strftime("%Y")
    currMonth = d.strftime("%m")
    currdDay = d.strftime("%d")
    curent = currYear + currMonth + currdDay
    
    delta = datetime.timedelta(days=1)
    
    currDateCounter = 1
    while(currDateCounter <= numOfDays):
        delta = datetime.timedelta(days=currDateCounter)
        currDateCounter+=1
        tempDate = str(d - delta)
        tempYear = tempDate[:4]
        tempMonth = tempDate[5:7]
        tempDay = tempDate[8:10]
        #print(tempDay)

        url = "https://raw.githubusercontent.com/COVID19PVI/data/master/Model12.4/Model_12.4_" + tempYear + tempMonth + tempDay + "_results.csv"
        r = requests.get(url)
        with open("r.text","w") as f:
            f.write(r.text)
            read_file = pd.read_csv('r.text')
        file_name = 'PVI_'+str(currDateCounter)+'.csv'
        file_names.append(file_name)
        read_file.to_csv(file_name, index = None)
    return file_names
        
def search_files(f_names,search_string, numOfDays):
    #print('INPUT PARAMS:',f_names,search_string)
    result = []
    mean_lis_PVI = []
    mean_lis_infection_rate_tc = []
    mean_lis_infection_rate_dp = []
    mean_lis_pop_concentartion_pm = []
    mean_lis_pop_concentartion_rd = []
    mean_lis_intervention_v = []
    mean_lis_intervention_sd = []
    mean_lis_intervention_test = []
    mean_lis_health_hb = []
    mean_lis_health_hv = []
    mean_lis_health_ap = []


    for i in range(0, numOfDays):
        file = pd.read_csv(f_names[i])
        data = file.values.tolist()
        for val in data:
            if val[3] == search_string:
                mean_lis_PVI.append(val[0])
                mean_lis_infection_rate_tc.append(val[5])
                mean_lis_infection_rate_dp.append(val[6])
                mean_lis_pop_concentartion_pm.append(val[7])
                mean_lis_pop_concentartion_rd.append(val[8])
                mean_lis_intervention_v.append(val[9])
                mean_lis_intervention_sd.append(val[10])
                mean_lis_intervention_test.append(val[11])
                mean_lis_health_hb.append(val[12])
                mean_lis_health_hv.append(val[13])
                mean_lis_health_ap.append(val[15])
                
    mean_PVI = round(sum(mean_lis_PVI)/len(mean_lis_PVI),3)
    result.append(mean_PVI)
    mean_tc = round(sum(mean_lis_infection_rate_tc)/len(mean_lis_infection_rate_tc),3)
    result.append(mean_tc)
    mean_dp = round(sum(mean_lis_infection_rate_dp)/len(mean_lis_infection_rate_dp),3)
    result.append(mean_dp)
    mean_pm = round(sum(mean_lis_pop_concentartion_pm)/len(mean_lis_pop_concentartion_pm),3)
    result.append(mean_pm)
    mean_rd = round(sum(mean_lis_pop_concentartion_rd)/len(mean_lis_pop_concentartion_rd),3)
    result.append(mean_rd)
    mean_v = round(sum(mean_lis_intervention_v)/len(mean_lis_intervention_v),3)
    result.append(mean_v)
    mean_sd = round(sum(mean_lis_intervention_sd)/len(mean_lis_intervention_sd),3)
    result.append(mean_sd)
    mean_test = round(sum(mean_lis_intervention_test)/len(mean_lis_intervention_test),3)
    result.append(mean_test)
    mean_hb = round(sum(mean_lis_health_hb)/len(mean_lis_health_hb),3)
    result.append(mean_hb)
    mean_hv = round(sum(mean_lis_health_hv)/len(mean_lis_health_hv),3)
    result.append(mean_hv)
    mean_ap = round(sum(mean_lis_health_ap)/len(mean_lis_health_ap),3)
    result.append(mean_ap)
    return result

def main():
    n = len(sys.argv)
    result = []
    result1 = []
    result2 = []
    result3 = []
    search_string = ""
    
    if(n == 0):
        numOfDays = int(input("Enter number of days: "))
        search_string = get_location("me")
        f_names = read_csv_from_date_time(numOfDays)
        
        result = search_files(f_names,search_string)
        
    elif(n >3):
            print("Error more than 2 arguments found! Only 2 expected")
            exit
            
    else:    
        if(sys.argv[1] == '-z'):
            zipcode = sys.argv[2]
            #numOfDays = int(input("Enter number of days: "))
            search_string = get_location(zipcode)

            f_names = read_csv_from_date_time(30)
            result = search_files(f_names, search_string, 1)
            result1 = search_files(f_names, search_string, 7)
            result2 = search_files(f_names,search_string, 14)
            result3 = search_files(f_names,search_string, 30)

        elif(sys.argv[1] == "-d"):
            numOfDays = int(sys.argv[2])
            search_string = get_location("me")  
            f_names = read_csv_from_date_time(numOfDays)
            result = search_files(f_names,search_string)
        else:
            print("Expected either -z or -d as command line arguments")
            exit

    my_table4 = BeautifulTable()


    warnings.filterwarnings("ignore")
    
    my_table4.columns.header = [" ", "7 Day Average", "14 Day Average", "30 Day Average"]
    my_table4.append_row(["PVI", result1[0], result2[0], result3[0]])
    my_table4.append_row(["Infection Rate:\n Transmissible Cases", result1[1], result2[1], result3[1]])
    my_table4.append_row(["Infection Rate:\n Diesease Spread", result1[2], result2[2], result3[2]])
    my_table4.append_row(["Pop Concentration:\n Pop Mobility", result1[3], result2[3], result3[3]])
    my_table4.append_row(["Pop Concentration:\n Residential Density", result1[4], result2[4], result3[4]])
    my_table4.append_row(["Intervention:\n Vaccines", result1[5], result2[5], result3[5]])
    my_table4.append_row(["Intervention:\n Social Distancing", result1[6], result2[6], result3[7]])
    my_table4.append_row(["Intervention:\n Testing", result1[7], result2[7], result3[7]])
    my_table4.append_row(["Health & Environment:\n Hospital Beds", result1[8], result2[8], result3[8]])
    my_table4.append_row(["Health & Environment:\n Hospital Ventilators", result1[9], result2[9], result3[9]])
    my_table4.append_row(["Health & Environment:\n Air Pollution", result1[10], result2[10], result3[10]])
    print(my_table4)
    
      
main()
