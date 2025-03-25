# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

# odd=0
# even =0

# for i in range(len(arr)):

#     if(i%2==0):
#         even +=arr[i]
#     else:
#         odd+=arr[i]

# print(odd, even)

# for i in range(5):
#     print("*")
#     for j in range(0, i):
#         print("* ",end="")

# unArranged = [12, 5, 33, 20, 8, 47, 25, 14, 39, 2, 50, 17, 29, 3, 41, 9, 35, 26, 22, 11, 44, 7, 18, 42, 31, 1, 30, 48, 6, 46, 19, 36, 24, 4, 21, 49, 28, 16, 15, 40, 32, 10, 43, 34, 27, 23, 37, 45, 13, 38]


# newValue = sorted(unArranged,)
# print(newValue)


unArrangedValues =[(12, 'c', "string"), (5, 'c', "string"), (33, 'c', "string"), (20, 'c', "string"), (8, 'c', "string"), (47, 'c', "string"), (25, 'c', "string"), (14, 'c', "string"), (39, 'c', "string"), (2, 'c', "string"), (50, 'c', "string"), (17, 'c', "string"), (29, 'c', "string"), (3, 'c', "string"), (41, 'c', "string"), (9, 'c', "string"), (35, 'c', "string"), (26, 'c', "string"), (22, 'c', "string"), (11, 'a', "string"), (44, 'c', "string"), (7, 'c', "string"), (18, 'c', "string"), (42, 'c', "string"), (31, 'c', "string"), (1, 'c', "string"), (30, 'c', "string"), (48, 'c', "string"), (6, 'c', "string"), (46, 'c', "string"), (19, 'c', "string"), (36, 'c', "string"), (24, 'c', "string"), (4, 'c', "string"), (21, 'c', "string"), (49, 'c', "string"), (28, 'c', "string"), (16, 'c', "string"), (15, 'c', "string"), (40, 'c', "string"), (32, 'c', "string"), (10, 'c', "string"), (43, 'c', "string"), (34, 'c', "string"), (27, 'c', "string"), (23, 'c', "string"), (37, 'c', "string"), (45, 'c', "string"), (13, 'c', "string"), (38, 'c', "string")]



newValues = sorted(unArrangedValues, key=lambda x:x[1])
print(newValues)