import sys
import requests
import geocoder
import datetime
import json
import csv
import os

search_query = sys.argv[1]

d = datetime.datetime.now()
    
delta = datetime.timedelta(days=1)
    
tempDate = str(d - delta)
tempYear = tempDate[:4]
tempMonth = tempDate[5:7]
tempDay = tempDate[8:10]
        
github_url = "https://raw.githubusercontent.com/COVID19PVI/data/master/Model12.4/Model_12.4_" + tempYear + tempMonth + tempDay + "_results.csv"

ls1= []
ls2= []
    
def get_location():
    res = ""
    ip = geocoder.ip("me")
    g = geocoder.osm(ip.city)
    city = ip.city
    county = g.county
    if not city and not county:
        return res
    if not city:
        city = ip.town
    loc = ip.state
    if city:
        loc+= ', '+city
    if county:
        loc+= ', '+county
    ls1.append("Location")
    ls2.append(loc)
    res = ip.state
    if county:
        res+=', '+county.replace(" County",'')
    elif city:
        res+=', '+city+" City"
    return res


def get_formatted_results():
    formatted_results = []
    for i in range(0,11):
        value = ls2[i]
        if i >= 1:
            value = value[:4]
        result = {
            "title": ls1[i]+': '+str(value),
            "subtitle": '782'+str(i),
            "arg": 'aksd_'+str(i),
            "autocomplete": 'pvi data_ '+str(i),
            "icon": {
                "path": "covid_icon.png"
             }
        }
        formatted_results.append(result)

    return formatted_results


def write_file(search_results):
    open('local.txt', 'wb').write(search_results.content)
    with open('local.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count =0 
        for row in csv_reader:
            line_count +=1
            if line_count > 1:
                return row

def read_csv(search_results, search_string):
    open('local.txt', 'wb').write(search_results)
    with open('local.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for val in csv_reader:
            if val[3] == search_string:
                ls1.append("PVI")
                ls1.append("Infection Rate: Transmissible Cases")
                ls1.append("Infection Rate: Disease Spread")
                ls1.append("Pop Concentration: Pop Mobility")
                ls1.append("Pop Concentration: Residential Density")
                ls1.append("Intervention: Vaccines")
                ls1.append("Intervention: Social Distancing")
                ls1.append("Intervention: testing")
                ls1.append("Health & Environment: Hospital Beds")
                ls1.append("Health & Environment: Hospital ventilators")
                ls1.append("Health & Environment: Hospital Air Polution")
                ls2.append(val[0])
                ls2.append(val[5])
                ls2.append(val[6])
                ls2.append(val[7])
                ls2.append(val[8])
                ls2.append(val[9])
                ls2.append(val[10])
                ls2.append(val[11])
                ls2.append(val[12])
                ls2.append(val[13])
                ls2.append(val[15])
                break
        os.remove("local.txt")  
            

if __name__ == "__main__":
    search_string = ""
    file_name = ""
    search_string = get_location()
    r = requests.get(github_url)
    data = read_csv(r.content, search_string)

    alfred_json = json.dumps({
        "items": get_formatted_results()
    }, indent=2)

    sys.stdout.write(alfred_json)
