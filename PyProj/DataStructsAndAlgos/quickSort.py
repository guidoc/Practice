#### QUICK SORT ####
"""
Schema of the algorithm

Vect1  3 5 2 1 14 6 4 8 7

Pick a pivot (usually the last element)
We want to put this element at right place
and keep at the left all the smaller elements and at the right all the bigger elements

so the update would be like
[3 5 2 1 4 6] 7 [14 8]

and then we run quick sort on each of the 2 parts

"""

def quickSort(arr):
    # init counters
    pivotId = len(arr) - 1
    arrId = 0

    # put the pivot at the right place and keep at the left smaller els and at the right bigger els
    while pivotId > arrId:
        # if pivot is smaller we switch things around
        if arr[pivotId] < arr[arrId]:
            temp = arr[arrId]
            arr[arrId] = arr[pivotId-1]
            arr[pivotId-1] = arr[pivotId]
            arr[pivotId] = temp
            pivotId -= 1
        else:
            arrId += 1

    # run quick sort on the left and right portion
    if pivotId > 0: arr[:pivotId] = quickSort(arr[:pivotId])
    if pivotId+1 < len(arr): arr[pivotId+1:] = quickSort(arr[pivotId+1:])

    return arr


if __name__ == '__main__':
    v = [3,5,2,1,14,6,4,8,7]
    vs = quickSort(list(v))
    print v
    print vs













def partition(vect, low, high):

    i = low - 1
    pivot = vect[high]

    for j in range(low, high):
        if vect[j] <= pivot:
            i += 1
            vect[i], vect[j] = vect[j], vect[i]

    vect[i+1], vect[high] = vect[high], vect[i+1]
    return i+1



def quickSort(vect):

    pivotId = len(vect)


