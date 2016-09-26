import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
matplotlib.style.use('ggplot')

#
# Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
path = "C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x.b/module3/Datasets/"
df = pd.read_csv(path + "wheat.data")


#
# Create a slice of your dataframe (call it s1)
# that only includes the 'area' and 'perimeter' features
# 
s1 = df.loc[:, ['area','perimeter']]


#
# Create another slice of your dataframe (call it s2)
# that only includes the 'groove' and 'asymmetry' features
# 
s2 = df.loc[:, ['groove','asymmetry']]


#
# Create a histogram plot using the first slice,
# and another histogram plot using the second slice.
# Be sure to set alpha=0.75
# 
matplotlib.style.use('ggplot')  # Look Pretty

s1.plot.hist(alpha=0.5)
plt.show()

s2.plot.hist(alpha=0.5)
plt.show()
