import sys
from woocommerce import API
import json

wcapi = API(
    url="https://gquick.com",
    consumer_key="ck_8af3f64bd4a9c1ce4691d5d0df5148962f9fa280",
    consumer_secret="cs_fc6e9af15b7b09e7abb0d698c8d4e41f66d9ee65",
    version="wc/v3"
)


def update_product(id, data):
    res = wcapi.put(f"products/{id}", data).json()
    print(res)
    return res


def update_products(ids):
    data = {
        "categories": [
            {
                "id": 368
            },
            {
                "id": 230
            },
            {
                "id": 155
            },
            {
                "id": 282
            },
        ],
    }

    for id in ids:
        res = update_product(id, data)


if __name__ == "__main__":
    ids = [3626, 3623, 3618]
    update_products(ids)
