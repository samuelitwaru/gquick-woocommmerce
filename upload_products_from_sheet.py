import pandas
import numpy as np
from product.create_product import create_product

excel_data_df = pandas.read_excel(
    'sheets/accessories.xlsx', sheet_name='watches')


excel_data_df = excel_data_df.replace({np.nan: None})


# print whole sheet data
data = excel_data_df.to_records()


ids = ''

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
                    "id": 382

                },
            ],
            "images": [
                {
                    "src": img_1,
                    "name": f'{name}-0'
                }
            ]
        }
        print(data)
        print('>>>>>>>>', name)

        if isinstance(img_2, str):
            data['images'].append(
                {
                    "src": img_2,
                    "name": f'{name}-1'
                }
            )
            # print(data['images'])
        data = create_product(data)
        print(data)
        ids += (f"{data['id']}\n")
        print(ids)


'''
ACCESSORIES: 269
SPEAKER-BAGS: 355
PHONE-COVERS: 364
BATTERY-CASES: 377
BATTERies: 378
serums: 379
cosmetics: 228
cleansers: 380
toners: 381,
lotions: 295
body-washes: 382
bosy-oils: 383
creams: 384
sanitizers: 385
makeup: 233
sprays: 386
hair-oils: 387
mists: 294
lips-sticks: 388
perfumes: 291
deodorants: 389
vacuum-cleaners: 287
vacuum-cleaners-household: 371
electronics: 286
tablet: 329
phone-covers: 364
washes: 382
creams: 384
sanitizers: 385
makeup: 233
hand-foaming-soaps: 293
soaps: 265
shower-gels: 292
outdoor: 229
baskets: 390
baskets: 390
pots: 322
ice-buckets: 391
bowls: 391
solar-lights: 314
solar-lights: 392
furniture-outdoor: 393
fragrances-outdoor: 394
lanterns-outdoor: 395
cabinets: 396
air-coolers-outdoor: 315
air-heaters-outdoor: 316
'''
