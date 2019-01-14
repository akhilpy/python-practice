"""
Assertion: 
         An assertion in python is one which assert (Truthness) of the code.
         It is boolean experssion that confirm the boolean output of code.  

"""
assert 2==2  # AsserationError will popup

def div(p,q):

    assert q !=0  #Here assert will assure q is not equal to 0, if it is, will show AsserationError. 
    return p/q   


print(div(4,2))