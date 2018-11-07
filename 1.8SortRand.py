import random

def Rand(start,end,num):
    res = []

    for j in range(num):
        res.append(random.randint(start,end))
        print(res[j])

    print("po sortowaniu")
    return res

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

num = 10
start = 0
end = 50



result = Rand(start,end,num)
result.sort(key=int)
for i in range(9):
    print(result[i])

unsorted_list = result
sorted_list = merge_sort(unsorted_list)
print("po merge sort")
for i in range(9):
    print(sorted_list[i])
