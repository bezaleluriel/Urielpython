from multiprocessing import *
import time
import os
from PIL import Image, ImageFilter

path = r'C:\Users\MHT\Urielpython\images'
def create_thumbnail(filename, size=(50,50), thumb_dir='thumbs'):
    img = Image.open(os.path.join(path, filename))
    img = img.filter(ImageFilter.GaussianBlur())
    img.thumbnail(size)
    img.save(f'{thumb_dir}/{os.path.basename(filename)}')
    print(f'{filename} was processed...')

tic = time.time()
for i in os.listdir(path):
    create_thumbnail(i)
toc = time.time()
print(tic-toc)

filenames = os.listdir(path)