# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def is_ascending(*args):
    # one line!!
    return all([args[i] >= args[i - 1] for i in range(1, len(args))])
    # multiple line!!!
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    lst = [4, 5, 6, 7]
    ans = is_ascending(lst)




    dict1 = {'a': 1, 'b': 31, 'c': 3}
    [print(f'{k} = {v}') for k, v in dict1.items()]







    # is monotonic ascending or descending
    lst = [8,7,5,9]
    print(all([lst[i] >= lst[i - 1] for i in range(1, len(lst))]) or all([lst[j] <= lst[j - 1] for j in range(1, len(lst))]))

    input()

    #is prime func
    number = int(input("enter number: "))
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("not primary")
            break
    # if the for loop ended without reaching the break
    else:
        print("primary number")

    input()





    # some tricks on 2 lists
    l1 = [4,5,6,7]
    l2 = [6,7,8,9]

    print(set(l1).intersection(l2))
    print(set(l1).union(l2))
    print(set(l1).difference(l2))
    print(set(l1).symmetric_difference(l2))
    print(set(l1).issubset(l2))
    print(set(l1).issuperset(l2))





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







    x = int(input("please enter number "))
    y = int(input("please enter number "))
    print(x) if x > y else print(y)


    x = input("enter your full name: ")
    first_name = x.split()[0]
    last_name = x.split()[1]
    first_name = first_name[0].upper() + first_name[1:]
    last_name = last_name[0].upper() + last_name[1:]
    print(f'{first_name} {last_name}')






    x = input('enter text: ')
    print(x == x[::-1])
    print(type(x))
    print(x.upper())
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
