# TO-DO: Complete the selection_sort() function below 
arr1 = [1, 5, 8, 4, 2, 9, 0, 6, 3, 7]


def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element starting from the current index
                            #Grabbing the smallest value from the current index
        while arr[cur_index] > min(arr[cur_index :]):
            # Set variable to index of smallest element
            smallest_index = arr.index(min(arr[cur_index :]))

        # Swap the item from the current index with 
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

            cur_index += 1


        # print("Arr", arr)


    return arr

# selection_sort(arr1)
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    1.#Loop through the array
    for i in range(len(arr) -2):
        # use i as current index
        current_index = i
        for j in range(len(arr) - 1):

        # check if current index is larget than its neighbor
            # if neighbor is smaller than current index 
            if  arr[j] > arr[j + 1]:
                print(f"before swap {arr}")

                # swap the two items
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"after swap {arr}")

    print("End", arr)
    return arr

bubble_sort(arr1)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr