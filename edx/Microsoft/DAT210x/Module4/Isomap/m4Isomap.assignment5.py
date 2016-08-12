import numpy as np
import random
import pandas as pd
import os
import scipy
from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
from sklearn import manifold

# Look pretty...
matplotlib.style.use('ggplot')

#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#

samples = []
directory = 'C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x/Module4/Isomap/Datasets/ALOI/32'
files = os.listdir(directory)
for filename in files:
    img = scipy.misc.imread(directory + '/' + filename)
    samples = samples + [img.flatten()]
directory = 'C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x/Module4/Isomap/Datasets/ALOI/32i'



#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
files = os.listdir(directory)
for filename in files:
    img = scipy.misc.imread(directory + '/' + filename)
    samples = samples + [img.flatten()]
df = pd.DataFrame(samples)


#
# TODO: Convert the list to a dataframe
#
colors = np.array(["b", "r"])
colors = np.repeat(colors, [72, 12], axis=0)

df = pd.DataFrame(samples,colors)


#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#

iso = manifold.Isomap(n_neighbors=6, n_components=3)
iso.fit(df)

#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#

T = iso.transform(df)
x,y,z=T.transpose(1,0)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x,z)
plt.show()

#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
x,y,z=T.transpose(1,0)
ax.scatter(x, y, z, c=colors, marker='.')
plt.show()




