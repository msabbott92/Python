num1 = 42 #variable declaration, string
num2 = 2.3 #variable declaration, string 
boolean = True #variable declaration, initialize boolean 
string = 'Hello World' #variable declaration, initialize string 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize tuples
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement, access value from index 1 of pizza topping list 
pizza_toppings.append('Mushrooms') #add value 'mushrooms' to pizza toppings list 
print(person['name']) #log statement from dictionary no value yet 
person['name'] = 'George' #variable declaration, add value to person dictionary 
person['eye_color'] = 'blue' #variable declaration, add value to person dictionary 
print(fruit[2]) #log statement from index 2 from fruit tuples

if num1 > 45: #conditional if statement 
    print("It's greater") # log statement, string 
else: #conditional else statement
    print("It's lower") #log statement, string

if len(string) < 5: #conditional, if statement 
    print("It's a short word!") #log console, string 
elif len(string) > 15:# conditional, else if statment
    print("It's a long word!") #log console, string 
else: #conditional statement, else
    print("Just right!") #log console, string 

for x in range(5): #for loop, start x stop 5
    print(x) #log statement x
for x in range(2,5): #for loop, start 2 stop 5
    print(x) #log statment x
for x in range(2,10,3): #for loop, 
    print(x)#log statement 
x = 0 #variable declaration, number 
while(x < 5): #while loop, start x stop 5
    print(x) #log statement 
    x += 1 #while loop increment 1

pizza_toppings.pop() #list, delete value
pizza_toppings.pop(1) #list, delete value 

print(person) #log value, list 
person.pop('eye_color') #list, delete specific value 
print(person) #log value, list (updated)

for topping in pizza_toppings: #for loop 
    if topping == 'Pepperoni': #conditional statement 
        continue #for loop, continue
    print('After 1st if statement') #log statement, string
    if topping == 'Olives': #conditional, if statment
        break #for loop, break 

def print_hello_ten_times(): #function 
    for num in range(10): #parameter, for loop
        print('Hello') #log statement 

print_hello_ten_times() #function run

def print_hello_x_times(x): #funciton, x parameter
    for num in range(x): #for loop, parameter
        print('Hello') #log statement 

print_hello_x_times(4) #function run

def print_hello_x_or_ten_times(x = 10):  #function, parameter
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_or_ten_times() #function run
print_hello_x_or_ten_times(4) #function run 


"""
Bonus section
"""

# print(num3) -- NameError: name <variable name> is not defined
# num3 = 72  -- 
# fruit[0] = 'cranberry' -- TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) -- KeyError: 'favorite_team'
# print(pizza_toppings[7]) -- IndexError: list index out of range
#   print(boolean) -- IndentationError: unexpected indent
# fruit.append('raspberry') Tuples add value
# fruit.pop(1) tuples delete value 