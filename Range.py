def range(n):
    i=0
    while i<n:
        i+=1
        yield i

for i in range(5):
    print(i)