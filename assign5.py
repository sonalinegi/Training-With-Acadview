#To check if input is leap year or not
year=int(input("Enter year to be checked:"))
if (year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")

# Take length and breadth input from user and check whether the dimensions are of square or rectangle
length = float(input('Please Enter the length of a Rectangle: '))
breadth = float(input('Please Enter the breadth of a Rectangle: '))
if (length==breadth):
    print('area of square')
else:
    print('area of rectangle')

# Take the input age of 3 people and determine oldest and youngest among them
first=int(input("enter the first person age:"))
second=int(input("enter the  second person age:"))
third=int(input("enter the third person age:"))
if (first >= second and first >= third):
  print ("Oldest is first")
elif (second >= first and second >= third):
  print ("Oldest is second")
elif (third >= first and third >= second):
  print ("Oldest is third")

if (first <= second and first <= third):
  print ("youngest is first")
elif (second <= first and second <= third):
  print ("youngest is second")
elif (third <= first and third <= second):
  print ("youngest is third")

# question no 5
quantity=int(input("enter the required quantity:"))
cost=100*quantity
if (cost>1000):
    total_cost=cost-cost*10/100
else:
    total_cost=cost
print("the total cost is:%d" %(total_cost))

#question no 6
points=int(input("enter the points:"))
if(points<=200):
    if (points<=50):
        print("SORRY NO PRIZE THIS TIME")
    elif (points>=51 and points<=151 ):
        print("Congratulations! You won a wooden dog!")
    elif (points>=151 and points<=180):
        print("Congratulations! You won a book!")
    elif (points>=181 and points<=200):
        print("Congratulations! You won a choclates")
else :
    print("you exceed your points limit ")
