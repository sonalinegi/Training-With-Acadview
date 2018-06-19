#Create a threading process such that it sleeps for 5 seconds and then prints out a message.
import threading
import time
import math
def mythread() :

    print('thread is starting')
    time.sleep(5)
    print('thread is ending')
t=threading.Thread(target=mythread)
t.start()


#Make a thread that prints numbers from 1-10, waits for 1 sec between
def mythread2():
    for i in range(0,11):
        print(threading.Thread,i)
        time.sleep(1)

t=threading.Thread(target=mythread2)
t.start()

# Make a list that has 5 elements.
#Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
#Delay goes like 2sec-4sec-6sec-8sec-10sec
list=[1,2,3,4,5]
def mythread3(delay=1):
    for i in list :
        delay=delay*2
        time.sleep(delay)
        print(i)
t=threading.Thread(target=mythread3)
t.start()

#Call factorial function using thread.
def fact() :
    no=int(input('enter a no'))
    res=math.factorial(no)
    print(res)

threading.Thread(target=fact).start()

