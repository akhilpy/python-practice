"""Solution 1"""

def josephus(ls, skip):

    idx = skip
    while len(ls) > 1:
        ls.pop(idx)
        idx = (idx + skip) % len(ls)

    print ('survivor: ', ls[0])

ls=range(1,11)
skip=1
josephus(list(ls), skip)




"""Solutution 2"""
# def josephus2(n, k): 
  
#       if (n == 1): 
#           return 1
#       else: 
      
      
#           # The position returned by  
#           # josephus(n - 1, k) is adjusted 
#           # because the recursive call 
#           # josephus(n - 1, k) considers 
#           # the original position  
#           # k%n + 1 as position 1  
#           return (josephus2(n - 1, k) + k-1) % n + 1
  
# # Driver Program to test above function 
  
# n = 10
# k = 2
  
# print("The surviver ", josephus2(n, k)) 

