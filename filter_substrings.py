"""
    Filter all largest sting from the list, and remove all substring
    e.g 
    Input:-["ab", "bc", "abc", "ef", "fgh", "efgh"]
    Output:-['abc', 'efgh']
"""


import copy
listA = ["ab", "bc", "abc", "ef", "fgh", "efgh"]
listB=copy.deepcopy(listA) # create 2nd copy of main list 
new_list=[]
global longest_str 
longest_str = max(listA, key=len)
l_len=len(listA)
while l_len>0:
    for l in listB:
        if l in longest_str and len(l)<len(longest_str):
            listA.remove(l)  # remove the sub-string
        if longest_str == l:
            new_list.append(l) #append longest string in new_list
            listA.remove(l) #remove from the main list 
    l_len=len(listA)
    if l_len>0:
        longest_str=max(listA, key=len)

print(new_list)
