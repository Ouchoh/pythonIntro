# import packages
#
# #Assign variable
x = (1, 2, 3, 4)
y = "Hello World hjnmm ,lkjl 97988"
studentsScore = 12, 13, 14, 15
StudentsNames = "John", "Mary", "Tom"
students_Names = "John, Mary, Tom"

#assigning variables by Brian with ooutput
o = 10
print(o)
oi = 17,18,19
print(oi)
ou = 1,2,3
print(ou)
ii,iu,iy = 4,5,7
print(iu)
print(ii,iu,iy)
#combining a text and a variable
t = "Wednesday"
print("Today is " + t)
u = "today is"
w = u + t
print(w)

#print output
print(x)
print(y)
print(studentsScore)
print(StudentsNames)
print(students_Names)

a, b, c = (1, 2, 3)
print(a)


f, g = (1, 2, 3, 4), "Hello World"
print(f, g)
g = h = j = (1,2,3)
print(g, h, j)

#Data types
print(type(y))
print(type(x))
print(type(StudentsNames))
print(type(a))
k = [1, 2, 3, 4, 5]
print(type(k))
l = range(1,10)
print(type(l))
print(l)
studentRecords = {"studentsScore": (12, 13, 14), "StudentsNames": ("John", "Mary", "Tom")}
print(studentRecords)

x = True
print(type(x))

#convert type
k = [1, 2, 3, 4]
#print(type(k))
#print(k)
l = tuple(k)
print(type(l))
print(l)

j = range(1,10)
print(list(j))

#generate random numbers
print(sum((1 , 4)))
print(1 + 4)

#import packages
import random as rd

print(rd.randrange(1, 20))


# casting
flt = str(1)
print(type(flt))

#Boolean
print(10 == 10)

print(bool("nmkcj"))
print(bool(None))

