
a=4
b=0
try:
    b=a/b
    print(b)
except Exception as e:
    # this block execute when any exception genrate from Try block
    # you have a choice here , you can raise exception here
    print("you cant divide by zero",e)
finally: 
    # always excute this block
    print(" execute close ")