from xml.dom import minidom

xmldoc = minidom.parse('items.xml')
itemlist = xmldoc.getElementsByTagName('item')

print(len(itemlist))
print(itemlist[0].attributes['name'].value)
print('#')
for s in itemlist:
    print(s.attributes['name'].value)
