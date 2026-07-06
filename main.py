import requests
import json

print("""
      
Travel Information Dashboard

Displays country information, weather details,
and timezone using multiple public APIs.

Author: Sheldon Pais
      

""")

headers={'Authorization':"YOUR_API_KEY"}

#COUNTRY INFORMATION
country_url="https://api.restcountries.com/countries/v5"

country=input("Enter your country of preference: ")
country=country.title()


country_params={
    "q":country
}    


try:
    response=requests.get(country_url,params=country_params,headers=headers,timeout=10)

    if response.status_code==200:
      
      country_data=response.json()
      #print(json.dumps(country_data,indent=4))  #shows data in structured way
      #print(data["data"]["objects"][0].keys())
      
      
      official_name=country_data["data"]["objects"][0]["names"]["official"]
      capital=country_data["data"]["objects"][0]["capitals"][0]["name"]
      currency=country_data["data"]["objects"][0]["currencies"][0]["name"]
      latitude=country_data["data"]["objects"][0]["capitals"][0]["coordinates"]["lat"]
      longitude=country_data["data"]["objects"][0]["capitals"][0]["coordinates"]["lng"]

      print("=======TRAVEL DASHBOARD=======\n")
      print(":::::: Country Info :::::: \n")
      print("Country : ",official_name)
      print("\nCapital : ",capital)
      print("\nCurrency : ",currency)
    else:
       print("\nInvalid country input")  

except requests.Timeout:
    print("\nServer took too long")

except requests.RequestException:
    print("\nNetwork Error")


#Weather INFORAMTION
weather_url = "https://api.openweathermap.org/data/2.5/weather"
API_KEY= "YOUR_API_KEY"

weather_params={
   "q":capital,
   "appid":API_KEY,
   "units":"metric"
}

try:
    response=requests.get(weather_url,params=weather_params,timeout=10)
    
    if response.status_code==200:

        weather_data=response.json() #this converts data to type<dictionary>
        #print(json.dumps(data,indent=4)) #this shows everything in ordered manner in json format
        print("\n\n:::::: Weather Info :::::: ")
        print("\nCity : ",weather_data["name"])
        print("\nTemperature : ",weather_data["main"]["temp"])
        print("\nWeather Condition : ",weather_data["weather"][0]["main"])

    else:
        print("\nCity not found!") 

except requests.Timeout:
    print("\nServer took too long")

except requests.RequestException:
    print("\nNetwork Error")

#TIME ZONE
time_url="https://timeapi.io/api/v1/time/current/coordinate?"

time_params={
    "latitude":latitude,
    "longitude":longitude
}

try:

    response=requests.get(time_url,params=time_params,timeout=10)
    if response.status_code==200:
      time_data=response.json()
    
      #print(json.dumps(time_data,indent=4))  #this shows everything in ordered manner in json format 
      print("\n\n:::::: Time ::::::")
      print("\nTimezone : ",time_data["timezone"])

    else:
        print("\nTimezone not found")

except requests.Timeout:
    print("\nServer took too long")

except requests.RequestException:
    print("\nNetwork Error")