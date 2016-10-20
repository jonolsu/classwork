import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from scipy import misc
import scipy.io.wavfile as wavfile
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris
from pandas.tools.plotting import parallel_coordinates
from pandas.tools.plotting import andrews_curves
import numpy as np
from sklearn.decomposition import PCA
from sklearn import manifold
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#to install packages in pycharm, go to terminal and activate the conda environment and then install
# > activate StandardAnaconda27
# > conda install matplotlib

def module1():
    """
    Notes on module 1
    """

    # Data Analytics Steps
    #   1. Collecting
    #   2. Wrangling
    #   3. Exploring
    #   4. Transforming
    #   5. Modelling
    #   6. Evaluating
    #   7. Intelligence and/or go back to step 1

    # With supervised learning, there is a label or 'correct answer' that is expected. Due to
    # this, the computer 's job is to formulate an algorithm that produces that correct answer, given the input data.
    # With unsupervised learning, there is no answer / label, so the computer's only job is to come up
    # with interesting facts about the data.

    # Focus on engineering machine learning algorithms
    # 1. classification (like spam or not spam, provide examples of both with known output) -- Supervised
    # 2. regression (find relationship between variables) -- Supervised
    # 3. clustering (group similar records) - Unsupervised
    # 4. dimensionality reduction (reduce complex data set small subset of important factors) -- Unsupervised
    # 5. reinforcement leanring (how to play video games) -- not in this class
    print("only notes, no python code")



def module2():
    """
    Notes on module 2
    """

    # Continuous Features (measurable in value)
    # Categorical Features (isn't a measurable difference, usually discrete, textural in nature)
    #   a) Nominal (unordered) -- ie, colors, names, car models
    #   b) Ordinal (ordered) -- ie, age buckets, high/med/low, happy/unhappy

    # collect as many features as possible, even if noisy, because sometimes combining features makes for a
    # strong indicator

    # collect as much data as you can so the algorithms can converge.  More samples is better.

    # use your intuition and subject matter expertise

    # The only unbreakable rule is that you need to ensure you collect as many features and samples as you possibly can.
    # If you ever become unsure which one of the two you should focus on more, concentrate on collecting more samples.

    # There are no hard and fast rules when it comes to thinking up good features for your samples; but a rule does
    #  exist about what to avoid: garbage. If you collect details about your samples that you know is statistically
    #  irrelevant to the domain of the problem you're trying to solve, you'll only be wasting your time and eroding
    #  the accuracy of your analysis. Garbage in, garbage out

    # pandas data types:
    #   1) series -- homogneous
    #   2) data frame  -- collation of series stacked together, mimicks R data frame

    # columns = attributes = views = features depending on the context

    # in pandas axis=1 is the column/feature

    path = "C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x.b/module2/Datasets/"

    # df = pd.read_csv(path + "tutorial.csv")
    df = pd.read_csv(path + "direct_marketing.csv")

    print("df.head(5)")
    print (df.head(5))
    print ("df.tail(5)")
    print (df.tail(5))
    print ("df.describe()")
    print (df.describe())
    print ("df.columns")
    print (df.columns)
    print ("df.index")
    print (df.index)
    print ("df.dtypes")
    print (df.dtypes)

    # other ways to create data frames

    # Slicing Columns
    df.recency
    df['recency']
    df[['recency']]
    df.loc[:, 'recency']
    df.loc[:, ['recency']]
    df.iloc[:, 0]
    df.iloc[:, [0]]
    df.ix[:, 0]
    df.recency < 7

    # Once you're ready to move to a production environment, Pandas documentation recommends
    #  you use either .loc[], .iloc[], or .ix[] data access methods, which are more optimized.
    #  The .loc[] method selects by column label, .iloc[] selects by column index, and .ix[]
    #  can be used whenever you want to use a hybrid approach of either. All code in this course
    #  will use either the df.recency or df[['recency', ...]] data-access syntax styles for maximum clarity.

    # Slicing Rows
    df[0:2]
    df.iloc[0:2, :]
    df.recency < 7
    df[df.recency < 7]
    df[(df.recency < 7) & (df.newbie == 0)]

    # Slicing Rows and Columns
    df.loc[0:2,['recency','mens','womens']]

    # my_dataframe.columns = ['new', 'column', 'header', 'labels']

    # other ways to create data frames
    # my_dataframe.to_sql('table', engine)
    # my_dataframe.to_excel('dataset.xlsx')
    # my_dataframe.to_json('dataset.json')
    # my_dataframe.to_csv('dataset.csv')

    # you can map ordinal data using the astype
    # notice what happens when the mapping can't be made (maps to -1)
    ordered_satisfaction = ['Very Unhappy', 'Unhappy', 'Neutral', 'Happy', 'Very Happy']
    df2 = pd.DataFrame({'satisfaction': ['Mad', 'Happy', 'Unhappy', 'Neutral']})
    df2.satisfaction = df2.satisfaction.astype("category",
                                               ordered=True,
                                               categories=ordered_satisfaction
                                               ).cat.codes

    # mapping
    df3 = pd.DataFrame({'vertebrates': [
        'Bird',
        'Bird',
        'Mammal',
        'Fish',
        'Amphibian',
        'Reptile',
        'Mammal',
    ]})

    df3['vertebrates'] = df3.vertebrates.astype("category").cat.codes # will map alphabetically (faster/easier)
    df3 = pd.DataFrame({'vertebrates': [
        'Bird',
        'Bird',
        'Mammal',
        'Fish',
        'Amphibian',
        'Reptile',
        'Mammal',
    ]})

    df3 = pd.get_dummies(df3, columns=['vertebrates']) # will map with boolean indicator features (preferred)

    # Bag of Words Model
    # "featurize" a body of text
    corpus = ["Authman ran faster than Harry because he is an athlete.",
              "Authman and Harry ran faster and faster.",
              ]
    bow = CountVectorizer()
    X = bow.fit_transform(corpus) # Sparse Matrix
    bow.get_feature_names()
    X.toarray()

    # Featurize images
    # you can read in each pixel and store the luminosity
    img = misc.imread(path + "ILTQq.png")
    print (type(img))
    print (img.shape, img.dtype)
    img = img[::2,::2] #shrink
    img = (img/255.0).reshape(-1,3) #change to float values, RGB
    red = img[:,0]
    green = img[:,1]
    blue = img[:,2]
    gray = (0.299*red + 0.587*green + 0.115*blue) #grayscale magic numbers
    print(img.shape)
    print(gray.shape)
    # now you can do machine learning on the gray

    # audio encoding is similar to visual encoding.  Audio stored as an array of samples, so encode each sample but
    # make sure each audio file has the same sample feature rate
    sample_rate, audio_data = wavfile.read(path + "chimes.wav")
    print (audio_data)
    # do machine learning on audio_data

    # Wrangling Data
    # missing values, redacted, not collected, mechanical failure, doesn't even exist
    # np.nan behaves slightly differently than python's NAN
    df.isnull()
    df.notnull()
    df.fillna(0) #fill all with a scalar value
    df.spend.fillna(df.spend.mean()) #fill a feature with average of the feature
    df.fillna(method='ffill', limit=1) #forward fill like GPS coordinates of a trip, can also backfill
    df.interpolate(method='polynomial', order =2) #interpolate
    #drop all rows with holes
    df.dropna(axis=0)
    #drop all columns with holes
    df.dropna(axis=1)
    # drop duplicates, where the unique key is a subset of the features
    #print df.drop_duplicates(subset=['Major_category', 'Total']).reset_index()

    #coerce
    # df.Date = pd.to_datetime(df.Date, errors='coerce')
    # df.Height = pd.to_numeric(df.Height, errors='coerce')
    # df.Weight = pd.to_numeric(df.Weight, errors='coerce')
    # df.Age = pd.to_numeric(df.Age, errors='coerce')

    #unique
    df.DM_category.unique()

    #counts
    df.DM_category.value_counts()

