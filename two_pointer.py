def pointer(num,target):
    i = 0
    j = len(num) -1
    while i < j:
        sum_point = num[i] + num[j]
        if (sum_point == target):
            return [i , j]
        if (sum_point < target):
            i+= 1
        elif(sum_point > target):
            j-= 1
    return

a = [3,2,4]
find = 9
result = pointer(a,find)
print(result)