from turtle import color
from PIL import Image
import numpy as np
####
import matplotlib.pyplot as plt
import cv2


###tser4_t0003.BMP    https://ru.stackoverflow.com/questions/1145128/Как-преобразовать-jpg-в-массив-numpy

i = Image.open('tser4_t0000.BMP')#.convert('RGB')
#print(i)
iar = np.asarray(i)
img = iar.copy()
print(iar[1].shape)
print(iar.dtype)
cv2.imwrite("filearr.png", iar)
#print(img)
img[img < 100 ] = 0
img[img >= 100 ] = 1
#print(np.shape(iar))
x= np.unique(iar).size
print(iar.size)
b = plt.imshow(img, cmap= 'gray')
plt.colorbar(b)
plt.show()
plt.yscale("log")
#per = np.percentile(iar, 100)
#print(per)
#plt.axvline(per, color = "black")
#plt.semilogy()
z = plt.hist(iar.ravel(),256, [0,256])
plt.xlabel('элемент', fontsize=16)
plt.ylabel('частота', fontsize=16)
plt.show()


