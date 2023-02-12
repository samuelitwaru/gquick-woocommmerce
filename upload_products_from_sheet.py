import pandas
import numpy as np
from product.create_product import create_product

excel_data_df = pandas.read_excel(
    'sheets/selfcare.xlsx', sheet_name='accessories')


excel_data_df = excel_data_df.replace({np.nan: None})


# print whole sheet data
data = excel_data_df.to_records()


ids = ''

categories = [420,

              ]

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
            "status": "publish",
            "categories": [],
        }
        if img_1:
            data["images"] = [
                {
                    "src": img_1,
                    "name": f'{name}-0'
                }
            ]
            if isinstance(img_2, str):
                data['images'].append(
                    {
                        "src": img_2,
                        "name": f'{name}-1'
                    }
                )
        else:
            data["status"] = "pending"

        for category in categories:
            data["categories"].append({"id": category})

        print('>>>>>>>>', name)

        # print(data['images'])
        data = create_product(data)
        print(data)
        ids += (f"{data['id']}\n")
        print(ids)
