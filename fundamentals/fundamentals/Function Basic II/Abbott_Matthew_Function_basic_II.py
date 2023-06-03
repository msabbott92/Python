# Countdown 

def countdown(num):
    countdownTotal = []
    for x in range(num, -1, -1):
        countdownTotal.append(x)
    return countdownTotal

print(countdown(8))

#Print and Return 

def print_and_return(num1, num2):
    print(num1)
    return num2

print_and_return(2,3)
print(print_and_return(2,3))

# First Plus Length 

def first_plus_length(x):
    i = x[0] + len(x)
    return i 

print(first_plus_length([1,2,3,4,5]))

#Values greater than second

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    i = []
    for x in range(len(list)):
        if list[x] > list[1]:
            i.append(list[x])
    print(len(i))
    return i 


print(values_greater_than_second([2,3,5,1,6,2,5]))
print(values_greater_than_second([4]))

#This length, That value

def length_and_value(length, value):
    newList = []
    for x in range(length):
        newList.append(value)
    return newList

print(length_and_value(4,7))