def module3():
    """
    Notes on module 3
    """

    # The Seven Basic Tools of Quality: https://en.wikipedia.org/wiki/Seven_Basic_Tools_of_Quality

    #Histogram
    path = "C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x.b/module3/Datasets/"
    df = pd.read_csv(path + "wheat.data")
    matplotlib.style.use('ggplot')  # Look Pretty
    df.asymmetry.plot.hist(title='Asymmetry', bins=10)
    plt.show()

    #2D scatterplot
    df.plot.scatter(x='area', y='perimeter')
    plt.show()

    #3D scatterplot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('area')
    ax.set_ylabel('perimeter')
    ax.set_zlabel('asymmetry')
    ax.scatter(df.area, df.perimeter, df.asymmetry, c='r', marker='.')
    plt.show()

    #Parallel Coordinates -- higher dimensionality visualizations
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target_names'] = [data.target_names[i] for i in data.target]
    # Parallel Coordinates Start Here:
    plt.figure()
    parallel_coordinates(df, 'target_names')
    plt.show()

    #Andrews curve
    plt.figure()
    andrews_curves(df, 'target_names')
    plt.show()

    #correlation plot
    df = pd.DataFrame(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])
    print(df.corr())
    plt.imshow(df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
    plt.colorbar()
    tick_marks = [i for i in range(len(df.columns))]
    plt.xticks(tick_marks, df.columns, rotation='vertical')
    plt.yticks(tick_marks, df.columns)

def module4():
    """
    Notes on module 4
    """

    #make sure features are independent, discriminating, informative
    #  make sure all features have been properly transformed
    #  changes either number of features or feature values
    #  doesn't alter the number of samples of dataset
    #  wrangling out NAN, label encoding of categorical labels, normalization, standardization -> preprocessor transformers
    #  applied early on.  Next transformers are a different type.  performed right before modeling, not at beginning

    #principal component analysis (PCA) unsupervised dimensionality reduction algorithm
    #PCA takes in dataset and spits out uncorrelated linerly independent features
    #  step 1 -> finds center of data (mean)
    #  step 2 -> find direction of maximum variance (which direction)
    #  step 3 -> find all directions that are orthagonal to all other directions
    #  step 4 -> all new principal components added to list to form brand new feature space which is a linear translation
    #            or original feature space
    # scores each feature set by variance.
    #
    # An iterative approach to this would first find the center of your data, based off its numeric features.
    # Next, it would search for the direction that has the most variance or widest spread of values.
    # That direction is the principal component vector, so it is then added to a list.
    # By searching for more directions of maximal variance that are orthogonal to all previously computed vectors,
    # more principal component can then be added to the list. This set of vectors form a new feature space that you can
    # represent your samples with.
    #
    #PCA, and in fact all dimensionality reduction methods, have three main uses:
    # To handle the clear goal of reducing the dimensionality and thus complexity of your dataset.
    # To pre-process your data in preparation for other supervised learning tasks, such as regression and classification.
    # To make visualizing your data easier, since we can only perceive three dimensions simultaneously.
    #
    #One warning is that again, being unsupervised, PCA can't tell you exactly know what the newly created components or features mean.
    #
    #PCA is a very fast algorithm and helps you vaporizes redundant features,
    # so when you have a high dimensionality dataset, start by running PCA on it and then visualizing it.
    # This will better help you understand your data before continuing.
    #
    #weakness of PCA
    # 1) sensitive to feature scaling since it's measuring variance. works best if all quantites are of
    # same metric.  normalize before feeding into PCA.
    # 2) PCA is slow if dataset is too big.  use randomized PCA if this becomes an issue
    # 3) linear translation -- won't discern non-linear variances.  must use ISO Map in this case


    #PCA
    path = "C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x/Module4/PCA/Datasets/"
    df = pd.read_csv(path + "kidney_disease.csv")
    df = df.loc[:,['age','bp','sg','al','su']]
    df = df.interpolate(method='polynomial', order=2)
    pca = PCA(n_components=2)
    pca.fit(df)
    PCA(copy=True, n_components=2, whiten=False)
    T = pca.transform(df)
    print(df.shape)
    print(T.shape)

    #Isomap
    # creates a neighborhood . . .nearest neighbors.
    # as dataset increases in non-linearity isomaps helps.  bends, curves
    # tracking something moving, high correlation between data points.  handwritten digits.
    # finds a series of nearest neighbors and maps the path
    # Isomap is better than linear methods when dealing with almost all types of real image and motion tracking
    # So long as the underlying relationship is non-linear, another area isomap tends excel at is the grouping
    #   and identifying of similar variations in similar data samples. Due to this, it is extremely useful as a
    #   preprocessor step before conducting supervised learning tasks, such as classification or regression.
    # Finally, isomap's benefits also include all the other reasons you would use PCA or any other dimensionality
    #   reduction technique, including visualization and data compression.
    # Slower than PCA
    # Transformations are irreversible
    # Isomap is also a bit more sensitive to noise than PCA. Noisy data can actually act as a conduit to
    #  short-circuit the nearest neighborhood map, cause isomap to prefer the 'noisy' but shorter path
    #  between samples that lie on the real geodesic surface of your data that would otherwise be well separated.
    # When using unsupervised dimensionality reduction techniques, be sure to use the feature scaling on all
    #  of your features because the nearest-neighbor search that Isomap bases your manifold on will do poorly
    #  if you don't, and PCA will prefer features with larger variances.

    #Isomap (Isometric Feature Mapping)
    path = "C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x/Module4/PCA/Datasets/"
    df = pd.read_csv(path + "kidney_disease.csv")
    df = df.replace({'?': np.nan}).dropna(axis=0)
    df = df.dropna(axis=0)
    df.pcv = df.pcv.astype(float)
    df = pd.get_dummies(df,columns=['classification', 'rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane'])
    iso = manifold.Isomap(n_neighbors=4, n_components=2)
    iso.fit(df)
    manifold.Isomap(eigen_solver='auto', max_iter=None, n_components=2, n_neighbors=4,
           neighbors_algorithm='auto', path_method='auto', tol=0)
    manif = iso.transform(df)
    print(df.shape)
    print(manif.shape)
    print(manif)

def module5():
    """
    Notes on module 5
    """

    #Data Modeling
    #

    df = pd.DataFrame(np.random.randn(100, 2) * 1.1, columns=['x', 'y'])
    df.append = (pd.DataFrame(np.random.randn(100, 2) * 0.9, columns=['x', 'y']))
    df.append = (pd.DataFrame(np.random.randn(100, 2) * 1.5, columns=['x', 'y']))
    df.append = (pd.DataFrame(np.random.randn(100, 2) * 0.5, columns=['x', 'y']))
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(df)
    KMeans(copy_x=True, init='k-means++', max_iter=300, n_clusters=4, n_init=10,
           n_jobs=1, precompute_distances='auto', random_state=None, tol=0.0001,
           verbose=0)
    labels = kmeans.predict(df)
    centroids = kmeans.cluster_centers_
    df.plot.scatter(x='x', y='y')
    plt.show()

def main():
    #print("\nModule 1")
    #module1()
    #print("\nModule 2")
    #module2()
    #print("\nModule 3")
    #module3()
    #print("\nModule 4")
    #module4()
    print("\nModule 5")
    module5()
if __name__ == '__main__':
    main()