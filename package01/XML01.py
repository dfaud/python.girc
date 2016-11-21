#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/
#from lxml import etree
#tree = etree.parse("data.xml")
#for user in tree.xpath("/users/user/nom"):
#    print(user.text)
#/!>

from xml.dom import minidom
doc = minidom.parse('G2A.xml')
for element in root.getElementsByTagName('UDI_EXPEDITEUR'):
    print element
#> doc
#<xml.dom.minidom.Document instance at 0x...>
