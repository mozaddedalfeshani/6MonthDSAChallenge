arr = [1,3,5,2,45]
largestNumber = arr[0]
for item in arr:
    if largestNumber < item:
        largestNumber= item

print(largestNumber)