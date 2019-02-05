
"""An example of Insertion sort, O(n2)"""

def insertion_sort(listA):
    for i in range(1,len(listA)):

        curr_val=listA[i]
        pos=i

        while pos>0 and listA[pos-1]>curr_val:
                listA[pos]=listA[pos-1]
                pos=pos-1

        listA[pos]=curr_val

    return listA

listA=[45,14,34]
print(insertion_sort(listA))
