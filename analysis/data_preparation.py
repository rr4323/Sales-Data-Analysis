import data_collection

#Data Preparation
'''
1 Data Inspection: 
    We'll start by inspecting the dataset to see if there are any missing values, duplicates, or inconsistent data. We'll also check if the data types are correct and make sure the dataset is ready for analysis.

2 Data Cleaning: 
    Next, we'll clean the dataset by removing or correcting any errors, inconsistencies, or irrelevant information. This will make the dataset more reliable and accurate.

3 Data Transformation: 
    After cleaning the dataset, we may need to transform the data to make it more useful for analysis. This can include scaling, normalization, or feature engineering.

4 Data Saving: 
    Once we've prepared the data, we'll save it in a new file to avoid overwriting the original dataset. This way, we can always go back to the original dataset if we need to.

'''
pd=data_collection.pd
df=data_collection.df
print(df.shape)

# Check for missing values
def check_missing_values(dataframe):
    return dataframe.isnull().sum()

print(check_missing_values(df))
print(df[df.rating_count.isnull()])
# Remove rows with missing values in the rating_count column
df.dropna(subset=['rating_count'], inplace=True)
print(check_missing_values(df))


# Check for duplicates
def check_duplicates(dataframe):
    return dataframe.duplicated().sum()

print(check_duplicates(df))

# Check data types
def check_data_types(dataframe):
    return dataframe.dtypes

print(check_data_types(df))
print(df['actual_price'])
pd.set_option('display.max_columns', None)  # This sets the option to display all columns
print(df.head())

df['discounted_price'] = df['discounted_price'].astype(str).str.replace('₹', '').str.replace(',', '').astype(float)
df['actual_price'] = df['actual_price'].astype(str).str.replace('₹', '').str.replace(',', '').astype(float)
df['discount_percentage'] = df['discount_percentage'].astype(str).str.replace('%','').astype(float)/100

# The rating column has a value with an incorrect character, so we will exclude
# the row to obtain a clean dataset.
count = df['rating'].str.contains('\|').sum()
print(f"Total rating cloumn which contains | in value: {count}")
df = df[df['rating'].apply(lambda x: '|' not in str(x))]
count = df['rating'].str.contains('\|').sum()
print(f"Total rating cloumn which contains | in value: {count}")

df['rating'] = df['rating'].astype(str).str.replace(',', '').astype(float)
df['rating_count'] = df['rating_count'].astype(str).str.replace(',', '').astype(float)

print(check_data_types(df))

'''
rating_weighted" because it can be created as a way of considering not only the average rating, 
but also the number of people who rated the product.
This column weighs the average rating by the number of ratings, giving more weight to ratings with a large number of raters.
'''
# Creating the column "rating_weighted"
df['rating_weighted'] = df['rating'] * df['rating_count']

'''
 convert the 'category' column to a string type and then using the str.split('|') 
 method to split the string into a list based on the '|' character. 
 Finally, it's extracting the last element (str[-1]) to create a 'sub_category' column and the first element (str[0]) to create a 'main_category' column.
'''

df['sub_category'] = df['category'].astype(str).str.split('|').str[-1]
df['main_category'] = df['category'].astype(str).str.split('|').str[0]

print(df.columns)
print(len(df))