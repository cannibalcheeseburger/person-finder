import pandas as pd

df = pd.read_csv("dataset\All\lll.csv")

for column in df.columns:
    if df[column].dtypes == "object":
        df[column] = df[column].str.strip()

df.to_csv("dataset\All\cleaned.csv",index = False)