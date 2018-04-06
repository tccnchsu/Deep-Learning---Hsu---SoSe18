# Python Imaging Library/ conda install -c anaconda scipy/
# http://www.scipy-lectures.org/advanced/image_processing/
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.colors import NoNorm
import pylab
from scipy import misc
import numpy as np

#http://scikit-image.org/docs/dev/user_guide/transforming_image_data.html
#im_image = np.uint8(100*np.ones((28, 28)))
#im_image =100.*np.ones((28,28), dtype=np.float32)

im_image =100*np.ones((28,28), dtype=np.uint8)
im_image[1:3, 1:3] = 200
plt.subplot(211)
#plt.gray()
#plt.imshow(im_image , cmap='gray', norm=NoNorm())
plt.imshow(im_image , cmap=pylab.gray() , norm=NoNorm())
#plt.imshow(im_image , cmap=plt.cm.gray, norm=NoNorm())
#plt.show()

plt.imsave('C:/pythonwork/images/Pimage1.png', im_image) # uses the Image module (PIL)
#convert image (np.array) to binary image
#https://stackoverflow.com/questions/40449781/convert-image-np-array-to-binary-image
im_label=im_image<120  
#im_label=np.zeros((28,28), dtype=bool)
#im_label[1:3, 1:3] =np.array([[True, True] , [True, True]])
plt.subplot(212)
plt.imshow(im_label , cmap=plt.cm.binary)
plt.show()
plt.imsave('C:/pythonwork/labels/Plabel1.png', im_label) # uses the Image module (PIL)


# Store data to disk, and load it again:
#>>> np.save('/tmp/123', np.array([[1, 2, 3], [4, 5, 6]]))
#>>> np.load('/tmp/123.npy')
#array([[1, 2, 3],
#       [4, 5, 6]])

#arr = np.array(img) transform image to array
#arr = img.load() load array
#a=np.ones(10, dtype=bool)
#https://matplotlib.org/users/image_tutorial.html
#https://stackoverflow.com/questions/3823752/display-image-as-grayscale-using-matplotlib/11603881






