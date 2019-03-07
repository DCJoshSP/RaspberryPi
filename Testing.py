str_dict = ""
countlist = []
with open("clothes.txt", "r") as myfile:
    for i, line in enumerate(myfile):
        if i == 0:
            print(line.strip())
