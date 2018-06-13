#Create a function to calculate the area of a circle by taking radius from user.
rad=float(input("enter the radius:"))
def area(radius) :
    radius= 3.14*rad*rad
    print("area of circle is:%d"%(radius))
print(area(rad))
#Write a function “perfect()” that determines if parameter number is a perfect number.
def perfect(n) :
    sum= 0
    for i in range(1,n) :
        if n % i == 0 :
            sum=sum + i

    if sum == n :
        return True
    else:
        return False

for i in range(1,1001) :
    if perfect(i):
        print(i)
#Print multiplication table of 12 using recursion.
def table(n, t=1):
    if t == 11:
        return
    print(str(n) + " x " + str(t) + " = " + str(n*t))
    table(n, t+1)

table(int(input("Enter number: ")))
#Write a function to calculate power of a number raised to other ( a^b ) using recursion.
def power(a,b) :
    if b == 0:
        return 1
    if b >= 1 :
        return a*power(a,b-1)

print(power(2,3))
#Write a function to find factorial of a number but also store the factorials calculated in a dictionary.
def fact(n) :
    if n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("enter d no:"))
f=fact(num)
dict={num:f}
print(dict)