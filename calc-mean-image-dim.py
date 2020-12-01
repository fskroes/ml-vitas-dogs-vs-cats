import numpy as np
import cv2 as cv
import os
import pandas as pd
print(os.listdir("/Users/fskroes/dev/vitas/notebooks/dogs-vs-cats/input/data/train")) # ../input


filenames = os.listdir("/Users/fskroes/dev/vitas/notebooks/dogs-vs-cats/input/data/train")
categories = []
for filename in filenames:
    category = filename.split('.')[0]
    if category == 'dog':
        categories.append(1)
    else:
        categories.append(0)

df = pd.DataFrame({
    'filename': filenames,
    'category': categories
})



## example how to get dimensions of image
img = cv.imread('/Users/fskroes/dev/vitas/notebooks/dogs-vs-cats/input/data/train/'+filenames[0])
print(img.shape)

h, w, c = img.shape
print('width:  ', w)
print('height: ', h)
print('channel:', c)



heights = []
widths = []
for filename in filenames:
    img = cv.imread('/Users/fskroes/dev/vitas/notebooks/dogs-vs-cats/input/data/train/'+filename)
    h, w, _ = img.shape
    heights.append(h)
    widths.append(w)

## Create DF and get height and width of image in filenames array and add to dataframe
new_df = pd.DataFrame({
    'h': heights,
    'w': widths
})

## Calculate the mean of the dataframe
new_df.mean(axis = 0)