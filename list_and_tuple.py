         #* Lists of python and method of list.
name = ["Debraj Das", "Moumita Das", "Susmita Das", "Sekharaj Das"]
# name.clear()    #! clear method use to clear whole list;
print("\n", name)
number = [23, 34, 83, 94, 101, 8, 83, 18]
print("Before sorted number list = ", number)
number.sort()
print("number list after sorted in ascending order = ", number)
number.reverse()
print("After reverse the number list = ", number)
number.pop()
print("number list after pop up last member = ", number)
number.remove(94)
print("number list after remove 94 = ", number)
number.append(34)
print("number list after appending 34 = ", number)
number.insert(3, 89)
print("number list after insert 89 at 3 index = ", number)
print("index of 34 is = ", number.index(34))
name.extend(number)
print("extention of name list with number = ",name)
number[2] = 48      #@ member of the list can be change so it is a Mutable.
print("after add a member number = ",number)

        ## tuple of the python
tp = (2 , 8 , 0 )
#!  tp[1] = 8  member of the tuple can not be change.so it is a Inmutable.
print("member of the tuple = ",tp)
print("no of member in tuple is ",tp.__len__())
single_tp = (8 ,)  #~ for define singal member tuple's syntex 
print("single member tuple = ",single_tp)