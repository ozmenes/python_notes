"""
# source: https://www.youtube.com/watch?v=tvvEqvyh_Vw&ab_channel=Yaz%C4%B1l%C4%B1mBilimi

print("enes","ozmen","03","1993",sep="--") #yorum satiri
print("{} + {} = {}".format(2,3,2+3))

#1 derste Python dersi


#degiskenler
a = 2
b = 5.5
c = a + b
d = "Python"
e = "variables"
f = {1,2,3,4,"Python"}
g = (1,2,3,"variables")
h = {"elma":4,"Armut":5,"Kiraz":6} 
i = True
print(d,e,c) 
print(type(h))
print(type(i),i)



# Operators  https://www.w3schools.com/python/python_operators.asp
# Python Arithmetic Operators

x = 7
y = 5

print(x + y) # Addition Operator
print(x - y) # Subtraction Operator
print(x * y) # Multiplication Opreator
print(x / y) # Division Operator
print(x // y) # Floor Division Operator
print(x % y) # Modulus Operator
print(x ** y) #Exponen Operator : x^y

t = "Welcome"
y = "to"
u = "Python"
z = t + y + u
print(z)

k = "Hello Python"
print(k*5)

print("* " * 1 )
print("* " * 2)
print("* " * 3)
print("* " * 4)
print("* " * 5)

# strings and Lists

a = "Python"
b = [1,2,3,4,5,6,7]

print(b[1])
print( a , b[4])

print(len(a))
print(len(b))

print(a[len(a)-1])
print(b[len(b)-1])

print(a[:4])
x = b[:2]
y = b[2:]
z = x + y
print(b)
print(x)
print(y)
print(z)

print(b[0:])
print(b[::2])# iki atlayarak listeyi print etmek icin

a = {3:"Elma" , "Armut":4}
print(a[3])
print(a["Armut"])


# Get Input from User

#yas = input("Enter ur age: ")# get value as a String
#print("Your age : " + yas )

a = int(input("value a:"))
b = int(input("value b:"))
c = int(input("value c:"))
toplam = a + b + c
print("toplam :",toplam)


#if case
#Python Comparison Operators
# <"Less than", >"Greater than", <="Less than or equal to", >="Greater than or equal to", =="Equal",!="Not equal"

yas = int(input("Age : "))
if yas < 18:
    print("u re under 18. u cant enter to ..")
else:
    print("Welcome to ..")        


islem = int(input("Enter a num :"))

if islem == 1:
    print("ur num is ",islem)
elif islem == 2:
    print(print("ur num is ",islem)) 
elif islem == 3:
    print(print("ur num is ",islem))    
else:
    print("Invalid Transaction")


#Python Logical Operators
# and "Returns True if both statements are true"-- or "Returns True if one of the statements is true"-- not ""

a = 3
b = 4
if a == 3 and b == 4:
    print("Equl")
else:
    print("not Equl")

if a == 3 or  b == 5: # !!!b is not equal 5
    print("Equl")
else:
    print("not equl")   

if not 3 == 3: # not operator mean changs the case 
    print("yes")
else:
    print("no")


# while loops
i = 1

while i <= 1024:
    print("i :",i)
    i *= 2


#break and case
i = 0

while i < 10:
    if i == 5:
        break
    print("i : ",i)
    i +=1

i = 0
while i<10:
    if(i == 3 or i == 5):
        i+=1
        continue  # when i is equl 3 and 5,
    print("i : ",i)
    i+=1

# for Loops

a = [1,2,3,4,5,6]

for number in a:
    print(number)

b ="Python"

for char in b:
    print(char)

#range 

for sayi in range(20,30):
    print(sayi)
    

for evennumbers in range(0,20,2):#even numbers
    print(evennumbers)

# function

def selamla():
    print("Hi")
    print("whatssup!")
    a = input("what s ur name? ")
    print("Welcome to Python,",a)
selamla()

# Lists and Methods

lists =[1,2,3,4,5,"Python"]
a = "Python"

print(a.startswith("Py"))
print(a.endswith("on"))
n = a.replace("P","A")
print(n)

lists.append(n)#adds ONLY one argument
print(lists)

#lists.pop()
#print(lists)


lists.insert(6,7)
lists.insert(8,a)
print(lists)

z = lists.count(a)

print(z)

lists.remove(a)
print(lists)

lists.clear()
print(lists)
"""
# Read & Write Files

file = open("dosya.txt","w")
x = "Hello World\n"
y = "Hello Python\n"
z = "Hello Java"
file.write(x+y+z)
#file.close 

file = open("dosya.txt","r")
file.seek(5) # 10 karakter ileri git 
char = file.read(10)#10 karakter oku
print(char)
oku = file.read
#print(oku) 

#file.close

#file = open("dosya.txt","r")

for satir in file:
    print(satir)
file.close

#OOP Python
#class and methods def
class Account:
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = balance
    def accountInfo(self):
        print("Name : ", self.name)
        print("Number : ", self.number)
        print("Balance : ", self.balance)
    def getMoney(self,amount):
        if self.balance-amount < 0:
            print("You dont have enough money:D")
        else:
            self.balance -= amount
            print("New Balance : ",self.balance)
    def deposit(self,amount):
        self.balance += amount
        print("new balance : ",self.balance)

account =  Account("Mjölnir", 123, 1000)
account.accountInfo()
account.deposit(100)
account.getMoney(1001)
"""


e = 'mat'
a_sum = 1000
length = 50

def exp(x):
    e = 2.72
    print(e)
    print(a_sum)
    print(length)
    return e**x, a_sum / length

#result, 
result, result2 = exp(5)

print(result)
print(result2)
"""