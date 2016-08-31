import pandas as pd
import numpy as np

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
path = "C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x.b/module2/Datasets/"
featurenames =['motor', 'screw', 'pgain', 'vgain', 'class']
df = pd.read_csv(path + "servo.data", header=None, names=featurenames)

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the
# length of (# of samples in) that slice:
#
# .. your code here ..
dfv5 = df[df.vgain == 5]
print(len(dfv5))


# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
dfE = df[(df.motor == 'E') & (df.screw == 'E')]
print(len(dfE))



# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..
dfP4 = df[df.pgain == 4]
print(np.mean(dfP4.vgain))


# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
print (df.dtypes)