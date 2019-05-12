# The algorithm divides the input list into two parts: 
# the sublist of items already sorted, which is built up from left 
# to right at the front (left) of the list, and the sublist of items 
# remaining to be sorted that occupy the rest of the list. 
# Initially, the sorted sublist is empty and the unsorted sublist is 
# the entire input list. The algorithm proceeds by finding the smallest 
# (or largest, depending on sorting order) element in the unsorted 
# sublist, exchanging (swapping) it with the leftmost unsorted element 
# (putting it in sorted order), and moving the sublist boundaries one 
# element to the right.

myArray = [7, 3, -1, 0, 9, 2, 4, 6, 5, 8]

def selectionSort(array):

    if len(array) <= 1:
        print("array length is 1 or less")
        return array

    unsortedIndex = 0
    endOfArrayIndex = len(array)

    while unsortedIndex < endOfArrayIndex:
        print(f"starting another iteration of the while loop; unsortedIndex: {unsortedIndex}")

        # find smallest value in unsorted array 
        smallestValue = array[unsortedIndex]
        smallestValueIndex = unsortedIndex
        for index in range(unsortedIndex, endOfArrayIndex):
            if array[index] < smallestValue:
                smallestValue = array[index]
                smallestValueIndex = index
                print(f"smallestValue found: {smallestValue} and index: {smallestValueIndex}")

        # swap the smallest value with leftmost value 
        if array[smallestValueIndex] < array[unsortedIndex]:   
            swap(unsortedIndex, smallestValueIndex, array)

        print(f"result so far: {array}")
        unsortedIndex += 1

    print(array)
    return array

# i & j are indices of numbers to swap
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

selectionSort(myArray)