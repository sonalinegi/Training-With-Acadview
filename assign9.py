#Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def getarea(self):
        print("Area is : " + str(3.14 * self.radius * self.radius))

    def getcircumference(self):
        print("Circumference is: " + str( self.radius * 2 * 3.14))

ob=Circle(float(input('enter the radius:')))
ob.getarea()
ob.getcircumference()

#Create a Student class and initialize it with name and roll number.
class Student():
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(self.name)
        print(self.roll)

ob= Student(input("Enter name of student : "), input("Enter his/her roll no : "))
ob.display()


# Create a Temprature class.
class Temperature():
    def convertfahrenhiet(self, celsius):
        print("Temperature in Fahrenhiet is : " + str((celsius * (9 / 5)) + 32))

    def convertcelsius(self, farenhiet):
        print("Temperature in Celsius is : " + str((farenhiet - 32) * (5 / 9)))


ob = Temperature()
ob.convertfahrenhiet(int(input("Enter temperature in Celcius : ")))
ob.convertcelsius(int(input("Enter temperature in Fahrenhiet : ")))

# Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings.
class moviedetails():
    def __init__(self, moviename, artistname, yor, ratings) :
        self.moviename= moviename
        self.artistname= artistname
        self.yor= yor
        self.ratings= ratings

    def display(self):
        print("Movie name is :" +str(self.moviename))
        print("Artist name is " +str( self.artistname))
        print("Year of release is " +str (self.yor))
        print("Rating is " +str( self.ratings))

    def update(self):
        self.moviename = input("enter updated Movie name      : ")
        self.artistname = input("enter updated Artist name     : ")
        self.yor = input("enter updated Year of release : ")
        self.ratings = input("enter updated Ratings         : ")

ob = moviedetails('ZNMD', 'HRITIK', '2011', '81')
ob.display()
ob.update()
ob.display()

#Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.
class expenditure():
    def __init__(self,expenditure,savings) :
        self.expenditure= expenditure
        self.savings= savings

    def display(self):
        print("Expenditure is :" + str(self.expenditure))
        print("Saving is " +str(self.savings))
    def totalsalary(self):
        expenditure.totalsalary = expenditure + self.savings

    def display_totalsalary(self):
        print("total Salary is : " + str(self.totalsalary))
ob= expenditure(input("\n\nEnter Expenditure : "), input("Enter Savings     : "))
ob.display()
ob.totalsalary()
ob.display_totalsalary()