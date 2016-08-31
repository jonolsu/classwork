import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from scipy import misc
import scipy.io.wavfile as wavfile

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

def main():
    print("\nModule 1")
    module1()
    print("\nModule 2")
    module2()



if __name__ == '__main__':
    main()