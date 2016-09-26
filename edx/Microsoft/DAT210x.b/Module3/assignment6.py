import pandas as pd
import matplotlib.pyplot as plt


#
# Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
path = "C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x.b/module3/Datasets/"
df = pd.read_csv(path + "wheat.data")


#
# Drop the 'id' feature
# 
df.drop('id', axis=1, inplace=True)


#
# Compute the correlation matrix of your dataframe
# 
print(df.corr())


#
# Graph the correlation matrix using imshow or matshow
# 
plt.imshow(df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)


plt.show()


