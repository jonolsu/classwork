import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
df = pd.read_csv("C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x/Module3/Datasets/wheat.data",
header=0, usecols = range(1,8))


#
# TODO: Create a 2d scatter plot that graphs the
# area and perimeter features
# 

matplotlib.style.use('ggplot')
s1 =df[['area','perimeter']]
s1.plot.scatter(x='area',y='perimeter')




#
# TODO: Create a 2d scatter plot that graphs the
# groove and asymmetry features
# 
# .. your code here ..
s2 =df[['groove','asymmetry']]
s2.plot.scatter(x='groove',y='asymmetry')
#
# TODO: Create a 2d scatter plot that graphs the
# compactness and width features
# 

s3 =df[['compactness','width']]
s3.plot.scatter(x='compactness',y='width')



# BONUS TODO:
# After completing the above, go ahead and run your program
# Check out the results, and see what happens when you add
# in the optional display parameter marker with values of
# either '^', '.', or 'o'.


plt.show()


