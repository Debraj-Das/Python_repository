  #* set in python and it's methode
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c","z"}
print(type(x))
print( x.issuperset(y))  #! it check x is superset or not.
print(x.union(y))
print(x)
x.update(y)
print(x)