def merge_sort(input_array):
    while len(input_array) > 1:
        mid = len(input_array)//2
        array_1 = merge_sort(input_array[0:mid])
        array_2 = merge_sort(input_array[mid:len(input_array)])
        return merge(array_1, array_2)
    return input_array


def merge(array_1, array_2):
    ind_1 = 0
    ind_2 = 0
    merged_array = []
    # print(array_1)
    # print(array_2)
    while ind_1 < len(array_1) and ind_2 < len(array_2):
        if array_1[ind_1] < array_2[ind_2]:
            merged_array.append(array_1[ind_1])
            ind_1 += 1
        else:
            merged_array.append(array_2[ind_2])
            ind_2 += 1
    while ind_1 < len(array_1):
        merged_array.append(array_1[ind_1])
        ind_1 += 1
    while ind_2 < len(array_2):
        merged_array.append(array_2[ind_2])
        ind_2 += 1
    return merged_array


testArray = [23, 12, 31, 10, 78, 3, 6, 28, 35]
sortedArray = merge_sort(testArray)
print(sortedArray)
