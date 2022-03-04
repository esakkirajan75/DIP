#Creating checkerboard pattern-fourmethods
import numpy as np
import matplotlib.pyplot as plt
img1=np.zeros([4,4])
img2=np.zeros([4,4])
img3=np.zeros([4,4])
img4=np.zeros([4,4])
img3[1::2,::2]=1
img3[::2,1::2]=1
for i in range(0,4):
    for j in range(0,4):
        img1[i,j]=(-1)**(i+j)
        img2[i,j]=np.exp(1j*np.pi*(i+j))
        img4[i,j]=(i+j)%2
plt.subplot(2,2,1),plt.imshow(img1,cmap='gray')
plt.subplot(2,2,2),plt.imshow(img2,cmap='gray')
plt.subplot(2,2,3),plt.imshow(img3,cmap='gray')
plt.subplot(2,2,4),plt.imshow(img4,cmap='gray')