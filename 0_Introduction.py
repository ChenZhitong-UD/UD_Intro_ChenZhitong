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

import random
print('set your lower range:')
lr = int(input())
print('set your upper range:')
ur = int(input())

random_number = random.randint(lr,ur)
guessed_number = 0
nr_guesses = 0

while not random_number == guessed_number:
    print('make a guess')
    nr_guesses +=1
    guessed_number = int(input())
print(f'Congratulations, you guessed it in {nr_guesses}!')

sentence = input()
words = sentence.split(' ')
words.sort()
print(words)

sentence = input()
words = sentence.split(' ')
words.sort(key = lambda x : x.lower())
print(words)

print('*'*3)
height = int(input())
for i in range(1,height+1):
    spaces = ' '*(height-i)
    stars = '*'*(i+i-1)
    layer = spaces + stars
    print(layer)
print(' '*(height-1) + '|')

p0 = 1
p1 = 1
p2 = 1
n = int(input())
for i in range(n):
    print(p0)
    m = p0 + p1
    p0 = p1
    p1 = p2
    p2 = m