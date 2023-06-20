import sys
from woocommerce import API
import json

wcapi = API(
    url="https://gquick.com",
    consumer_key="ck_8af3f64bd4a9c1ce4691d5d0df5148962f9fa280",
    consumer_secret="cs_fc6e9af15b7b09e7abb0d698c8d4e41f66d9ee65",
    version="wc/v3"
)


def get_categories(page):
    res = wcapi.get(f"products/categories",
                    params={"per_page": 100, "page": page}).json()
    # print((res))
    json_str = json.dumps(res)
    with open('json_files/categories.json', 'w') as fh:
        fh.write(json_str)
        print(json_str)


get_categories(3)
