def insertion_sort(arr):
    if arr is None:
        return None
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j = j -1
    return arr
if __name__ == '__main__':
    arr = [2, 8, 5, 3, 9, 4]
    #arr = []
    sorted_arr = insertion_sort(arr)
    sorted_arr1 = insertion_sort(sorted_arr)
    print(sorted_arr1)
