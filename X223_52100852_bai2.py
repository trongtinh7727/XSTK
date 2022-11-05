import pandas as pd

df = pd.read_csv('population.csv')
df = df.drop(['Year'], axis=1)
print(df.head(5))
df = df.groupby(['Country Name', 'Country Code'])[
    'Value'].describe(percentiles=[])
print(df.to_string())
