from bs4 import BeautifulSoup
import requests
import random
from product.create_product import create_product

categories = [458, 461]
sunbeds = [
    # "https://sanipexgroup.com/su-nest-3-seater-sofa-can-57523usl",
    # "Nest 2 Seater Sofa with Seat & 2 Back Cushions Quick Dry Foam Padding Removable Lining Aluminium Frame 420 mm Seat Height L1650 x W800 x H740 mm"
    # "https://sanipexgroup.com/su-nest-outdoor-table-footstool-large-can-57321u",
    # "https://sanipexgroup.com/su-nest-footstool-can-57320u-cnfp",
    "https://sanipexgroup.com/nest-outdoor-armchair-can-57421wsw",
    # "https://sanipexgroup.com/nest-outdoor-lounge-chair-can-57422usl",
    # "https://sanipexgroup.com/ja-moments-outdoor-3-seater-sofa-can-7543rogaitg",
    # "https://sanipexgroup.com/moments-outdoor-armchair-can-7443rogaitg",
    "https://sanipexgroup.com/cane-line-moments-2-seater-sofa-right-module-can-7542rog",
    # "https://sanipexgroup.com/ja-moments-outdoor-corner-module-can-7545rogaitg",
    # "https://sanipexgroup.com/ja-moments-outdoor-2-seater-sofa-left-module-can-7541rogaitg",
    # "https://sanipexgroup.com/ja-moments-extra-back-outdoor-pillow-600x400x160mm-grey-can-7543ry81",
    # "https://sanipexgroup.com/ja-sense-outdoor-3-seater-sofa-can-7543uaitt",
    # "https://sanipexgroup.com/sense-outdoor-armchair-can-7443uaitt",
    # "https://sanipexgroup.com/capture-outdoor-2-seater-sofa-right-modular-can-55402aitl",
    # "https://sanipexgroup.com/capture-outdoor-2-seater-sofa-left-modular-can-55401aitl",
    "https://sanipexgroup.com/capture-outdoor-2-seater-sofa-modular-can-55400aitl",
    "https://sanipexgroup.com/capture-outdoor-pouf-can-55300aitl",
    # "https://sanipexgroup.com/arch-outdoor-3-seater-sofa-base-and-seat-cushion-can-55803futaitt",
    "https://sanipexgroup.com/arch-outdoor-launch-chair-base-pouf-with-seat-cushion-can-54800futaitt",
    "https://sanipexgroup.com/arch-outdoor-armrest-backrest-low-can-54800lbfut",
    # "https://sanipexgroup.com/arch-outdoor-back-cushion-can-54800bcy80",
    "https://sanipexgroup.com/arch-outdoor-side-cushion-small-can-54800scy80",
    "https://sanipexgroup.com/santorini-outdoor-3-seater-sofa-har-sano-05a-apm-cnfp",
    # "https://sanipexgroup.com/santorini-outdoor-2-seater-sofa-har-sano-06a-apm-cnfp",
    "https://sanipexgroup.com/santorini-outdoor-armchair-har-sano-08a-apm-cnfp",
    "https://sanipexgroup.com/santorini-outdoor-single-modular-sofa-har-sano-08d-apm-cnfp",
    # "https://sanipexgroup.com/santorini-outdoor-pouf-har-sano-09a-apm-cnfp",
    # "https://sanipexgroup.com/santorini-outdoor-right-hand-modular-sofa-har-sano-06cr-apm-cnfp",
    # "https://sanipexgroup.com/santorini-outdoor-left-modular-sofa-har-sano-06cl-apm-cnfp",
    "https://sanipexgroup.com/ora-outdoor-3-seater-sofa-har-ora-05a-tag",
    # "https://sanipexgroup.com/ora-outdoor-armchair-har-ora-08a-tag",
    # "https://sanipexgroup.com/avalon-outdoor-3-seater-sofa-har-aval-05a-tag",
    # "https://sanipexgroup.com/avalon-outdoor-armchair-har-aval-08a-tag",
    # # "Avalon Pouf with Seat Cushion Quick Dry Foam Padding Removable Lining Teak Frame 380 mm Seat Height L860 x W635 x H380 mm
    # "https://sanipexgroup.com/ria-soft-outdoor-3-seater-sofa-fst-7623-11eric-cnfp",
    # "https://sanipexgroup.com/ria-soft-outdoor-2-seater-sofa-fst-7622-11eric-cnfp",
    # "https://sanipexgroup.com/ria-soft-outdoor-armchair-fst-7621-11eric-cnfp",
    # "https://sanipexgroup.com/truro-outdoor-3-seater-sofa-frame-with-2-side-tables-jtk-4918-0155-set-tk",
    # "https://sanipexgroup.com/truro-outdoor-2-seater-sofa-frame-with-2-side-tables-jtk-4917-0154-set-tk",
    # "https://sanipexgroup.com/bari-pergola-truro-fano-outdoor-backrest-jtk-01-000923",
    # "https://sanipexgroup.com/truro-seatback-cushion-set-jtk-02-000929",
    # "https://sanipexgroup.com/durbuy-outdoor-3-seater-sofa-jtk-01-006240",
    # "https://sanipexgroup.com/durbuy-outdoor-2-seater-sofa-jtk-01-006239",
    # "https://sanipexgroup.com/durbuy-outdoor-armchair-jtk-01-006238",
    # "https://sanipexgroup.com/caspe-outdoor-3-seater-sofa-jtk-01-006245",
    # "https://sanipexgroup.com/caspe-outdoor-armchair-jtk-01-006244",
    # "https://sanipexgroup.com/fortuna-sock-outdoor-3-seater-sofa-jtk-01-002474-cnfp",
    # "https://sanipexgroup.com/fortuna-sock-outdoor-2-seater-sofa-jtk-01-003361-cnfp",
    # "https://sanipexgroup.com/fortuna-sock-outdoor-armchair-jtk-01-002472-cnfp",
    # "https://sanipexgroup.com/bali-outdoor-3-seater-sofa-var-2383ac-tk-gc",
    # "https://sanipexgroup.com/bali-outdoor-2-seater-sofa-var-2382ac-tk-gc",
    # "https://sanipexgroup.com/bali-outdoor-armchair-var-2381ac-tk-gc",
    # "https://sanipexgroup.com/colori-di-como-outdoor-3-seater-sofa-bdo-gym-eva3p3me80-1",
    # # "Colori Di Como 2 Seater Sofa with Seat & Back Cushion Quick Dry Foam Padding Removable Lining Aluminium Frame 460 mm Seat Height L1780 x W790 x H720 mm
    # "https://sanipexgroup.com/colori-di-como-outdoor-armchair-bdo-gym-poeva1g128-4-cnfp",
    # "https://sanipexgroup.com/ithaca-outdoor-3-seater-sofa-gym-ith-103-wsb-cnfp",
    # "https://sanipexgroup.com/ithaca-outdoor-2-seater-sofa-gym-ith-102-wsb-cnfp",
    # "https://sanipexgroup.com/mea/ithaca-outdoor-right-modular-2-seater-sofa-gym-ith-112r-csc",
    # "https://sanipexgroup.com/mea/ithaca-outdoor-left-modular-2-seater-sofa-gym-ith-112l-wsb-cnfp",
    # "https://sanipexgroup.com/mea/ithaca-outdoor-armchair-gym-ith-101-wsb-cnfp",
    # "https://sanipexgroup.com/mea/ithaca-outdoor-right-modular-sofa-lounge-gym-ith-113r-wsb-cnfp",
    # "https://sanipexgroup.com/mea/ithaca-outdoor-left-modular-sofa-lounge-gym-ith-113l-wsb-cnfp",
    # "https://sanipexgroup.com/mea/sardinia-outdoor-bean-bag-lounge-chair-gym-sar-603-slv-cnfp",
    # "https://sanipexgroup.com/mea/sardinia-outdoor-bean-bag-lounge-bed-gym-sar-604-slv-cnfp",
    # "https://sanipexgroup.com/mea/sardinia-outdoor-bean-bag-pouf-gym-sar-620-slv-cnfp",
    # # "Sardinia Optional Cushion with Strap Memory Foam Lined Polystyrene Beans Removable Lining Dia. 250 x H800 mm",
    # # "Scroll 3 Seater Sofa Aluminium Frame 460 mm Seat Height L2030 x W990 x H910 mm",
    # # "Scroll Sofa Cushion Set with Bolster Cushion Water Repellent Removable Lining L1980 x W780 x H450 mm",
    # # "Scroll Armchair Aluminium Frame 460 mm Seat Height L720 x W990 x H910 mm",
    # "https://sanipexgroup.com/ulm-outdoor-3-seater-sofa-with-cushion-von-54135-ecr-sta-cnfp",
    # "https://sanipexgroup.com/ulm-outdoor-sectional-sofa-armless-with-cushion-von-54171-ecr-sta-cnfp",
    # "https://sanipexgroup.com/ulm-outdoor-armchair-with-cushion-von-54134-ecr-sta-cnfp",
    # "https://sanipexgroup.com/ulm-outdoor-sectional-sofa-corner-with-cushion-von-54172-ecr-sta-cnfp",
    # "https://sanipexgroup.com/ulm-outdoor-ottoman-pouf-von-54133-ecr-sta-cnfp",
    # "https://sanipexgroup.com/ulm-outdoor-sectional-sofa-right-with-cushion-von-54174-ecr-sta-cnfp",
    # "https://sanipexgroup.com/ulm-outdoor-sectional-sofa-left-with-cushion-von-54173-ecr-sta-cnfp",
    # "https://sanipexgroup.com/belt-outdoor-modular-1-seater-sofa-armless-var-2213-gc",
    # "https://sanipexgroup.com/belt-outdoor-modular-corner-sofa-var-2216-gc",
    # "https://sanipexgroup.com/belt-outdoor-right-modular-sofa-lounge-var-2214-gc",
    # "https://sanipexgroup.com/belt-outdoor-left-modular-sofa-lounge-var-2215-gc",
    # "https://sanipexgroup.com/stone-outdoor-sofa-von-55005-ecr-cnfp",
    # "https://sanipexgroup.com/stone-outdoor-sofa-cushion-von-55005co-zae-cnfp",
    # "https://sanipexgroup.com/stone-outdoor-lounge-chair-von-55006-ecr-cnfp",
    # "https://sanipexgroup.com/stone-outdoor-lounge-chair-cushion-von-55006co-zae-cnfp",
    # "https://sanipexgroup.com/stone-outdoor-coffee-table-von-55007-ecr-cnfp",
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


count = 1
for link in sunbeds:
    print(count)
    data = get_product_info(link, categories)
    # print(data["images"])
    # add attributes
    data['attributes'] = [
        {
            "id": 0,
            "name": 'delivery',
            "options": ['10 DAYS - INTERNATIONAL']
        }
    ]
    try:
        data = create_product(data)
        print(data)
    except requests.exceptions.ReadTimeout:
        print('>>>>>>>>>>>>> Time out')
    count += 1
