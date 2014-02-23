# -*- coding: utf8 -*-
import unittest
import pyayml

class ViewTests(unittest.TestCase):
    def setUp(self):
        pass

    #http://softwaremaniacs.org/forum/python/25537/
    def test_001(self):
        obj=pyayml.YaYml()
        data={
            'shop':{
                'name':'shop name',
                'company': 'my cool company',
                'url' : 'http://www.mail.ru',
            },
            'currencies':[
                {'id':'RUR','rate':'CBRF'},
                {'id':'USD','rate':'CBRF'},
            ],
            'categories': [
                {'id':'1','name':u'АЛЛ Продуктс'},
                {'id':'2','name':'sub cat products','parentId':'1'},
            ],
            'offers':[
                {
                    'id':'1',
                    'url':'http://mail.ru/1212',
                    'price':'1234',
                    'currencyId':'RUR',
                    'categoryId':'1',
                    'picture':'http://mail.ru/1212.jpg',
                    'name':'product1',
                    'vendor':'AND',
                    'description':'some text here',
                },
                {
                    'type':"vendor.model",
                    'id':'2',
                    'url':'http://mail.ru/1212?ddd&c=d',
                    'price':'1234',
                    'currencyId':'RUR',
                    'categoryId':'2',
                    'picture':'http://mail.ru/1212.jpg',
                    'model':'product2',
                    'vendor':'AND',
                    'description':"""some text here
                        '"': '&quot;',
                        '&': '&amp;',
                        '>': '&gt;',
                        '<': '&lt;',
                        "'": '&apos;',
                    """,
                },
            ],
        }
        obj.set_shop(data['shop'])
        obj.set_currencies(data['currencies'])
        obj.set_categories(data['categories'])
        obj.set_offers(data['offers'])

        #print obj.get_xml()

        #self.assertEqual(info['project'], 'pyayml')

#https://wiki.python.org/moin/EscapingXml
#https://wiki.python.org/moin/EscapingHtml