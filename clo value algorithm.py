import itertools as it      #combination



#Algorithm with clo values pre-installed
#only using a few items to show method, clo values are accurate

my_clothes = {
    "shirt":{"short-sleeve": 0.09, "long-sleeve": 0.25},
    "trousers":{"shorts":0.06,"jeans":0.25},
    "jacket":{"vest":0.13,"heavy jacket":0.35},
    "base layer":{"nylon":0.14,"long-sleeve":0.12},
    }

def return_key(val, category):
        for garment in my_clothes[category]:
            if my_clothes[category][garment] == val:
                return garment
#clo varies by 0.16 for every degree on average
#at 21C clo is 1 standard room temperature
#wind chill can be added later

temp = 23
clo_value = 1+((21-temp)*0.16)      #suggest clo value

best1 = []

combinations = it.product(*my_clothes.values())
mylist = list(combinations)
best = 999
for i in mylist:
    count = 0
    total = 0
    newlist = []
    for j in my_clothes:
        newlist.append(my_clothes[j][i[count]])
        count += 1
    total = sum(newlist)
    if abs(clo_value - total) < best:
        best = abs(clo_value - total)
        best_list = newlist
count = 0
print("Best option to wear today: ")
for i in my_clothes:
    print(return_key(best_list[count],i))
    count = count + 1


