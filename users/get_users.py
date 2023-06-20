import sys
from woocommerce import API
import json

wcapi = API(
    url="https://gquick.com",
    consumer_key="ck_8af3f64bd4a9c1ce4691d5d0df5148962f9fa280",
    consumer_secret="cs_fc6e9af15b7b09e7abb0d698c8d4e41f66d9ee65",
    version="wc/v3"
)


users = wcapi.get("customers", params={"per_page": 100, "page": 1}).json()

for user in users:
    # if 'gmail' in user["email"]:
    print(user)
    print(user["id"], user["email"], user["first_name"],
          user["last_name"], user["username"],)
