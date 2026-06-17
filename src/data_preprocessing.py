import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def split_features_target(df):
    X = df.drop("price", axis=1).values
    y = df["price"].values
    return X, y