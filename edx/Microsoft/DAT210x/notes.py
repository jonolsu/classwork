import pandas as pd
def week1():
    """
    1.0 the Big Picture

    out of the box machine learning types
        Supervised
            Classification (spam or not)
            Regression  
        Unsupervised  
            Clustering  
            Dimensionality Reduction (take lots of attributes and determine if it's good
                "Dimensionality reduction falls into the realm of unsupervised learning because you will not be the one telling the computer which features you want it build. Rather, it will infer this information automatically by examining your unlabeled data."
        Reinforcement learning (how to play and beat a video game, prioritizing set of actions that results in a reward or constraint) (Not in this class)
    """
    

def week2():
    """
    categorical features (not measured, usually discrete, textural in nature like flavors)
        broken down into nominal (non ordered -- red/green/blue) and ordinal (ordered -- grade A,B,C,D,F)
    continuous features (measurements like time)
    
    just because it's noisy, don't assume you don't collect or add it to your list
    don't throw out features until you do your analysis
    collect as much data as you can (volume on samples and features)
    use intuition about the domain of the question

    pandas has data frames and series
        So a series is basically an array-like structure.
        It can store any type of Python data type, ints, strings,
        floats, what have you.
        But the important thing about series is that they
        are homogeneous, so they can only store one type of data. 
    
    you should create categories for ordinal features .cat.codes
    you should encode nominal data to artificial categories as well, by default this will be alphabetical which is actually meaningless
    
    df.satisfaction = df.satisfaction.astype("category",
    ordered=True,
    categories=ordered_satisfaction
    ).cat.codes # creates a single column, but orders them according to what you've defined in ordered_satisfaction

    df['vertebrates'] = df.vertebrates.astype("category").cat.codes # creates a single column with an integer for each category
    df = pd.get_dummies(df,columns=['vertebrates']) # creates a column for each type in the feature, with a 1 or 0 -- better
    
    scitext uses bagofwords to create boolean features + counts out of text fields
    corpus = [
    "Authman ran faster than Harry because he is an athlete.",
    "Authman and Harry ran faster and faster.",
    ]
    bow = CountVectorizer()
    X = bow.fit_transform(corpus)
    uses a sparse matrix b/c it woudl create a tremendous amout of new features
    
    scipy can read in image files and create a feature for each pixel. usually scale colors to a float between 0 and 1.
    also consider shrinking image so the data inputs are not too large
    also consider converting to a black/white
    basically the same for audio encoding, but make sure your sampling frequency is the same for all music clips
    
    np.nan can help to represent missing data
    you can forward fill or backfill or interpolate between non missing points. or you can drop a record (or even a column if necessary)
    you might consider dropping duplicates as well
    sometimes there is also bogus data as when users are requied to enter something.  like a fake email.  requires closer inspection
    
    """
    df = pd.read_csv("C:/Users/jbennett02/Documents/Magic Briefcase/classwork/edx/Microsoft/DAT210x/Module2/Datasets/tutorial.csv")
    df.tail(2)
    df.head(2)
    df.columns
    df.describe()
    
    df.col0
    df['col0']
    df[['col0']]
    df.loc[:, 'col0']
    df.loc[:, ['col0']]
    df.iloc[:, 0]
    df.iloc[:, [0]]
    df.ix[:, 0]
    df.iloc[0:1, :]
    df.col0 < 0
    df[ df.col0 < 0 ]
    

#PCA is for linear reduction
# Isomap is for non linear reduction