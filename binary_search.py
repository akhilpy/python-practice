"""Binary Search  program in python"""

data=[3,5,2,7,4,9,6]
data.sort(reverse=False) # Rule 1- List should be sorted before performing Binary search

def binary_search(data,n):
    lower_bound=0
    upper_bound=len(data)-1
    
    while lower_bound<=upper_bound:
        
        mid = (lower_bound+upper_bound)//2 

        if data[mid]==n:
            print("value found at sorted position", mid)
            return True
        else:
            if n>data[mid]:
                lower_bound=mid+1
            else:
                upper_bound=mid-1
    print("not found in list")
    return False

binary_search(data, 4)