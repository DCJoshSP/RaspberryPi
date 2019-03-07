import itertools as it      #combination


#Algorithm with clo values pre-installed
#only using a few items to show method, clo values are accurate
with open("clothes.txt", "r") as myfile:
    for i, line in enumerate(myfile):
        if i == 0:
            data = line.strip()
        if i == 3:
                temp = line.strip()
                temp = float(temp[23:28])

my_clothes = eval(data)
def return_key(val, category):
        for garment in my_clothes[category]:
            if my_clothes[category][garment] == val:
                return garment
#clo varies by 0.16 for every degree on average
#at 21C clo is 1 standard room temperature
#wind chill can be added later

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




