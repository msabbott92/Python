#1 Basic

for x in range(151):
    print(x)

#Multiple of five

for x in range(5, 1001, 5):
    print(x)

#Printing Coding Dojo way

for x in range(101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

#Whoa. That sucker's huge

finalSum = 0
for x in range(1,500001,2):
    finalSum += x
print(finalSum)

#Countdown by fours

for x in range(2018, 0, -4):
    print(x)

#Flexible Counter

lowNum = 2
highNum = 9 
mult = 3

for x in range(lowNum, (highNum + 1)):
    if x % mult == 0:
        print(x)

