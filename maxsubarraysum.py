"""

"""



def maxsubarraysum(a, size):
    max_so_far= a[0]
    current_max=a[0]

    for i in range(1,size):
        current_max = max(a[i], current_max+a[i])
        max_so_far= max(max_so_far, current_max)

    return max_so_far


a =[-2,3,5,-1,4,-3]
print(maxsubarraysum(a, len(a)))


def maxsubarraysum(a, size):
    max_so_far= 0
    max_end_here=0
    start=0
    end=0
    s=0

    for i in range(0,size):
        max_end_here = max_end_here+a[i]
        if max_end_here<0:
            max_end_here=0
            s = i+1
        elif(max_so_far<max_end_here):
            max_so_far= max_end_here
            start =s
            end=i 


        # current_max = max(a[i], current_max+a[i])
        # max_so_far= max(max_so_far, current_max)
    print(start, end)
    return max_so_far


a =[-2,3,5,-1,4,-3]
print(maxsubarraysum(a, len(a)))