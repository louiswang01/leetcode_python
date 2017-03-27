"""
Quick Sort
1. pick pivot
2. partition on pivot
3. use recursion to quick sort two partitions
"""

def qs_helper(lst):
    if len(lst)<=1:
        return lst
    pivot=lst[0]
    left=1
    right=len(lst)-1
    while right>left:
        if lst[left] > pivot:
            temp=lst[right]
            lst[right]=lst[left]
            lst[left]=temp
            right-=1
        else:
            left+=1
    if lst[right] < pivot:
        lst[0]=lst[right]
        lst[right]=pivot
        
    return qs_helper(lst[:right]) + \
        qs_helper(lst[right:])
    
