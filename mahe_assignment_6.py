import pandas as pd

# 6a
df = pd.read_csv('./data/cereal.csv')

# 6b
honey_df = df[df["name"].str.contains("Honey")]
print(honey_df)

# 6c
honey_rice_df = df[(df["name"].str.contains("Honey") | df["name"].str.contains("Rice"))]
print(honey_rice_df)
