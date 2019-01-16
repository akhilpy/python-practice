"""
This example remove the duplicate element from the list
"""

list_a=[1,2,3,4,4,5,7,2,5,6]

#solution 1
b = list(set(list_a)) # convert list into set, and it remove the duplicate elements 
print(b)

#Solution 2 

new_list=[]
for i in list_a:
    if i  not in new_list:
        new_list.append(i)

print(new_list) 

#solution 3  Using list comprihension
x=[]
[x.append(i) for i in list_a if  i not in x]
print(x)

#solution 4  Using dict comprihension

new_list ={i:1 for i in list_a}.keys()
print(list(new_list))



