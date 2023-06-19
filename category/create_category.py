import sys
from woocommerce import API
import json

wcapi = API(
    url="https://gquick.com",
    consumer_key="ck_8af3f64bd4a9c1ce4691d5d0df5148962f9fa280",
    consumer_secret="cs_fc6e9af15b7b09e7abb0d698c8d4e41f66d9ee65",
    version="wc/v3"
)


def create_category(data):
    res = wcapi.post(f"products/categories/", data).json()
    print(res)


cats = [
    ("Air Fryers", "https://gquick.com/wp-content/uploads/2022/11/ninja-air-fryer-150x150.jpg"),
    ("Pressure Cookers", "https://gquick.com/wp-content/uploads/2022/11/nutri-cook-nutribullet-1-150x150.jpg"),
    ("Microwaves", "https://gquick.com/wp-content/uploads/2022/11/blackdecker-900w-microwave-oven-with-grill-150x150.jpg"),
    ("Refrigerators", "https://gquick.com/wp-content/uploads/2022/09/2-1-150x150.png"),
    ("Vacuum cleaners", "https://gquick.com/wp-content/uploads/2023/01/Kenwood-0.5-Litre-Dust-Capacity-Wet-And-Dry-Handheld-Vacuum-150x150.png"),
    ("Table Mats", "https://cdn.shopify.com/s/files/1/0104/1524/3330/products/zoco-home-kindia-table-mat-natural-white-37303692230868_150x.png?v=1655385917"),
    ("Scented Candles", "https://gquick.com/wp-content/uploads/2022/09/1-21-150x150.jpg"),
    # ("Unscented Candles", ""),
    # ("Utensils", ""),
    # ("Cutlery", "",),
    # ("Tables", "",),
    # ("Chairs", "",),
    # ("Cupboards", "",),
]


if __name__ == "__main__":
    for cat in cats:
        data = {
            "name": cat[0],
            "slug": cat[0].lower().replace(' ', '-') + '-household',
            "parent": 230,
            "image": {
                "src": cat[1],
            }

        }
        print(data)
        create_category(data)
