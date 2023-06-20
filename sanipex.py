from bs4 import BeautifulSoup
import requests
import random
from product.create_product import create_product

categories = [458, 461l
              ]
sunbeds = [
    "https://sanipexgroup.com/argo-wood-icon-outdoor-sofa-right-modular-with-pouf-tlt-agodxpuf-l2-c130",
    "https://sanipexgroup.com/argo-wood-icon-outdoor-left-modular-sofa-lounge-tlt-agoxlsx-l2-c130",
    "https://sanipexgroup.com/argo-wood-icon-outdoor-sofa-loveseat-tlt-agodivlov-l2c131",
    "https://sanipexgroup.com/mea/argo-wood-icon-outdoor-armchair-tlt-agopl-l2-c131",
    "https://sanipexgroup.com/mea/cruise-teak-icon-outdoor-right-modular-sofa-lounge-tlt-crulxldx-c24",
    "https://sanipexgroup.com/mea/cruise-teak-icon-outdoor-sofa-left-modular-tlt-cruldivsx-c24",
    "https://sanipexgroup.com/mea/cruise-teak-icon-outdoor-armchair-tlt-crulpl-c24",
    "https://sanipexgroup.com/coral-outdoor-sofa-corner-tlt-corang-bi",
    "https://sanipexgroup.com/coral-outdoor-sofa-cx-tlt-corcx-bi",
    "https://sanipexgroup.com/coral-outdoor-sofa-lounge-right-hand-tlt-corlondx-bi",
    "https://sanipexgroup.com/coral-outdoor-sofa-lounge-left-hand-tlt-corlonsx-bi",
    "https://sanipexgroup.com/coral-outdoor-2-seater-sofa-tlt-cordiv-bi",
    "https://sanipexgroup.com/coral-outdoor-armchair-tlt-corplonrp-bi",
    "https://sanipexgroup.com/coral-outdoor-pouf-tlt-corpuf-bi",
    "https://sanipexgroup.com/sa/coral-outdoor-decorative-cushion-tlt-corpil5035-c38-cnfp",
    "https://sanipexgroup.com/frame-outdoor-3-seater-sofa-tlt-fmediv3-bi",
    "https://sanipexgroup.com/frame-outdoor-2-seater-sofa-tlt-fmediv2-bi",
    "https://sanipexgroup.com/frame-outdoor-armchair-tlt-fmepl-bi",
    "https://sanipexgroup.com/mea/frame-outdoor-armchair-tlt-fmepl-bi",
    "https://sanipexgroup.com/mea/cleo-alu-frame-outdoor-decor-cushion-tlt-fmepil4545-c129-cnfp",
    "https://sanipexgroup.com/slam-outdoor-sofa-right-hand-tlt-sladx-bi-cnfp",
    "https://sanipexgroup.com/slam-outdoor-sofa-left-hand-tlt-slasx-bi-cnfp",
    "https://sanipexgroup.com/slam-outdoor-sofa-tlt-slacx-bi-cnfp",
    "https://sanipexgroup.com/slam-outdoor-sofa-corner-tlt-slaang-bi-cnfp",
    "https://sanipexgroup.com/slam-outdoor-sofa-lounge-right-hand-tlt-slalondx-bi-cnfp",
    "https://sanipexgroup.com/slam-outdoor-sofa-lounge-left-hand-tlt-slalonsx-bi-cnfp",
    "https://sanipexgroup.com/slam-outdoor-sofa-pouf-tlt-slapuf-bi-cnfp",
    "https://sanipexgroup.com/slam-outdoor-decorative-cushion-tlt-slapil4525-c118-cnfp",
    "https://sanipexgroup.com/slam-outdoor-decorative-cushion-tlt-slapil6040-c99-cnfp",
    "https://sanipexgroup.com/organix-outdoor-sofa-a-comp-000648",
    "https://sanipexgroup.com/organix-outdoor-sofa-b-comp-000649",
    "https://sanipexgroup.com/organix-sofa-c-comp-000650",
    "https://sanipexgroup.com/organix-outdoor-sofa-d-comp-000651-supg",
    "https://sanipexgroup.com/qa/royal-botania-organix-coffee-table-element-900x743mm-rob-ogxl08",
    "https://sanipexgroup.com/organix-lounge-chair-comp-000739",
]


def get_image_from_tag(tag):
    return tag["href"]


def get_product_info(link, categories):
    response = requests.get(link)
    html = response.text

    soup = BeautifulSoup(html, features="html.parser")

    images = soup.find_all(class_="image square")
    name = soup.find('h1', attrs={'itemprop': 'name'}).text
    code = soup.find("div", attrs={"class": "sku"}).text
    short_description = soup.find('table', attrs={"class": "specification"})

    return {
        "name": name,
        "type": "simple",
        # "regular_price": str(price),
        "short_description": str(short_description),
        "status": "publish",
        "categories": [{"id": cat} for cat in categories],
        "images": [{"src": get_image_from_tag(tag), "name": f"{name} {random.randint(10,99)}"} for tag in images]
    }


for link in sunbeds:
    data = get_product_info(link, categories)
    print(data["images"])
    # print(str(data["short_description"]))
    try:
        data = create_product(data)
        print(data)
    except requests.exceptions.ReadTimeout:
        print('>>>>>>>>>>>>> Time out')
