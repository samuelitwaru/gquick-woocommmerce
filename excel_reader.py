import pandas as pd
from upload_product import upload_product
import numpy as np

# read by default 1st sheet of an excel file
xls = pd.ExcelFile('sheets/cosmetics.xlsx')
dataframe1 = pd.read_excel(xls, 'lotions')
df1 = dataframe1.replace(np.nan, '', regex=True)

csv = dataframe1.to_csv()
json = dataframe1.to_json()
dict = dataframe1.to_dict()
recs = dataframe1.to_records()

for rec in recs:
    index, id, name, desc, price, img_1, img_2, addr = rec
    if np.isnan(id):
        data = {
            "name": name,
            "type": "simple",
            "regular_price": str(price),
            "short_description": desc,
            "description": "",
            "categories": [
                {
                    "id": 228
                },
                {
                    "id": 295
                }
            ],
            "images": [
                {
                    "src": img_1
                }
            ]
        }

        # print(data)
        # print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

        upload_product(data.status)
