#Factorial  using recursion 

def fact(n):

    if(n==1):
        return 1

    return n*(fact(n-1))

a=fact(3)
print(a)