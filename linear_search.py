"""
 An example of linear search with multiple way, Also it check searching number is int or not via decorator function. 
"""
lst=[12,14,19,32,22,45,36]

def check_args(function):
    """
    This functions is decotator that check the passed argument is int, if not it will show error message
    """
    def wrapper(*args, **kwargs):
        try:
            input = int(args[1]) #  args( passed agruments) is tuple here, args[1] is 2nd argument that have to search in passed list.
        except ValueError:
            print("please enter only number") # if input is not interger value
        return function(*args, **kwargs)
    return wrapper

@check_args
def search_without_loop(lst, num):
    """ 
        This function will search 'num' in list 'lst'
        :param lst, num: 
        :return: Boolean 
    """
    if num in lst:
        print("found here")
        return True
    else:
        print(" not found")
        return False 
@check_args
def search_while_loop(lst, num):
    """ 
    This function with While  loop will search 'num' in list 'lst'
    :param lst, num: 
    :return: Boolean 
    """
    i=0
    while i<len(lst):
        if num==lst[i]:
            print("found here at pos", i+1)
            return True
        i=i+1
    print("not found")
    return False


@check_args
def search_for_loop(lst, num):
    """ 
    This function  with for loop will search 'num' in list 'lst'
    :param lst, num: 
    :return: Boolean 
    """
    for i in range(len(lst)):
        if num==lst[i]:
            print("found here at pos", i)
            return True
    return False
    


search_without_loop(lst,36)

search_while_loop(lst, 19)

search_for_loop(lst, 'f')
