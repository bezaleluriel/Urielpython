func2 = lambda x: x ** 2
print(func2(4))


def even(x):
    if x % 2 == 0:
        return True
    else:
        return False


l1 = [3, 6, 8, 9, 10, 7, 5]
# similiar to map, need to get condition of True/False and some list
newlist = filter(even, l1)
# better solution
newlist = filter(lambda x: x % 2 == 0, l1)
for i in newlist:
    print(i)

l1 = [3, 6, -8, 9, -10, 7, 5]
l2 = map(lambda x: -x, l1)
for i in l2:
    print(i)

# only x^2 of the negative numbers
l1 = [3, -6, 8, 9, -10, 7, -5]
l2 = map(lambda x: x ** 2, filter(lambda x: x < 0, l1))
print(list(l2))
