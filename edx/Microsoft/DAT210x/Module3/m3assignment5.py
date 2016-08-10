import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import parallel_coordinates
from pandas.tools.plotting import andrews_curves

# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
df = pd.read_csv("C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x/Module3/Datasets/wheat.data",
header=0, usecols = range(1,9))


#
# TODO: Drop the 'id', 'area', and 'perimeter' feature
# 
df.drop('area', axis=1, inplace=True)
df.drop('perimeter', axis=1, inplace=True)



#
# TODO: Plot a andrews curve chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
plt.figure()
andrews_curves(df, 'wheat_type', alpha = 0.4)

plt.show()

df = pd.read_csv("C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x/Module3/Datasets/wheat.data",
header=0, usecols = range(1,9))
plt.figure()
andrews_curves(df, 'wheat_type', alpha = 0.4)

plt.show()

