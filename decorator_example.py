"""
A simple function that take two agruments and returns its sum. 
But Interesting case is we  handle the arugment via  python Decorator
if passed agruments are not interger it will raise an Exception.
"""

def check_args(fun):
    def wrapper(*args, **kwarg):
        for a in args:
            if not isinstance(a, int):
                 #raise TypeError("Expected int, got %s" % (type(a)))
                 raise Exception('input should be interger value ')
        for k,v  in kwarg.items():
            if not isinstance(v, int):
                # raise TypeError("Expected int, got %s" % (type(v)))
                raise Exception('input should be interger value')
        else:
            return fun(*args, **kwarg)
    return wrapper



@check_args
def addnum(a,b):
    return a+b

print(addnum(4, b=4))