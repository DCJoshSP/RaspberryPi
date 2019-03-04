import pyowm
import datetime

clothes_dict ={ #creates clothes dictionary, assume they have more than 1 of each item
    "Hats": [],
    "Gloves": [],
    "Shirts": [],
    "Jackets": [],
    "Bottoms": [],
    "Socks": []
    }

ride_x_dict ={  #ride of current day
    "Hats": {},
    "Gloves": {},
    "Shirts": {},
    "Jackets": {},
    "Bottoms": {},
    "Socks": {}
    }

journey_dict = {}       #response dictionary
weather_dict = {}       #current weather dictionary

def enter_wardrobe():
    for i in clothes_dict:      #cycles through dictionary, press "enter" to end each list
        while "" not in clothes_dict[i]:
            clothes_dict[i].append(input("What " + i + " do you cycle in?: "))
        clothes_dict[i].pop()   #removes unecessary blank
    with open("clothes.txt", "w") as myfile:
        print(clothes_dict, file=myfile)

def enter_today():
    for i in ride_x_dict:   #cycles through dict, asks for each item
        ride_x_dict[i] = input("What " + i + " are you wearing today?: ")
    with open("clothes.txt", "a") as myfile:
        print(ride_x_dict, file=myfile)

def feeling():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    journey_dict[current_date] = input("How did you feel on your journey today? \nvery warm \nwarm \ncold \nvery cold \n")
    with open("clothes.txt", "a") as myfile:
        print(journey_dict, file=myfile)


owm = pyowm.OWM('19869702ff812dc8fab95ff8ddffec2f')

def weather_today():
    observation = owm.weather_at_place('London,GB') ### Search for current weather in London (Great Britain)
    w = observation.get_weather()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    weather_dict[current_date] = dict(w.get_temperature('celsius'), **{"status": w.get_status()}, **w.get_wind(), **{"humidity": w.get_humidity()}) ### Weather details
    with open("clothes.txt", "a") as myfile:
        print(weather_dict, file=myfile)

def weather_forecast():
    fc = owm.three_hours_forecast('London,uk')  # requests 3 day forecast
    str_tomorrow = "2019-03-02 08:10:06+00"
    f = fc.get_weather_at(str_tomorrow)
    x = f.get_temperature('celsius')
    with open("clothes.txt", "a") as myfile:
        print("tomorrow weather: " + str(x['temp']) + "°C", file=myfile)

##with open("clothes.txt", "r") as myfile2:
##    for line in myfile2:
        
enter_wardrobe()
##print(clothes_dict)
enter_today()
##print(ride_x_dict)
feeling()
##print(journey_dict)
weather_today()
##print(weather_dict)
weather_forecast()


#hardware buttons?


#ignore stuff below:
journey_dict = {'2019-02-23': 'very warm'}
forecast = {'2019-02-23': 5, '2019-02-23': 10, '2019-02-23': 0, '2019-02-23': 13, '2019-02-23': 1}

weather_dict = {'2019-02-23':{"temp": 5}, '2019-02-23':{"temp": 10}, '2019-02-23':{"temp": 0}, '2019-02-23':{"temp": 13}, '2019-02-23':{"temp": 1}}
feelings = ['very warm', 'warm', 'cold', 'very cold']

current_date = datetime.datetime.now().strftime("%Y-%m-%d")

def analysis():
    journey_dict[current_date] = input("How did you feel on your journey today? \nvery warm \nwarm \ncold \nvery cold \n")
    for key in clothes_dict:
        for val in clothes_dict[key]:
            for feeling in feelings:
                if weather_dict[current_date][feeling] > 18:
                    clothes_dict[key][ride_x_dict[key][current_date]] *= 0.25
                elif 9 <= weather_dict[current_date][feeling] <= 18:
                    clothes_dict[key][ride_x_dict[key][current_date]] *= 0.5
                elif 2 <= weather_dict[current_date][feeling] <= 9:
                    clothes_dict[key][ride_x_dict[key][current_date]] *= 0.75
                elif weather_dict[current_date][feeling] < 2 :
                    clothes_dict[key][ride_x_dict[key][current_date]] *= 1.00


#what to wear same time tomorrow based on results.
##next_day == True                    
##while next_day == True:
##    for i in ride_x_dict:   #cycles through dict, asks for each item
##        ride_x_dict[i][current_date] = input("What " + i + " are you wearing today?: ")
##    journey_dict[current_date] = input("How did you feel on your journey today? \nvery warm \nwarm \ncold \nvery cold \n")
##    analysis()
##    print(clothes_dict)
##    current_date = current_date + timedelta(days=1)
        

    
#this will have to cycle each day not sure about the loop yet...
