# data: input array, left: index of the first element, right: index of the last element, k: top k
def quick_sort(data, left, right, k):
    if left < right and left < k:
        mid = partition(data, left, right)
        print(data)
        quick_sort(data, left, mid - 1, k)
        quick_sort(data, mid + 1, right, k)


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


test_list = [17, 6, 8, 8, 21, 34, 4, 8]
k = 2
print(test_list)
quick_sort(test_list, 0, len(test_list)-1, k)
print("k=", k, ": ", test_list)
