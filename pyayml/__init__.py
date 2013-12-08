# -*- coding: utf8 -*-
from lxml import etree
from datetime import datetime

class YaYml(object):
    REPLACEMENTS={
        '"': '&quot;',
        '&': '&amp;',
        '>': '&gt;',
        '<': '&lt;',
        "'": '&apos;',
    }
    HEADER="""<?xml version="1.0" encoding="windows-1251"?>
<!DOCTYPE yml_catalog SYSTEM "shops.dtd">"""
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
            'market_category ',
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
            'categoryId ',
            'market_category ',
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
            'market_category ',
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
            'market_category ',
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
            'market_category ',
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
            # 'market_category ',
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
            'market_category ',
            'picture',
            'store',
            'pickup',
            'delivery',
            'worldRegion',
            'country ',
            'region',
            'days',
            'dataTour',
            'name',
            'hotel_stars ',
            'room',
            'meal',
            'included',
            'transport',
            'description ',
            'age',
        ],
        'event.ticket':[
            'url',
            'price',
            'currencyId',
            'categoryId',
            'market_category ',
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


    def __init__(self):
        self.root = etree.Element('yml_catalog', date=datetime.today().strftime("%Y-%m-%d %H-%M"))

    # def set_sthop(self):
    #     shop = etree.SubElement(self.root, 'shop')
    #     self.shop=shop
        
    #     etree.SubElement(shop, 'name').text = YML_CONFIG['name']
    #     etree.SubElement(shop, 'company').text = YML_CONFIG['company']
    #     etree.SubElement(shop, 'url').text = YML_CONFIG['url']

    # def set_currencies(self):
    #     currencies = etree.SubElement(self.shop, 'currencies')
    #     self.currencies=currencies
    #     for currency in YML_CONFIG['currencies']:
    #         etree.SubElement(currencies, 'currency', rate=currency['rate'], id=currency['id'])


    # def set_categories(self, shop):
    #     categories_tag = etree.SubElement(shop, 'categories')
    #     for category in clazz.objects.all():
    #         etree.SubElement(categories_tag, 'category', id=str(category.id)).text = category.get_name()

    # def add_offers(self, shop):
    #     offers = etree.SubElement(shop,'offers')
    #     for product in Product.objects.filter(active=True):
    #         offer = etree.SubElement(offers,'offer', id=str(product.id), available="true")
    #         etree.SubElement(offer,'url').text =  YML_CONFIG['url'] + product.get_absolute_url()
    #         etree.SubElement(offer,'price').text =  str(product.get_price())
    #         etree.SubElement(offer,'currencyId').text =  product.get_currency()
    #         etree.SubElement(offer,'categoryId').text =  str(product.category.id)
    #         etree.SubElement(offer,'picture').text = YML_CONFIG['url'] + product.head_image.url
    #         etree.SubElement(offer,'delivery').text = "true"
    #         etree.SubElement(offer,'name').text = product.get_name()
