def findSumArry(arr, k):
    sum = 0
    for i in range(k):
        sum += arr[i]

    currentSum = sum

    for i in range(k, len(arr)):
        currentSum += arr[i] - arr[i - k]
        if currentSum > sum:
            sum = currentSum

    return sum

arr1 = [1, 4, -1, 2, 3]
print("#1 example:",findSumArry(arr1, 3))

arr2 = [1, 4, -1, 2, 3]
print("#2 example:",findSumArry(arr2, 2))
