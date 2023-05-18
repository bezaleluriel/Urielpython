import sys

import numpy

size = 1_000_000
lst = list(range(size))
print("list size {}".format(len(lst) * sys.getsizeof(lst[-1]))) # 28000000

# each number is in the same size of 28 bytes!! it's bad, therefore we want to use numpy
# for i in range(1000):
#     print(i, sys.getsizeof(lst[i]))

import numpy as np

# much better
arr = numpy.arange(size)
print("array size {}".format(arr.size * arr.itemsize)) # 4000000


#ex1 3,4,15,16
a = np.arange(18)
a = a.reshape(3,6)
print(a)
print(a[::2 ,  3:5])

#ex2 Fancy indexing
mat = np.arange(12).reshape((3, 4))
print(mat)
rows = np.array([2,0,1])
colms = np.array([1,1,1])
print(mat[rows, colms])

rows = np.array([2, 2, 1, 1])
cols = np.array([0, 1, 0, 1])
print(mat[rows, cols])


import matplotlib.pyplot as plt
import random
fig = plt.figure()
x = ['a', 'b', 'c', 'd']
y = [random.randint(10, 20) for i in range(4)]
plt.plot(x ,y)
plt.show()


import pandas as pd
dice1 = pd.Series([np.random.randint(1, 7) for i in range(100)])
dice2 = pd.Series([np.random.randint(1, 7) for i in range(100)])

df = pd.DataFrame({"dice1": dice1, "dice2": dice2})

# Specify the file path where you want to save the CSV file
file_path = "dices.csv"

# Save the DataFrame to a CSV file
df.to_csv(file_path)

# Count the number of double cases
double_cases = (df["dice1"] == df["dice2"]).sum()
print(double_cases)

# second is bigger
sec_bigger_cases = (df["dice1"] > df["dice2"]).sum()
print(sec_bigger_cases)



# Read the CSV file
df = pd.read_csv(r'Z:\___advanced python\movies.csv')

# Group the data by genres and count the movies in each genre
genre_counts = df.groupby('genres').size().reset_index(name='count')

# Print the genre counts
print(genre_counts)

# Sort the genre counts in descending order
sorted_genre_counts = genre_counts.sort_values('count', ascending=False)

# Print the top 3 genres
top_3_genres = sorted_genre_counts.head(3)
print(top_3_genres)