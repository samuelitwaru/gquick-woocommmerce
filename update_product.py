import sys
from woocommerce import API
import json

wcapi = API(
    url="https://gquick.com",
    consumer_key="ck_8af3f64bd4a9c1ce4691d5d0df5148962f9fa280",
    consumer_secret="cs_fc6e9af15b7b09e7abb0d698c8d4e41f66d9ee65",
    version="wc/v3"
)


def update_product_from_json(path, id):
    fh = open(path)
    content = fh.read()
    data = json.loads(content)
    res = wcapi.put(f"products/{id}", data).json()
    print(res)


def update_product_category(id, category_id):
    data = {
        "categories": [
            {
                "id": category_id
            }
        ]
    }
    res = wcapi.put(f"products/{id}", data).json()


def update_product_categories(id, category_ids):
    data = {
        "categories": [
            {"id": category_id} for category_id in category_ids
        ]
    }
    res = wcapi.put(f"products/{id}", data).json()


if __name__ == "__main__":
    path = sys.argv[1]
    print(path)
    create_product_from_json(path)
