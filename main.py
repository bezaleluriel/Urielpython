# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math


def is_ascending(*args):
    # one line!!
    return all(args[i] <= args[i+1] for i in range(len(args)-1))
    # multiple lines!!!
    # last = args[0]
    # is_ascending = True
    # for i in range(1, len(args)):
    #     if args[i] >= last:
    #         last = args[i]
    #         continue
    #     else:
    #         is_ascending = False
    #         break
    # return is_ascending

def is_descending(*args):
    return all(args[i] >= args[i + 1] for i in range(len(args) - 1))


# ascending or descending
def is_monotonic(*args):
    return is_ascending(args) or is_descending(args)
   # return all([args[i] >= args[i - 1] for i in range(1, len(args))]) or all([args[j] <= args[j - 1] for j in range(1, len(args))])


def if_splitted_element_len_is_2_so_flip_the_values(lst1):
    # for s in lst1:
    #     if len(s.split(' ')) == 2:
    #         bla = reversed(s.split(' '))
    #         print(' '.join(bla))

    # with 1 line
    print([' '.join(reversed(s.split(' '))) for s in lst1 if len(s.split()) == 2])


if __name__ == '__main__':

    # # This will print the result of dividing 9 by 4 as a floating point number -> 2.25
    # print(9 / 4)
    # # This will print the result of dividing 9 by 4 using integer division, which discards the remainder -> 2
    # print(9 // 4)
    #
    # # Prompt user to enter text and store it in variable x as string
    # x = input('enter text: ')
    # # Check if x is equal to its reversed version (i.e., is it a palindrome?) and print the result
    # print(x == x[::-1])
    # # Print the data type of x
    # print(type(x))
    # # Convert x to uppercase and print the result
    # print(x.upper())
    # # Convert the first letter of each word in x to uppercase and print the result
    # print(x.capitalize())

    # # Prompt user to enter their full name and store it in variable x
    # x = input("enter your full name: ")
    # # Split the full name into first and last name using the split() method and store them in separate variables
    # first_name = x.split()[0]
    # last_name = x.split()[1]
    # # Capitalize the first letter of the first name and last name, and concatenate the rest of the name
    # first_name = first_name[0].upper() + first_name[1:]
    # last_name = last_name[0].upper() + last_name[1:]
    # # Print the formatted first and last name with a space in between
    # print(f'{first_name} {last_name}')
    #
    # # in one line!!! - Split the full name into first and last name using the split() method,
    # # capitalize the first letter of each name, and concatenate them using list comprehension!!
    # first_name, last_name = [name.capitalize() for name in x.split()]
    #
    # # another example of list comprehension:
    # # List comprehensions can also include conditions that filter the elements of the iterable based on some criteria
    # # Here's an example that generates a list of even numbers between 0 and 9:
    # evens = [x for x in range(10) if x % 2 == 0]
    #
    # x = int(input("please enter number "))
    # y = int(input("please enter number "))
    # print(x) if x > y else print(y)


    # # using all function
    # #The all function takes an iterable and returns True if all elements in the iterable are truthy, and False otherwise
    # lst = [4, 5, 5, 6, 7]
    # ans = is_ascending(lst)
    # print(ans)




    # num = 13
    # if num < 2:
    #     print('not primary')
    # for i in range(2, int(math.sqrt(num) + 1)):
    #     if num % i == 0:
    #         print('not primary')
    #         break
    # # cool feature of python! if the for loop ended properly..
    # else:
    #     print('primary')
    # # in 1 line!!
    # print("primary") if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)) and num > 1 else print(
    #     "not primary")

    # # Reverses the order of two-word strings in lst1 and prints them.
    # s = 'aa bb,ccc dddd,eee,f ff ff,jjj hh'
    # lst_s = list(s.split(','))
    # if_splitted_element_len_is_2_so_flip_the_values(lst_s)

    # lst = [4, 3, 2, 1]
    # ans = is_ascending(lst)
    # # is ascending or descending
    # ans2 = is_monotonic(lst)

    # # This code will print out each key-value pair in the dict1 dictionary using a list comprehension
    # dict1 = {'a': 1, 'b': 31, 'c': 3}
    # [print(f'{k} = {v}') for k, v in dict1.items()]



    # # some tricks on 2 lists
    # l1 = [4,5,6,7]
    # l2 = [6,7,8,9]
    # # find the common elements between two lists
    # print(set(l1).intersection(l2))
    # # combine two lists and remove any duplicates
    # print(set(l1).union(l2))
    # # find the elements that are unique to one list and not present in another list
    # print(set(l1).difference(l2))
    # # find the elements that are unique to either list
    # print(set(l1).symmetric_difference(l2))
    # # checks is subset
    # print(set(l1).issubset(l2))
    # # a set is a collection of unique elements, while a superset is a set that contains all the elements of another set.
    # print(set(l1).issuperset(l2))





    str = 'hello world'
    # use a dictionary comprehension to count the letter frequencies
    # in dict comprehension to return key:value the syntax is x : y
    letter_count = {char : str.count(char) for char in str}
    # print the letter count dictionary
    print(letter_count)






    dict1 = {'name': 'uriel', 'age': 31, 'is_student': False}

    # dictionary comprehension
    dict1 = {k:None for k in dict1.keys()}
    [print(f'{k} = {v}') for k, v in dict1.items()]

    dict1 = {'name': 'uriel', 'age': 31, 'is_student': False}
    # cool way of unpacking
    [print(f'{k} = {v}') for k, v in dict1.items()]
    #another cool way
    print('\n'.join([f'{k} = {v}' for k, v in dict1.items()]))

    # is ascending 1 line, create boolean list and do magic
    lst = [3,4,5,6,7]
    print(all([lst[i] >= lst[i-1] for i in range(1, len(lst))]))



    # all x^2 when x is 1-10.
    print([x**2 for x in range(1,11)])



    lst = [4, 5, 6, 1]
    # even_lst = []
    # for i in lst:
    #     if i % 2 == 0:
    #         even_lst.append(i)
    # print(even_lst)

    # list comprehension
    print([item for item in lst if item % 2 == 0])










    lst = [4, 5, 6 , 7]
    last = lst[0]
    is_ascending = True
    for i in range(1 , len(lst)):
        if lst[i] >= last:
            last = lst[i]
            continue
        else:
            is_ascending = False
            break
    print(is_ascending)

















