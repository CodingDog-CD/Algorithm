def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        print(data)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)


def partition(data, left, right):
    tmp = data[left]
    while left < right:
        while (data[right] >= tmp) and (left < right):
            right -= 1
        if left < right:
            data[left] = data[right]
        while (data[left] <= tmp) and (left < right):
            left += 1
        if left < right:
            data[right] = data[left]
    data[left] = tmp
    return left


test_list = [17, 6, 2, 4, 21, 34, 3, 8]
print(test_list)
quick_sort(test_list, 0, len(test_list)-1)
print(test_list)
