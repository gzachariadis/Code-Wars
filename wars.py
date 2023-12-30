def move_zeros(array):
    return [x for x in array if x!=0] + [0] * array.count(0)

# def move_zeros(lst):
#     for x in lst:
#         if int(x) == int(0):
#             lst.append(lst.pop(lst.index(x)))
#     return lst


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
print(move_zeros([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]))
