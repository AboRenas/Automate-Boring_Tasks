
import pandas as pd
import json
import os
from openpyxl.workbook import Workbook


folder_path = "C:/Users/HP/PycharmProjects/Automating_CSV_Excel and JSON/file_handling_demo"
os.makedirs(folder_path, exist_ok=True)

cvs_data = {
    "name":["kareem", "renas", "wala"],
    "age":[4, 6, 40],
    "country":["sudan","us", "egypt"]
}
csv_file = os.path.join(folder_path, "example.csv")
pd.DataFrame(cvs_data).to_csv(csv_file, index=False)

excel_data = {
    "product":["mouse", "mic", "laptop"],
    "price":[500,700,2800],
    "stock":[60,400,122]
}

excel_file = os.path.join(folder_path, "example.xlsx")
pd.DataFrame(excel_data).to_excel(excel_file, index=False)

json_data = {
    "student":[
        {"name": "Alan", "grade":"B"},
        {"name":"bob","grade":"C"},
         {"name":"tim","grade":"D"}
    ]
}
json_file = os.path.join(folder_path, "example.json")
with open(json_file, "w") as f:
    json.dump(json_data, f, indent=4)
   # f.close()
(csv_file, excel_file, json_file)