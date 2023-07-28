        ## some advance data type in python
d1 =[]
print(type(d1))
d2 = {}
print(type(d2))
d3 = ()
print(type(d3))

        #@ Dictionary and its Method
dic = { "Debraj" : "Rice","Moumita":"Dry food","Susmita":{"brakefast":"Tea","Lunch":"meet"},"little bro":["meet","dry food","Tea"]}
 #* in Dictionary we use any type of data type in vaule,but in Key type general use any static type data type.
 #* so you can use string or integer , float type variable.
print(dic)
print(dic["little bro"])
dic["Ram"] = "vig food"  #$ this appened the new member in dic Dictionary
         ## exchange of upper syntex we can used dic = {"Ram" : "vig food"}
print(dic)
link_dic = dic  #~ this case pointer of two variable(link_dic and dic) are pointed same Dictionary.
cp_dic = dic.copy() #~ this copy Method creat a new dictionary then pointed to cp_dic pointer.
del dic["Debraj"];
print(dic)
print(dic.keys())
print(cp_dic)
print(link_dic)
