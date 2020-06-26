import pandas as pd

df = pd.read_csv("dataset\All\Mtech.csv",index_col=0)

mandi = df[df['City']=='Mandi']
print(mandi)