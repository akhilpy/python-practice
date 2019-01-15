from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(10):
            print("hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi")
            sleep(1)

t1=Hello()
t2=Hi()
#main thread create two thread t1, t2 and stat/ run that
t1.start()
#t1.run()
sleep(0.2)
t2.start()
#t2.run() 

#main thread wait here to t1 , t2 to join main thread 
t1.join()
t2.join()

#Then main thread execute from here 
print("bye bye")