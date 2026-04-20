import pandas as pd

df_excel = pd.read_excel("example.xlsx")

print("Exce Data:\n", df_excel)

df_excel.to_excel("output.xlsx", index=False)

