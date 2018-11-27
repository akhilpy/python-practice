data =[43,54,23,22,65,54,44]

def selection_sort(data):
   
    for n in range(len(data)-1):
        minpos=n
        for i in range(n, len(data)):
            if data[i]<data[minpos]:
                minpos=i
        
        temp =  data[n]
        data[n]=data[minpos]
        data[minpos]=temp
        
    return data

print(selection_sort(data))
