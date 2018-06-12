#Take 10 integers from user and print it on screen.
print("enter the elements:")
for i in range(10):
    a=int(input())

#Write an infinite loop.An infinite loop never ends. Condition is always true.
'''while (1):
    print('true')
'''

#create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
list=[]
print('enter the int elements')
list= [int(x) for x in input().split()]
print(list)
def square(list):
    ret = []
    for i in list:
        ret.append(i ** 2)
    return ret

print(square(list))
#From a list containing ints, strings and floats, make three lists to store them separately
list=[1,2,3,'sonali',3.6,8.7,1.1,'antra','shru']
nolist= [x for x in list if isinstance(x, int)]
strlist=[x for x in list if isinstance(x, str)]
floatlist=[x for x in list if isinstance(x, float)]
print(nolist)
print(strlist)
print(floatlist)

#Using range(1,101), make a list containing even and odd numbers.
even=[]
odd=[]
for i in range(1,101):
  if i%2 == 0:
    even.append(i)
  else:
    odd.append(i)
print(even)
print(odd)

#pattern
for i in range(0,5) :
    for j in range(0,i+1) :
        print("*",end=" ")
    print()
#question no  7
n = int(input('enter the size:'))          #n is the number of items you want to enter
d ={}
for i in range(n):
    key=input()
    value=int(input())
    d[key]=value

for x in d :
    print(x)

#question no 8
print('enter the elements in list')
list = [int(x) for x in input().split()]
print(list)
no=int(input('enter no to be removed'))
for i in list:
    if i==no:
        print('found')
list.remove(no)
print(list)
