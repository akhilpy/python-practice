
def fib():
    a,b = 1,1
    num=input("Please input:")
    print(a)
    for i in range (1,num):
        a,b=b,a+b
        print(b)
fib()