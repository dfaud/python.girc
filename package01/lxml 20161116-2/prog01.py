'''
Created on 16 nov. 2016

@author: U01E852
'''
from lxml import objectify, etree

xml = '''
<dataset>
  <statusthing>success</statusthing>
  <datathing gabble="sent">joe@email.com</datathing>
  <datathing gabble="not sent"></datathing>
</dataset>
'''

root = objectify.fromstring(xml)

print ("#1########")
print root.tag
print root.text
print root.attrib

# dataset
# None
# {}

print ("#2########")
print root.statusthing.tag
print root.statusthing.text
print root.statusthing.attrib
# statusthing
# success
# {}

print ("#3########")
for e in root.datathing:
    print e.tag
    print e.text
    print e.attrib
    print e.attrib['gabble']
    print "---"

# datathing
# joe@email.com
# {'gabble': 'sent'}
# sent
# datathing
# None
# {'gabble': 'not sent'}
# not sent

print ("#4########")
for e in root.getchildren():
    print e.tag
# statusthing
# datathing
# datathing

print ("#5########")
for e in root.iterchildren():
    print e.tag
# statusthing
# datathing
# datathing

# you cannot modify the text attribute of an element.
# instead just assign to the element itself.
try:
    root.statusthing.text = 'failure'
except:
    import traceback
    traceback.print_exc()
# Traceback (most recent call last):
#   File "lxml_ex.py", line 54, in <module>
#     root.statusthing.text = 'failure'
#   File "lxml.objectify.pyx", line 237, in lxml.objectify.ObjectifiedElement.__setattr__ (src/lxml/lxml.objectify.c:2980)
# TypeError: attribute 'text' of 'StringElement' objects is not writable

# modify element text and write it out as xml again
root.statusthing = 'failure'
xml_new = etree.tostring(root, pretty_print=True)
print xml_new
# <dataset>
#   <statusthing xmlns:py="http://codespeak.net/lxml/objectify/pytype" py:pytype="str">failure</statusthing>
#   <datathing gabble="sent">joe@email.com</datathing>
#   <datathing gabble="not sent">
# </datathing></dataset>

# Use deannotate() to get rid of 'py:pytype' information
objectify.deannotate(root, cleanup_namespaces=True)
xml_new = etree.tostring(root, pretty_print=True)
print xml_new
# <dataset>
#   <statusthing>failure</statusthing>
#   <datathing gabble="sent">joe@email.com</datathing>
#   <datathing gabble="not sent">
# </datathing></dataset>

# Add a child element to the root
c = etree.Element("thisdoesntmatter")
c.tag = "thisdoesntmattereither"
c.text = "mytext"
c.attrib['myattr'] = 'myvalue'
root.newchild = c
objectify.deannotate(root, cleanup_namespaces=True)
xml_new = etree.tostring(root, pretty_print=True)
print xml_new
# <dataset>
#   <statusthing>failure</statusthing>
#   <datathing gabble="sent">joe@email.com</datathing>
#   <datathing gabble="not sent">
#   <newchild myattr="myvalue">mytext</newchild>
# </datathing></dataset></module>