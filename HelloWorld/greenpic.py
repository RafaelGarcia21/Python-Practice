# Rafael Garcia
# Feb 27 2018
# This program prints a picture green


import matplotlib.pyplot as plt
import numpy as np

img = input("Enter name of the input file:")  # Read in image from csBridge.png
plt.imshow(img)  # Load image into pyplot
plt.show()  # Show the image (waits until closed to continue)

img2 = img.copy()  # make a copy of our image
img2[:, :, 1] = 1  # Set the blue channel to 0

plt.imshow(img2)  # Load our new image into pyplot
plt.show()  # Show the image (waits until closed to continue)

plt.imsave('reds.png', img2)  # Save the image we created to the file: reds.png
