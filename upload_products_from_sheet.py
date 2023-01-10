import pandas
import numpy as np
from product.create_product import create_product

excel_data_df = pandas.read_excel(
    'sheets/accessories.xlsx', sheet_name='phone-holders')


excel_data_df = excel_data_df.replace({np.nan: None})


# print whole sheet data
data = excel_data_df.to_records()


for row in data:
    index = row[0]
    id = row[1]
    name = row[2]
    desc = row[3]
    price = row[4]
    img_1 = row[5]
    img_2 = row[6]
    addr = row[7]

    if not id:
        data = {
            "name": name,
            "type": "simple",
            "regular_price": str(price),
            "short_description": desc,
            "categories": [
                {
                    "id": 269
                },
                {
                    "id": 348
                },
            ],
            "images": [
                {
                    "src": img_1
                }
            ]
        }

        if isinstance(img_2, str):
            data['images'].append(
                {
                    "src": img_2
                }
            )
            # print(data['images'])

        create_product(data)
