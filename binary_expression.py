"""This example convert the binary string expression0 to  int and calculate the result """

stri = '101+100-110*101010/101'

total_count = 0

for i ,j in enumerate(stri):
   if j in "+-/*":
      total_count=total_count+1
res=[]
k=0
c=0
# for i,j in enumerate(stri):
#     if j in "+-/*":      # count the total mathematical expression 
#         total_count = total_count + 1

for i, j in enumerate(stri):
   if j in "+-/*":
      res.append(str(int(stri[k:i],2)))
      res.append(j)
      k=i+1
      c=c+1
   if c ==total_count:
      res.append(str(int(stri[i+1:],2)))
      c=c+1
   
print(res)
print(eval(('').join(res)))

# result = []
# k=0
# count = 0
# for i,j in enumerate(stri):
#     if j in "+-/*":
#        result.append(str(int(stri[k:i],2)))  # Get the binary expression  and convert into INT and append in the Result list

#        result.append(j) # Append the mathematical expression in Result list
#        k = i+1 
#        count = count+1 

#     if count == total_count: 
#        result.append(str(int(stri[i+1:],2))) # Append the last binary expression in the Result List
#        count = count+1

# print(result) #The complete list of Int value and mathematical expression in the order of given string.

# print(eval(('').join(result))) # Join the list and eval() the Result.