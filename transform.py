import pandas as pd


def clean_data(df):
    # Split data column into separate five separate columns
    df[['brand', 'model', 'colors', 'price', 'additional info']] = df['data'].str.split('\n', expand=True)

    # Extract original and discounted prices
    df[['original price', 'discounted price']] = df['price'].str.replace('$', '').str.split(' ', expand=True)

    # Drop the first two but now redundant columns
    df1 = df.drop(['data', 'price'], axis=1)

    # Clean colors column and dropping unnecessary rows
    df1['colors'] = df1['colors'].str.replace(' colors', '')
    rows_mis_info = df1['colors'].str.strip().str.contains('\\$', na=False)
    df1 = df1[~rows_mis_info]

    # Filling empty values with the string 'REGULAR' in additional info column
    df1['additional info'] = df1['additional info'].fillna('REGULAR')

    # Removing the ' , ' sign in original & discounted price column and convert into numeric
    df1['original price'] = df1['original price'].str.replace(',', '').str.strip()
    df1['discounted price'] = df1['discounted price'].str.replace(',', '').str.strip()
    df1['original price'] = pd.to_numeric(df1['original price'], errors='coerce')
    df1['discounted price'] = pd.to_numeric(df1['discounted price'], errors='coerce')

    # Removing empty original price rows
    df1.dropna(subset=['original price'], inplace=True)

    # Calculating two new columns discount amount and discount %
    df1['discount amount'] = df1['original price'] - df1['discounted price']
    df1['discount amount'] = df1['discount amount'].fillna(0)
    df1['discount %'] = (df1['discount amount'] / df1['original price']) * 100
    df1['discount %'] = df1['discount %'].fillna(0)

    # Removing any rows in model colum with $ sign
    row_mis_info_2 = df1['model'].str.contains('\\$')
    df2 = df1[~row_mis_info_2]
    df2 = df2.drop_duplicates()

    # Function returning dictionary to be loaded into MongoDB
    return df2.to_dict(orient='records')
