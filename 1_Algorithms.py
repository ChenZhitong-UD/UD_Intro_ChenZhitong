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

brand = {'name':'leica', 'type':'film camera', 'location':'german', 'year':1955, 'model':'iiif', 'lens':'elmar'}
print(brand)

def adic(c,z):
    for n in c.keys():
        if z == n:
            return True
    return False
print(adic(brand,'name'))

def adic(c,z):
    for n in c.values():
        if z == n:
            return True
    return False
print(adic(brand,'leica'))

def adic(c,z):
    for n in c.items():
        if z == n:
            return True
    return False
print(adic(brand,'leica'))

def swapdic(c):
    newdic = {}
    for z in c.keys():
        newdic[c[z]]=z
    return newdic
print(swapdic(brand))

dict1 = {'a':1, 'b':2, 'c':3, 'd':2}
def swapdic(c):
    newdic = {}
    for z in c.keys():
        if adic(newdic,c[z]):
            cv = newdic[c[z]]
            nv = [cv, z]
            newdic[c[z]]=nv
        else:
            newdic[c[z]]=z
    return newdic
print(swapdic(dict1))

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
