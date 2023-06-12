from tkinter.tix import Balloon


list_item = [ int , float , "Debraj", 56 , 83 , 3 , "Bappy",45, 203] 

for item in list_item :
    if str(item).isnumeric() and item > 6 :
        print(item)
print("Number of list ",len(list_item),end="\n\n")

list_item.append("pulak")
print(list_item)