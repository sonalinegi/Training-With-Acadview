#question no 1
list=[]
f=int(input("1st ele:"))
s=int(input("2nd  ele:"))
t=input('3rd ele:')
list.append([f,s,t])
print(list)
#question no 2)
list.append(['google','apple','facebook','microsoft','tesla'])
print(list)
#question no 3
a=[1,2,1,4,2,3,2]
print(a)
print(a.count(1))
print(a.count(2))
#question  no 4
no=[1,2,5,9,3,7,8]
no.sort()
print(no)
#question no 5
A=[1,3,4,7,8]
B=[9,10,11]
C= A + B
print(C)
C.sort()
print(C)
# stack using list
stack = ["sonali", "shru", "Anta"]
stack.append("rohan")
stack.append("laskhmi")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
#optional que
print(C)
e=0
o=0
for x in C:
        if not x % 2:
    	     e+=1
        else:
    	     o+=1
print("Number of even numbers :",e)
print("Number of odd numbers :",o)
#queue
q = []
for i in range(0, 5):
    q.append(i)  # Add to back of queue
while q:  # Queue not empty
    j = q.pop(0)
    print(j)

