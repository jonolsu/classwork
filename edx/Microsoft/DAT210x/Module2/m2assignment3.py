import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
df = pd.read_csv("C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x/Module2/Datasets/servo.data",
header=None)
df.columns = ['motor', 'screw', 'pgain', 'vgain', 'class']


# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..

df_vgain5 = df[df['vgain'] == 5]
print(len(df_vgain5))


# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
df_motorE = df[df['motor'] == 'E']
df_motorscrewE = df_motorE[df_motorE['screw'] == 'E']
print(len(df_motorscrewE))


# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#

df_pgain4 = df[df['pgain'] == 4]
print((df_pgain4["vgain"]).mean())



# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!



