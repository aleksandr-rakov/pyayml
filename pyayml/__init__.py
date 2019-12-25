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
    'delivery-options',
    'pickup-options',
]
OFFERS_TAGS={
    '':[
        'url',
        'price',
        'oldprice',
        'currencyId',
        'categoryId',
        'market_category',
        'picture',
        'store',
        'pickup',
        'delivery',
        'delivery-options',
        'pickup-options',
        'name',
        'goodname', #ali
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
        'keywords', #tiu
        'weight', #ali
        'Length', #ali
        'Width', #ali
        'Height', #ali
        'quantity', #ali
    ],
    'vendor.model':[
        'url',
        'price',
        'oldprice',
        'currencyId',
        'categoryId',
        'market_category',
        'picture',
        'store',
        'pickup',
        'delivery',
        'delivery-options',
        'pickup-options',
        'typePrefix',
        'vendor',
        'vendorCode',
        'model',
        'goodname', #ali
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
        'keywords', #tiu
        'Length', #ali
        'Width', #ali
        'Height', #ali
        'quantity', #ali
    ],
    'book':[
        'url',
        'price',
        'oldprice',
        'currencyId',
        'categoryId',
        'market_category',
        'picture',
        'store',
        'pickup',
        'delivery',
        'delivery-options',
        'pickup-options',
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
        'oldprice',
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
        'oldprice',
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
        # 'oldprice',
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
        'oldprice',
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
        'oldprice',
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

    def insert_delivery_options(self,parent,data):
        delivery_options_tag = etree.SubElement(parent,'delivery-options')
        for opt in data:
            etree.SubElement(delivery_options_tag, 'option', **opt)

    def insert_pickup_options(self,parent,data):
        pickup_options_tag = etree.SubElement(parent,'pickup-options')
        for opt in data:
            etree.SubElement(pickup_options_tag, 'option', **opt)

    def set_shop(self,shop_data):
        shop_tag = etree.SubElement(self.root, 'shop')
        self.shop=shop_tag
        
        for key in SHOP_TAGS:
            if key in shop_data:
                if key=='delivery-options':
                    self.insert_delivery_options(shop_tag,shop_data[key])
                elif key=='pickup-options':
                    self.insert_pickup_options(shop_tag,shop_data[key])
                else:
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

    def set_shop_delivery_options(self, delivery_options):
        self.insert_delivery_options(self.shop,delivery_options)

    def set_offers(self, offers_data):
        offers_tag = etree.SubElement(self.shop,'offers')
        for offer in offers_data:
            otype=offer.get('type','')
            available='true'
            kwargs=dict(id=offer['id'], available=available)
            if '__available' in offer:
                kwargs['available']=offer['__available'] and 'true' or 'false'
            if '__selling_type' in offer:
                kwargs['selling_type']=offer['__selling_type']
            if otype:
                kwargs['type']=otype
            if '__group_id' in offer:
                kwargs['group_id']=offer['__group_id']
                
            offer_tag = etree.SubElement(offers_tag,'offer', **kwargs)
            for key in OFFERS_TAGS[otype]:
                if key in offer:
                    if key=='delivery-options':
                        self.insert_delivery_options(offer_tag,offer[key])
                    elif key=='pickup-options':
                        self.insert_pickup_options(offer_tag,offer[key])
                    elif isinstance(offer[key],list):
                        for param in offer[key]:
                            if isinstance(param,dict):
                                kwargs=dict((k,v) for k,v in param.items() if not k.startswith('_'))
                                etree.SubElement(offer_tag, key, **kwargs).text = param['_text']
                            else:
                                etree.SubElement(offer_tag, key).text = param
                    else:
                        if "__use_cdata_%s"%key in offer:
                            etree.SubElement(offer_tag, key).text=etree.CDATA(offer[key])
                        else:
                            etree.SubElement(offer_tag, key).text = offer[key]

    def set_promos(self, promos_data):
        if promos_data:
            promos_tag = etree.SubElement(self.shop, 'promos')
            for promo in promos_data:
                promo_tag=etree.SubElement(promos_tag, 'promo', id=promo['id'], type=promo['type'])
                for t in ('start-date','end-date','description','url','promo-code'):
                    tval=promo.get(t)
                    if tval:
                        etree.SubElement(promo_tag, t).text=tval

                kwargs={'unit': promo['unit']}
                if promo['currency']:
                    kwargs['currency']=promo['currency']
                etree.SubElement(promo_tag, 'discount', **kwargs).text=promo['discount']

                purchase_el=etree.SubElement(promo_tag, 'purchase')
                for product in promo['products']:
                    kvargs={'offer-id':product}
                    etree.SubElement(purchase_el, 'product', **kvargs)
