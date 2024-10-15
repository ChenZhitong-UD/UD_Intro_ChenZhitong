print("Introduction to Programming")

name = "ZHITONG CHEN"
email = "ucbvzc7@ucl.ac.uk"
age = "23"
print(name + '\n' + email + '\n' + age)

name = "ZHITONG CHEN"
email = "ucbvzc7@ucl.ac.uk"
age = "23"
print(f"name: {name} \nemail: {email} \nage: {age}")

print(0)
print(178)
print(-21)
print(2938/49)
print(436*9948)
print(12**20)

from math import *
print(sin(radians(200)))
print(cos(radians(100)))
print(tan(pi/4))

firstname = input()
lastname = input()
print(firstname + ' ' + lastname)

import random
random_number = random.randint(1,20)
guessed_number = 0
while not random_number == guessed_number:
    guessed_number = int(input())
print('Congratulations, you guessed it!')

mylist = []
for n in range (20):
    mylist.append(n*5)
print(mylist)

def function(input):
    x = 1
    for n in range (1,input+1):
        if input % n == 0:
            x = n
            print(n)
    return(x)
print(function(20))

dic = {'name':'leica', 'type':'film camera', 'location':'german', 'year':1955, 'model':'iiif', 'lens':'elmar'}
print(dic)

def adic(c,z):
    for n in z.keys():
        if c == n:
            return True
    return False

def swapDictionary(d):
    newDict = {}
    for k in d.keys():
        newDict[d[k]]=k
    return newDict

swapDictionary(neueNationalGalerie)

dict1 = {'a':1, 'b':2, 'c':3, 'd':2}
def swapDictionary(d):
    newDict = {}
    for k in d.keys():
        if inDictionary(newDict,d[k]):
            cv = newDict[d[k]]
            nv = [cv, k]
            newDict[d[k]]=nv
        else:
            newDict[d[k]]=k
    return newDict
swapDictionary(dict1)

def fib(n):
    x = {}
    c = 1
    a1 = 0
    a2 = 1
    for i in range(n):
        i = i + 1
        x [i] = a1
        f = a1 + a2
        a2 = a1
        a1 = f
    return x
print(fib(10))
