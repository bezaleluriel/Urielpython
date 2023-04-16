
#muliples board
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


