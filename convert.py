import pandas as pd
import json
import os

from hand_csv import df_csv
from handle_xlsx import df_excel

df_csv = pd.read_csv('example.csv')
df_csv.to_excel("converted_from_csv.xlsx", index=False)

df_excel = pd.read_excel("example.xlsx")
df_excel.to_json("converted_from_json.json", orient="records",indent=4)

print("Automation completed:")