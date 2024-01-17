import numpy as np
import pandas as pd

df=pd.read_csv("first.csv")
#print(df)
#print(df.head()) 
#print(df.tail(5))
#print(df.index)
#print(df.columns)
#print(df.describe)
#print(df.sort_values(by="per",ascending=False))
print(df.T)