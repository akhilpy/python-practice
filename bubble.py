
data = [2,4,3,67,43,23,7]

def bubble_sort(data):
    for n in range(len(data)-1,0,-1):
        for i in range(n):
            if data[i]<data[i+1]:
                temp=data[i]
                data[i]=data[i+1]
                data[i+1]=temp
    
    return data

print(bubble_sort(data))