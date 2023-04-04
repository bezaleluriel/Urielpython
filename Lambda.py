from functools import reduce

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

# find the longest word
text = "welcome to israel and have a good time"
print(reduce(lambda x, y: x if len(x) > len(y) else y, text.split()))

# find the number that x^2 is biggest
l1 = [3, -6, 8, 9, -10, 7, -5]
print(reduce(lambda x, y: x if x**2 > y**2 else y, l1))



# using generator compehension '()' instead of list comprehension '[]' - return sum of each element
my_list = [123, 45, 678]
# Define a generator comprehension that applies a lambda function to each element in the input list
# The lambda function converts each element to a string, then iterates over its digits and sums them up
# The resulting iterator of sums is converted to a list using the list() function
digit_sum_list = list(map(lambda x: sum(int(d) for d in str(x)), my_list))
print(digit_sum_list)  # Output: [6, 9, 21]