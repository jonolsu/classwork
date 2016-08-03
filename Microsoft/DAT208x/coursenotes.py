import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

year = [1950, 1970, 1990, 2010]
population = [2.519, 3.692, 5.263, 6.972]

population = [1.0,1.262,1.650] + population
year = [1800, 1850, 1900] + year

plt.plot(year,population)
plt.show()
#plt.xscale('log')
plt.fill_between(year, population,0,color='green')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B'])
plt.show()

plt.scatter(year,population,s=np.array(population)*20)

histvals = histvals = random.sample(range(1,1000),20)
plt.hist(histvals, bins = 4)
plt.show()
plt.clf()


#other settings:
#plt.grid(True)
#plt.text(xcoord,ycoord,"c") # adds text to xy coordinate
#plt.scatter(year,population,s=np.array(population)*20,c=col, alpha = 0.8) #where col is a list of colors and alpha is

#PANDAS
# abc = pd.read_csv("path/file.csv",index_col = 0)
# abc["colname"] #to select column
# abc.colname #to select column
# abc["hello"] = [1,2,3,4,5] #to create new column
# abc.hello = abc.hello/1000 #based on numpy, so element-wise reference of columns
# abc.loc["BR"] #to reference a row named "BR"
# abc.loc["BR"].hello # to reference a cell
# abc.loc["hello"].loc["BR"] # to reference a cell
# abc.loc["BR","hello"] # to reference a cell
# cars['cars_per_cap'] #data series
# cars[['cars_per_cap']] #data frame
# cars.loc[['AUS',"EG"]] # return data frame with two columns
# print(cars.loc[['MOR','RU'],['country','drives_right']]) #returns data frame of two columns for two obeservations