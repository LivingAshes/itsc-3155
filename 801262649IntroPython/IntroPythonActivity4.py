#program 4 Jeremie Koehler 9/3/22

itnum = int(input("Number of items: "))
itemlist = list()
for x in range(0, itnum):
    stritem = input("Input item and price: ")
    itemlist.append(stritem)
for i in range(0, itnum): 
    print(itemlist[i-1])