# operation
#MODULUS; Returns the reminder of
print(7 % 2)
#Floor division : trancates
print(3 // 2)

#exponentiation to the power of
print (2 ** 2)

#assignment operators
z = 7
print(z  == 10 )
z %= 4
print(z)

#if..else
a = 40
b = 50
c = 30
#if statement
if b<a:
    print("b>a")
#elif
if b>a:
    print("b>a")
elif b<a:
     print("b<a")

#if..else statement
if b>a:
    print("b>a")
elif b<a:
     print("b<a")
else:
     print("b==a")

#shorthand if..else
print(a) if a>b else print(b) if a<b else print(c)

#and
f = 20
g = 30
h = 10
if f > g  and h > f :
    print(g)
if f < g and h < g:
    print(g)

#or
if f > g  or h < f :
    print(g)

if f > g  or h < f  and g == 30 :
    print(g)

#nested if
x = 50
if x > 10:
    print("above 10")
    if x > 20 :
        print("above 20")
    else:
        print("not above 20")

#pass
if a > b:
   pass

#while loop
g = 1
while g < 10:
    print(g)
    g += 1

#break statement
i = 1
while i < 10:
    print(i)

    if i == 6:
        break
    i += 1

#continue statement
l = 1
while l < 10:

    l += 1
    if l == 6 :
        continue
    print(l)

#else statement
x = 1
while x < 10:
    print(x)
    x += 1
else:
    print ('x is nolonger less than 10')

#Functions
def greetings():
    print("hello world")
greetings()

def students_names(firstName, secondName):
    print(secondName +firstName + " Brian")
students_names(" Ouchoh" , " brian")

#arbtrary arguments, *args
def family (*kids):
    print("first kid" + kids[2])
family(" james", " sharon", " mary" , " tom")

#keywords arguments
def children (child3 , child1 , child2):
    print("last child is" + child3)
children(child1 = " James" , child3 = " sharon" , child2 = " mary")

#arbitrary key arguments , **kwrgs
def children2 (**kids):
    print("middle child " + kids["lname"])
children2( fname = "mary" , lname = "sharon")

#default parameter value
def country(city = "nairobi"):
    print(" I am from " + city)
country(" nakuru")

#return values
def division(x):
    return 10/x
print(division(2))

#pass statement
def country():
    pass

#recursion
def recurring( k ):
    if (k > 0):
        results = k + recurring (k - 1)
        print(results)
    else:
        results = 0
    return results
recurring(6)

#for loops
fruits = [" banana" , "apples" , "mangoes"]
for x in fruits:
    print(x)

#looping through a string
for x in "banana":
    print(x)

#break
for x in fruits:
    if x == "apples":
        break
    print(x)

#continue statement
for x in fruits:
    if x == "apples":
        continue
    print(x)

#range function
for x in range(3 ,6):
    print(x)

#while loop
i = 1
while i < 6 :
    print(i)
    i +=1

#breaking the while loop even when the condition is true
x = 1
while x < 6:
    print(x)
    if x == 3:
        break
    x += 1

#continue .. stops the current indentation and continues with the next
y = 0
while y < 6:
     y += 1
     if y == 3:
       continue
     print(y)

#else statement
g = 1
while g < 6:
    print(g)
    g += 1
else:
    print("g is nolonger less than 6")

#for loops
fruits = ["apple" , "banana" , "cherry"]
for x in fruits :
    print(x)

# stop when we reach banana
matunda = ["apple" , "banana" , "cherry"]
for x in matunda:
    print(x)
    if x == "banana":
        break

#do not print banana
matunda = ["apple" , "banana" , "cherry"]
for x in matunda:
    if x == "banana":
        continue
    print(x)

#else in loop .. specifies a block of code to be executed when the loops is finnished
for x in range(6):
    print(x)
else:
    print("finally finnished")
#the else block will not be executed if the loop is stooped by a break statement
for x in range(6):
    if x == 3:break
    print(x)
else:
    print("finally finnished")

#nested loops..the inner loop will be executed one time for each iteration of the outer loop
adj = ["red" , "big" , "tasty"]
fruits = ["apple" , "banana" , "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

#the pass statement...put in loops with no content t avoid errors
for x in [1,2,3]:
    pass

#lambda
#lambda arguments: expression
x = lambda a:a +10
print(x(5))

y = lambda a,b:a * b
print(y(5,6))

def addition(n):
    return lambda a:a + n
add = addition(10)
print(add(20))

def division(n):
    return (lambda x: x/n)(30)
print (division (3))

#python arrays
import numpy as np
cars = ["ford" , "volvo" , "bmw"]
print(cars [2])

#length of an array
print(len(cars))

#looping array elements
for x in cars:
    print(x)

#adding array elements
cars.append("honda")
print(cars)

#remove elements
cars.pop(1)
print(cars)

cars.remove("ford")
print(cars)

#using lambda in for loops
list1 = [1,2,3,4,5]
list2 = []

for i in list1:
    f = lambda i: i/2
    list2.append(f(i))
print(list2)

#Practice
#question 1
def sum(num1,num2,num3):
    return(num1+num2+num3)

total = sum(50,70,40)

if total < 100:
    print(total)
else:
    print(50*70*40)

#question 2
i = 1
while i < 15:
    print(i/5)
    if i == 15:
        break
    i += 1

#question 3
list1 = [10,30,50,10,40,10]
if  list1[0]==list1[5]:
    print('true')
else:
    print("false")

list2= [75,85,95,65,55]

if list2[0]==list2[4]:
    print("True")
else:
     print("false")


#question 4
divBy3 = [5,9,8,12,15,6,16,20]
for x in divBy3:
   y = lambda x: x/3
   print(y(x))

#question 5
x = [5,9,8,12,15,6,16,20]

#length
print(len(x))

#the fourth value
print(x[4])

#the last value
print(x[len(x)-1])

#reverse list
print(x[: : -1])

#question 6
#y = [10,30,50,10,10,40,10]


my_list = [10,30,50,10,10,40,10]
total = 0

for i in range (0, len(my_list)):
    total = total+ my_list[i]
print(total/len(my_list))

#Classes/Objects
class Person:
    def __init__(self,name,age):   #createa a class named person and assigned values age and name using the init funtion
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)                    #p1 is the object ie self
print(p1.age)

#object methods
# create a method in the class person
class person:                                  #class name
    def __init__(self,name,age):               #_init_ function to assigh name and age values
        self.name = name
        self.age = age
    def myfunc(self):                           #A function that prints greetings and executes self.name
        print("hello my name is "+ self.name)
P1 = person ("John" , 36)                        #creating object p1
P1.myfunc()                                       #a function that executes object p1 and myfunc

print(p1.age == 40)

#modify object properties
#delete object properties
#delete objects
#the pass statement


def sum_Two_Numbers(a,b):
    sumOfValues = a+b
    #print(sumOfValues)

sum_Two_Numbers(8,8)

#create a function that takes in kgs and converts to grams,milligrams and micrograms
#example message * Kgs are equal to * grams,which are equal to * milligrams, or * micrograms

grams_converter = 1000
milligrams_converter = 1000 * 1000
micrograms_converter = 1000 * 1000 * 1000

#kgs_to_grams,grams_to_milligrams,miliigrams_to_micrograms
def weight_converter(Weightinkgs,grams_converter,milligrams_converter,micrograms_converter):
    print(Weightinkgs, "KGs is equivalent to",Weightinkgs * grams_converter, "grams")
    print(Weightinkgs,"KGs is equivalent to" , Weightinkgs * milligrams_converter, "milligrams")
    print(Weightinkgs, "KGs is equivalent to", Weightinkgs * micrograms_converter, "micrograms")
    print(Weightinkgs,"kgs is equal to " ,Weightinkgs * grams_converter , " grams which is equal to" , Weightinkgs * milligrams_converter ," milligrams which is equal to" , Weightinkgs * micrograms_converter, "micrograms")
weight_converter(4,grams_converter,milligrams_converter,micrograms_converter )



















