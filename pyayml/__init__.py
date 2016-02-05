# -*- coding: utf8 -*-
from lxml import etree
from datetime import datetime

REPLACEMENTS={
    '"': '&quot;',
    '&': '&amp;',
    '>': '&gt;',
    '<': '&lt;',
    "'": '&apos;',
}
HEADER="""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE yml_catalog SYSTEM "shops.dtd">
"""
SHOP_TAGS=[
    'name',
    'company',
    'url',
    'platform',
    'version',
    'agency',
    'email',
    'cpa',
    'local_delivery_cost'
]
OFFERS_TAGS={
    '':[
        'url',
        'price',
        'currencyId',
        'categoryId',
        'market_category',
        'picture',
        'store',
        'pickup',
        'delivery',
        'local_delivery_cost',
        'name',
        'vendor',
        'vendorCode',
        'description',
        'sales_notes',
        'manufacturer_warranty',
        'country_of_origin',
        'adult',
        'age',
        'barcode',
        'param',
    ],
    'vendor.model':[
        'url',
        'price',
        'currencyId',
        'categoryId',
        'market_category',
        'picture',
        'store',
        'pickup',
        'delivery',
        'local_delivery_cost',
        'typePrefix',
        'vendor',
        'vendorCode',
        'model',
        'description',
        'sales_notes',
        'manufacturer_warranty',
        'seller_warranty',
        'country_of_origin',
        'downloadable',
        'adult',
        'age',
        'barcode',
        'cpa',
        'rec',
        'expiry',
        'weight',
        'dimensions',
        'param',
    ],
    'book':[
        'url',
        'price',
        'currencyId',
        'categoryId',
        'market_category',
        'picture',
        'store',
        'pickup',
        'delivery',
        'local_delivery_cost',
        'author',
        'name',
        'publisher',
        'series',
        'year',
        'ISBN',
        'volume',
        'part',
        'language',
        'binding',
        'page_extent',
        'table_of_contents',
        'description',
        'downloadable',
        'age',
    ],
    'audiobook':[
        'url',
        'price',
        'currencyId',
        'categoryId',
        'market_category',
        'picture',
        'author',
        'name',
        'publisher',
        'series',
        'year',
        'ISBN',
        'volume',
        'part',
        'language',
        'table_of_contents',
        'performed_by',
        'performance_type',
        'storage',
        'format',
        'recording_length',
        'description',
        'downloadable',
        'age',
    ],
    'artist.title':[
        #music
        'url',
        'price',
        'currencyId',
        'categoryId',
        'market_category',
        'picture',
        'store',
        'pickup',
        'delivery',
        'artist',
        'title',
        'year',
        'media',
        'description',
        'age',
        'barcode',
        #video
        # 'url',
        # 'price',
        # 'currencyId',
        # 'categoryId',
        # 'market_category',
        # 'picture',
        # 'store',
        # 'pickup',
        # 'delivery',
        # 'title',
        # 'year',
        # 'media',
        # 'starring',
        # 'director',
        # 'originalName',
        # 'country',
        # 'description',
        # 'adult',
        # 'age',
        # 'barcode',
        
    ],

    'tour':[
        'url',
        'price',
        'currencyId',
        'categoryId',
        'market_category',
        'picture',
        'store',
        'pickup',
        'delivery',
        'worldRegion',
        'country',
        'region',
        'days',
        'dataTour',
        'name',
        'hotel_stars',
        'room',
        'meal',
        'included',
        'transport',
        'description',
        'age',
    ],
    'event.ticket':[
        'url',
        'price',
        'currencyId',
        'categoryId',
        'market_category',
        'picture',
        'store',
        'pickup',
        'delivery',
        'name',
        'place',
        'hall plan',
        'date',
        'is_premiere',
        'is_kids',
        'age',
    ],
}
PICTUTE_MAX_COUNT=10
PICTURE_URL_MAXLEN=512
OFFER_NAME_MAXLEN=255
SHOP_NAME_MAXLEN=20
CURRENCIES=[
    "RUR",
    "USD",
    "EUR",
    "UAH",
    "KZT",
    "BYR",
]
CURSES=[
    'CBRF',
    'NBU',
    'NBK',
    'СВ',
]

class YaYml(object):
    def __init__(self):
        self.root = etree.Element('yml_catalog', date=datetime.today().strftime("%Y-%m-%d %H:%M"))

    def get_xml(self):
        return HEADER+etree.tostring(self.root, encoding='utf-8', pretty_print=True)

    def set_shop(self,shop_data):
        shop_tag = etree.SubElement(self.root, 'shop')
        self.shop=shop_tag
        
        for key in SHOP_TAGS:
            if key in shop_data:
                etree.SubElement(shop_tag, key).text = shop_data[key]

    def set_currencies(self,currencies_data):
        currencies_tag = etree.SubElement(self.shop, 'currencies')
        self.currencies=currencies_tag
        for currency in currencies_data:
            #xxx check id, rate, plus
            if currency.get('plus'):
                etree.SubElement(currencies_tag, 'currency', id=currency['id'], rate=currency['rate'], plus=currency['plus'])
            else:
                etree.SubElement(currencies_tag, 'currency', id=currency['id'], rate=currency['rate'])


    def set_categories(self, categories_data):
        categories_tag = etree.SubElement(self.shop, 'categories')
        for category in categories_data:
            if not category.get('parentId') is None:
                etree.SubElement(categories_tag, 'category', id=category['id'], parentId=category['parentId']).text = category['name']
            else:
                etree.SubElement(categories_tag, 'category', id=category['id']).text = category['name']

    def set_offers(self, offers_data):
        offers_tag = etree.SubElement(self.shop,'offers')
        for offer in offers_data:
            otype=offer.get('type','')
            if otype:
                offer_tag = etree.SubElement(offers_tag,'offer', id=offer['id'], available="true", type=otype)
            else:
                offer_tag = etree.SubElement(offers_tag,'offer', id=offer['id'], available="true")
            for key in OFFERS_TAGS[otype]:
                if key in offer:
                    if isinstance(offer[key],list):
                        for param in offer[key]:
                            if isinstance(param,dict):
                                kwargs=dict((k,v) for k,v in param.items() if not k.startswith('_'))
                                etree.SubElement(offer_tag, key, **kwargs).text = param['_text']
                            else:
                                etree.SubElement(offer_tag, key).text = param
                    else:
                        etree.SubElement(offer_tag, key).text = offer[key]
