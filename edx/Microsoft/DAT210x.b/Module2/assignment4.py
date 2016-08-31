import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
df = pd.read_html("http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2",header=1)[0]


# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..
new_columns = df.columns.values
new_columns[13] = 'PP_G'
new_columns[14] = 'PP_A'
new_columns[15] = 'SH_G'
new_columns[16] = 'SH_A'
df.columns = new_columns


# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..
df = df.dropna(axis=0, thresh=4)

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
df = df[df['PLAYER'] <> 'PLAYER']

# TODO: Get rid of the 'RK' column
#
# .. your code here ..
df = df.drop(labels=['RK'], axis=1)

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
df = df.reset_index(drop=True)


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
df.dtypes
df.GP = pd.to_numeric(df.GP, errors='coerce')
df.G = pd.to_numeric(df.G, errors='coerce')
df.A = pd.to_numeric(df.A, errors='coerce')
df.PTS = pd.to_numeric(df.PTS, errors='coerce')
df["+/-"] = pd.to_numeric(df["+/-"] , errors='coerce')
df.PIM = pd.to_numeric(df.PIM, errors='coerce')
df["PTS/G"] = pd.to_numeric(df["PTS/G"], errors='coerce')
df.SOG = pd.to_numeric(df.SOG, errors='coerce')
df.PCT = pd.to_numeric(df.PCT, errors='coerce')
df.GWG = pd.to_numeric(df.GWG, errors='coerce')
df.PP_G = pd.to_numeric(df.PP_G, errors='coerce')
df.PP_A = pd.to_numeric(df.PP_A, errors='coerce')
df.SH_G = pd.to_numeric(df.SH_G, errors='coerce')
df.SH_A = pd.to_numeric(df.SH_A, errors='coerce')


# TODO: Your dataframe is now ready! Use the appropriate
# commands to answer the questions on the course lab page.
print(len(df))
print(len(df.PCT.unique()))
print(sum(df[15:17]['GP']))