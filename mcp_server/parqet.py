import pandas as pd 

draft = pd.read_csv("data/sample.csv")

draft.to_parquet("data/sample.parquet",index=False)