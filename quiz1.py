def finValue(arr):
    maxValue = arr[0]
    beforeMaxValue = None

    for num in arr:
        if num > maxValue:
            beforeMaxValue = maxValue
            maxValue = num
        elif beforeMaxValue is None or num > beforeMaxValue:
            beforeMaxValue = num

    return maxValue, beforeMaxValue

arr1 = [-1, 4, 30, 2, -4]
arr2 = [ 3, 4, 5, 6, 7 ]
arr3 = [ 3, 4, 5, 6, 7, 7 ]

#1 example:
maxValue, beforeMaxValue = finValue(arr1)
print("#1 example max:", maxValue)
print("#1 example before max:", beforeMaxValue)

#2 example:
maxValue, beforeMaxValue = finValue(arr2)
print("#2 example max:", maxValue)
print("#2 example before max:", beforeMaxValue)

#3 example:
maxValue, beforeMaxValue = finValue(arr3)
print("#3 example before max:", beforeMaxValue)


