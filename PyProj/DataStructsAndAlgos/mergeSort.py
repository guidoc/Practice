#### MERGE SORT ####
"""
Schema of the algorithm

Vect1  3 5 2 1 14 6 4 8 7

Split until I get vectors of 1 or 2 elements

(3 5 2 1 14)            (6 4 8 7)
(3 5 2) (1 14)          (6 4) (8 7)
(3 5) (2) (1 14)          (6 4) (8 7)

Sort each vector
(3 5) (2) (1 14)          (4 6) (7 8)


Merge
(2 3 5) (1 14).     (4 6 7 8)
"""

def mergeSort(vect):
    # split until is len 1
    if len(vect) > 1:
        mid = len(vect)/2
        left = mergeSort(vect[:mid])
        right = mergeSort(vect[mid:])

        # merge the vectors
        l = r = 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                vect[l+r] = left[l]
                l += 1
            else:
                vect[l+r] = right[r]
                r += 1

        # finish the copy
        while l < len(left):
            vect[l+r] = left[l]
            l += 1
        while r < len(right):
            vect[l+r] = right[r]
            r += 1

    # return the sorted vector
    return vect




def mergeSort2(arr):
    # base case
    if len(arr) == 1:
        return arr

    # split the array into 2 and run merge sort on them
    l = len(arr)
    arr1 = mergeSort(arr[:l/2])
    arr2 = mergeSort(arr[l/2:])

    # combine the 2 arrays
    i = j = 0
    while i < len(arr1) and j in len(arr2):
        if arr1[i] <= arr2[j]:
            arr[i+j] = arr1[i]
            j += 1
        else:
            arr[i+j] = arr2[j]
            i += 1

    while i < len(arr1):
        arr[i+j] = arr1[i]
        i += 1

    while j < len(arr2):
        arr[i+j] = arr2[j]
        j += 1

    return arr










if __name__ == '__main__':
    v = [3,5,2,1,14,6,4,8,7]
    vs = mergeSort(list(v))
    print v
    print vs



























