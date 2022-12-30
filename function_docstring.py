print("Hello everyone,nice to meet you all")
def func(a , b) :
    """This function write for sum to a and b
       and return the average to a and b
        and importance things is it only work two input."""  ## docstring of the func function.
    print("sum of the ",a ," and ",b," = ",a+b)  #* my write function in python.
    return (a+b)/2
print(func.__doc__)
print(func(3,5))