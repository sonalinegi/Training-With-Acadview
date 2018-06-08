#TUPLES
#Create a tuple with different data types
tuple = ("sonali", False, 3.2, 1,60)
print(tuple)
print('length of tuple:%d' %(len(tuple)))
#maximum no
a=(100,150,500,265,34)
print('maximum no:%d' %(max(a)))
#minimum no
print('minimum no:%d' %(min(a)))
#product of elements
num=(1,2,3,4,5,6)
product = 1
for i in num:
        product = product * i
print('product of elements:%d' %(product))

#SETS
#sets uding user defined value
#creating user defined set
s=set()
a=input('input values for set a:').split()
for i in a:
    s.add(i)
print(s)
s1=set()
b=input('input values for set b:').split()
for i in b:
      s1.add(i)
print(s1)
#difference between 2 sets
print(s-s1)
#comaparison between 2 sets
print(s==s1)
#intersection of 2 sets
print(s&s1)

#DICTIONORY
n = int(input('enter the size:'))          #n is the number of items you want to enter
d ={}
for i in range(n):
    key=input()
    value=int(input())
    d[key]=value

print(d)
#sort it
for key, value in sorted(d.items(), key=lambda x: x[1]):
    print ("%s: %s" % (key, value))
#mississippi problem
def freq(str):
    dict={}
    for n in str:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else :
            dict[n]=1

    return dict
print(freq('MISSISSIPPI'))
