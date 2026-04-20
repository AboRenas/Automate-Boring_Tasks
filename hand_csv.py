import pandas as pd

df_csv = pd.read_csv("example.csv")
print("CSV DATA:\n",df_csv)

df_csv.to_csv("ouput.csv", index=False)