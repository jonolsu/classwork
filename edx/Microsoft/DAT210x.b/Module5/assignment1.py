#
# Import whatever needs to be imported to make this work
#
from datetime import datetime
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


matplotlib.style.use('ggplot') # Look Pretty


#
# TODO: To procure the dataset, follow these steps:
# 1. Navigate to: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2
# 2. In the 'Primary Type' column, click on the 'Menu' button next to the info button,
#    and select 'Filter This Column'. It might take a second for the filter option to
#    show up, since it has to load the entire list first.
# 3. Scroll down to 'GAMBLING'
# 4. Click the light blue 'Export' button next to the 'Filter' button, and select 'Download As CSV'



def doKMeans(df):
  #
  # INFO: Plot your data with a '.' marker, with 0.3 alpha at the Longitude,
  # and Latitude locations in your dataset. Longitude = x, Latitude = y
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.scatter(df.Longitude, df.Latitude, marker='.', alpha=0.3)

  #
  # Filter df so that you're only looking at Longitude and Latitude,
  # since the remaining columns aren't really applicable for this purpose.
  #
  dataframe = df[['Longitude', 'Latitude']]

  #
  # Use K-Means to try and find seven cluster centers in this df.
  #
  kmeans_model = KMeans(n_clusters=7)
  kmeans_model.fit(dataframe)

  #
  # INFO: Print and plot the centroids...
  centroids = kmeans_model.cluster_centers_
  ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)
  print centroids



#
# Load your dataset after importing Pandas
#
df = pd.read_csv("C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x.b/Module5/Datasets/Crimes_-_2001_to_present.csv",
header=0)


#
# Drop any ROWs with nans in them
#
df = df.dropna(axis=0)


#
# Print out the dtypes of your dset
#
print(df.dtypes)


#
# Coerce the 'Date' feature (which is currently a string object) into real date,
# and confirm by re-printing the dtypes. NOTE: This is a slow process...
#
df.Date = pd.to_datetime(df.Date)


# INFO: Print & Plot your data
doKMeans(df)


#
# Filter out the data so that it only contains samples that have
# a Date > '2011-01-01', using indexing. Then, in a new figure, plot the
# crime incidents, as well as a new K-Means run's centroids.
#
keepdates = df.Date > '2011-01-01'
df = df[keepdates]




# INFO: Print & Plot your data
doKMeans(df)
plt.show()


