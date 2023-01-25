import pandas
import numpy as np
from product.create_product import create_product
import os

files = os.listdir('sheets')
print(files)

count = 0
for file in files:
    if file.endswith('.xlsx'):
        xl = pandas.ExcelFile(f'sheets/{file}')
        sheet_names = xl.sheet_names
        for name in sheet_names:
            df = xl.parse(name)
            n = len(df.to_records())
            print(file, name, n)
            count += n
print(count)

# print(excel_data_df)


# excel_data_df = excel_data_df.replace({np.nan: None})


# # print whole sheet data
# data = excel_data_df.to_records()
