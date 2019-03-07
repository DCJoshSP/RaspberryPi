import pyowm
import datetime

clothes_dict ={ #creates clothes dictionary, assume they have more than 1 of each item
    "Shirts": {},
    "Trousers": {},
    "Sweaters": {},
    "Socks": {}
    }

ride_x_dict ={  #ride of current day
    "Shirts": {},
    "Trousers": {},
    "Sweaters":{},
    "Socks": {}
    }

Shirts_d = {
    1: ("Sleeveless/scoop-neck blouse",0.12),
    2: ("Short-sleeve knit sport shirt",0.17),
    3: ("Short-sleeve dress shirt",0.19),
    4: ("Long-sleeve dress shirt",0.25),
    5: ("Long-sleeve flannel shirt",0.34),
    6: ("Long-sleeve sweatshirt",0.34)
}

Trousers_d = {
1:("Short shorts",0.06),
2:("Walking shorts",0.08),
3:("Straight trousers (thin)", 0.15),
4:("Straight trousers (thick)",0.24),
5:("Sweatpants",0.28),
6:("Overalls",0.30),
7:("Coveralls",0.49)}

Sweaters_d = {
    1:("Sleeveless vest (thin)",0.13),
    2:("Sleeveless vest (thick)",0.22),
    3:("Long-sleeve (thin)",0.25),
    4:("Long-sleeve (thick)",0.36)
    }

Socks_d = {
1:("(thin socks)/sandals/shoes", 0.02),
2:("Slippers (quilted,lined)/Calf-length socks",0.03),		
3:("Knee socks (thick)",0.06),
4:("Boots",0.10)
}

journey_dict = {}       #response dictionary
weather_dict = {}       #current weather dictionary

def enter_wardrobe():
    for i in clothes_dict:#cycles through dictionary, press "enter" to end each list
        end = False
        while end == False:
            print("What " + i + " do you cycle in?:")
            for k in globals()[i+"_d"]:
                print(str(k)+"."+globals()[i+"_d"][k][0])
            choice = int(input())
            if choice == 0:
                end = True
            else:
                clothes_dict[i].update({globals()[i+"_d"][choice][0]:globals()[i+"_d"][choice][1]})
    with open("clothes.txt", "w") as myfile:
        print(clothes_dict, file=myfile)
        
def enter_today():
    for i in ride_x_dict:   #cycles through dict, asks for each item
        print("What " + i + " are you wearing today?: ")
        for k in globals()[i+"_d"]:
            print(str(k)+"."+globals()[i+"_d"][k][0])
        choice = int(input())
        ride_x_dict[i] = globals()[i+"_d"][choice][0]
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
    weather_dict[current_date] = dict(w.get_temperature('celsius'))# **{"status": w.get_status()}, **w.get_wind(), **{"humidity": w.get_humidity()}) ### Weather details
    with open("clothes.txt", "a") as myfile:
        print(weather_dict, file=myfile)

def weather_forecast():
    fc = owm.three_hours_forecast('London,uk')  # requests 3 day forecast
    str_tomorrow = "2019-03-08 07:00:00+00"
    f = fc.get_weather_at(str_tomorrow)
    x = f.get_temperature('celsius')
    with open("clothes.txt", "a") as myfile:
        print("tomorrow weather: " + str(x['temp']) + "°C", file=myfile)

print("Enter relevant number for choice, enter 0 to finish list\n")
if input("Do you want to update your wardrobe: Y/N ") == "Y":
    enter_wardrobe()
#print(clothes_dict)
enter_today()
#print(ride_x_dict)
feeling()
##print(journey_dict)
weather_today()
##print(weather_dict)
weather_forecast()


