import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import assignment2_helper as helper
import numpy as np
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

# Look pretty...
matplotlib.style.use('ggplot')


# Do * NOT * alter this line, until instructed!
scaleFeatures = True


# Load up the dataset and remove any and all
# Rows that have a nan. You should be a pro at this
# by now ;-)
#
df = pd.read_csv("C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x/Module4/PCA/Datasets/kidney_disease.csv",
header=0, usecols = range(1,26))
df = df.replace({'?':np.nan}).dropna(axis=0)
df = df.dropna(axis=0)




# Create some color coded labels; the actual label feature
# will be removed prior to executing PCA, since it's unsupervised.
# You're only labeling by color so you can see the effects of PCA
labels = ['red' if i=='ckd' else 'green' for i in df.classification]


# Use an indexer to select only the following columns:
#       ['bgr','wc','rc']
#
#df = df[['bgr','wc','rc']]
#df.wc = df.wc.map(str.strip)
#df.wc = df.wc.astype(float)
#df.rc = df.rc.map(str.strip)
#df.rc = df.rc.astype(float)
df.pcv = df.pcv.astype(float)

df = pd.get_dummies(df,columns=['classification', 'rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane'])




# Print out and check your dataframe's dtypes. You'll probably
# want to call 'exit()' after you print it out so you can stop the
# program's execution.
#
# You can either take a look at the dataset webpage in the attribute info
# section: https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease
# or you can actually peek through the dataframe by printing a few rows.
# What kind of data type should these three columns be? If Pandas didn't
# properly detect and convert them to that data type for you, then use
# an appropriate command to coerce these features into the right type.
#
df.wc = df.wc.map(str.strip)
df.wc = df.wc.astype(float)
df.rc = df.rc.map(str.strip)
df.rc = df.rc.astype(float)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('bgr')
ax.set_ylabel('wc')
ax.set_zlabel('rc')
ax.scatter(df.bgr, df.wc, df.rc, c='red', marker='.')
fig = plt.figure()
print(df.describe())


# PCA Operates based on variance. The variable with the greatest
# variance will dominate. Go ahead and peek into your data using a
# command that will check the variance of every feature in your dataset.
# Print out the results. Also print out the results of running .describe
# on your dataset.
#
# Hint: If you don't see all three variables: 'bgr','wc' and 'rc', then
# you probably didn't complete the previous step properly.
#
df.var(axis=0)



# This method assumes your dataframe is called df. If it isn't,
# make the appropriate changes. Don't alter the code in scaleFeatures()
# just yet though!
#
# .. your code adjustment here ..
if scaleFeatures: df = helper.scaleFeatures(df)



# Run PCA on your dataset and reduce it to 2 components
# Ensure your PCA instance is saved in a variable called 'pca',
# and that the results of your transformation are saved in 'T'.
#
pca = PCA(n_components=2)
pca.fit(df)
T = pca.transform(df)

# Plot the transformed data as a scatter plot. Recall that transforming
# the data will result in a NumPy NDArray. You can either use MatPlotLib
# to graph it directly, or you can convert it to DataFrame and have pandas
# do it for you.
#
# Since we've already demonstrated how to plot directly with MatPlotLib in
# Module4/assignment1.py, this time we'll convert to a Pandas Dataframe.
#
# Since we transformed via PCA, we no longer have column names. We know we
# are in P.C. space, so we'll just define the coordinates accordingly:
ax = helper.drawVectors(T, pca.components_, df.columns.values, plt, scaleFeatures)
T = pd.DataFrame(T)
T.columns = ['component1', 'component2']
T.plot.scatter(x='component1', y='component2', marker='o', c=labels, alpha=0.75, ax=ax)
plt.show()

