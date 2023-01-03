import pandas
from product.create_product import create_product

excel_data_df = pandas.read_excel(
    'sheets/outdoors.xlsx', sheet_name='baskets')

# print whole sheet data
data = excel_data_df.to_records()

print(len(data))

for row in data:
    index, id, name, desc, price, img_1, img_2, addr = row
    data = {
        "name": name,
        "type": "simple",
        "regular_price": str(price),
        "short_description": desc,
        "categories": [
            {
                "id": 229
            },
            {
                "id": 322
            }
        ],
        "images": [
            {
                "src": img_1
            }
        ]
    }
    print(data)
    create_product(data)
