# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
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
