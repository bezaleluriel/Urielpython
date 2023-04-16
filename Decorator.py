def make_pretty(func):
    def inner():
        print("i got decorated")
        func()
        print("return")
    return inner

@make_pretty
def regular():
    print('i am regular func')

# this line is what actually happens when we use @make_pretty
# regular = make_pretty(regular)

regular()

######################################

def smart_divide(func):
    def inner(a, b):
        if b == 0:
            return 0
        else:
            return func(a, b)
    return inner
@smart_divide
def divide(a, b):
    return a/b

print(divide(4, 2))
print(divide(4, 0))


##################################


