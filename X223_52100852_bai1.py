import pandas as pd

df = pd.read_csv('iris.csv')

print(df.head(5))

print(df.describe().drop(['25%', '50%', '75%']))
