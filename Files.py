
#muliples board
import csv
import os.path
import re

# f = open('multiples_board.txt', 'w')
#
# for x in range(1,11):
#     for y in range(1,11):
#         f.write(f'{y*x} ')
#     f.write('\n')
# f.close()
#
# #names inputs
# names = []
# f = open('names.txt', 'a', encoding='utf-8')
# for _ in range(5):
#     f.write(input('enter name') + '\n')
#
# f.close()


# all times from file to file
f = open(r'Z:\___advanced python\01.txt', 'r')
g = open('times.txt', 'w')
time_pattern = '\d{2}:\d{2}:\d{2}'
x = re.findall(time_pattern, f.read())
f.close()
g.write('\n'.join(x))
g.close()


#csv
with open(r'Z:\___advanced python\movies.csv', 'r+', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i in reader:
        if i['title'] == 'Black Mirror':
            print(i['movieId'])

# #csv
# with open(r'Z:\___advanced python\movies.csv', 'a+', encoding='utf-8', newline='') as f:
#     writer = csv.DictReader(f,fieldnames=['movieId', 'title', 'geners'])
#     writer.writerow({'movieId':'99999', 'title':'moti abu', 'geners':'education'})


#all txt files from dextop to one file in my project
desktop = r'C:\Users\MHT\Desktop'
with open('all_files_from_desktop.txt', 'w') as w_file:
    for i in os.listdir(desktop):
        if i.endswith('.txt'):
            with open(os.path.join(desktop,i)) as f:
                w_file.write(f.read() + '\n')



