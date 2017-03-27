"""
Merge Sort
1. use recursion to create small intervals
2. merge small intervals
"""

def merge_sort(lst):
    if len(lst)==1:
        return lst
    elif len(lst)==2:
        if lst[0]>lst[1]:
            return lst[::-1]
        else:
            return lst

    mid = len(lst)/2
    return merge(merge_sort(lst[:mid]),merge_sort(lst[mid:]))

def merge(lst1, lst2):
    i=0
    j=0
    k=0
    lst=[]
    while i<len(lst1) and j<len(lst2):
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            k+=1
            i+=1
        else:
            lst.append(lst2[j])
            k+=1
            j+=1
    if i<len(lst1):
        lst+=lst1[i:]
    elif j<len(lst2):
        lst+=lst2[j:]
    return lst
