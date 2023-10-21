'''
In this file, I calculated the qualities of life for all countries based on the user inputs and 
put them into a text file. 
'''
import requests
import math

f = open("customQuality.txt", "w")

#inputs

purchasingInput = float(input("On a scale of 1-200, how much do you value purchasing power?"))
housePriceInput = float(input("On a scale of 1-5, how much do you value the cost of a house?"))
livingCostInput = 9.9 - float(input("On a scale of 1-20, how much do you value the cost of living in general?")) 
safetyInput = 9.9 - float(input("On a scale of 1-5, how much do you value safety?"))
healthIndexInput = 9.9 -float(input("On a scale of 1-5, how much do you value the health index of the country?"))
trafficInput = 9.9 - float(input("On a scale of 1-5, how much do you value traffic time(or lack thereof)?"))
pollutionInput = 9.9 - float(input("On a scale of 1-5, how much do you value pollution(or lack thereof)?"))
climateInput = 9.9 - float(input("On a scale of 1-5, how much do you value the climate index of the country?"))

#countries
url = "https://www.numbeo.com/api/"
fields = {"api_key" : "0jalvgng5h70u2"}
r = requests.get(url + "/cities", params = fields)

cities = r.json()
cities = cities["cities"]

countries = []

for city in cities:
  if city ["country"] not in countries:
    countries.append(city["country"])

purchasingPower = []
housePriceToIncome = []
costOfLiving = []
safety = []
healthIndex = []
trafficTime = []
pollutionIndex = []
climateIndex = []
calcCountries = []

for countryName in countries:
  url = "https://www.numbeo.com/api/"
  fields = {"api_key": "0jalvgng5h70u2", "country": countryName}
  r2 = requests.get(url + "/country_indices", params = fields)
  r2 = r2.json()
  if "purchasing_power_incl_rent_index" in r2:
    if "property_price_to_income_ratio" in r2:
       if "cpi_and_rent_index" in r2:
         if "safety_index" in r2:
           if "health_care_index" in r2:
             if "traffic_time_index" in r2:
               if "pollution_index" in r2:
                 if "traffic_co2_index" in r2:
                   purchasingPower.append(r2["purchasing_power_incl_rent_index"])
                   housePriceToIncome.append(r2["property_price_to_income_ratio"])
                   costOfLiving.append(r2["cpi_and_rent_index"])
                   safety.append(r2["safety_index"])
                   healthIndex.append(r2["health_care_index"])
                   trafficTime.append(r2["traffic_time_index"])
                   pollutionIndex.append(r2["pollution_index"])
                   climateIndex.append(r2["traffic_co2_index"])
                   calcCountries.append(countryName)

#quality of life 
for i in range (len(calcCountries)):
  f.write(str(calcCountries[i]) + "," + str(max(0, purchasingInput + purchasingPower[i] / housePriceInput - (housePriceToIncome[i] * 1.0) - costOfLiving[i]/livingCostInput + safety[i]/safetyInput + healthIndex[i]/healthIndexInput - trafficTime[i]/trafficInput- pollutionIndex[i]/pollutionInput + climateIndex[i]/climateInput))+"\n")
