# -*- coding: utf8 -*-
import unittest
import pyayml

class ViewTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_001(self):
        obj=pyayml.YaYml()
        data={
            'shop':{
                'name':'shop name',
                'company': 'my cool company',
                'url' : 'http://www.mail.ru',
            },
            'currencies':[
                {'id':'RUR','rate':'CBFR'},
            ],
            'categories': [
                {'id':'1','name':u'АЛЛ Продуктс'},
                {'id':'2','name':'sub cat products','parentId':'1'},
            ]
        }
        obj.set_shop(data['shop'])
        obj.set_currencies(data['currencies'])
        obj.set_categories(data['categories'])

        print obj.get_xml()

        #self.assertEqual(info['project'], 'pyayml')
