import sys
from woocommerce import API
import json

wcapi = API(
    url="https://gquick.com",
    consumer_key="ck_8af3f64bd4a9c1ce4691d5d0df5148962f9fa280",
    consumer_secret="cs_fc6e9af15b7b09e7abb0d698c8d4e41f66d9ee65",
    version="wc/v3"
)


def create_product_from_json(path):
    fh = open(path)
    content = fh.read()
    data = json.loads(content)
    res = wcapi.post("products", data).json()
    print(res)


if __name__ == "__main__":
    path = sys.argv[1]
    print(path)
    create_product_from_json(path)
