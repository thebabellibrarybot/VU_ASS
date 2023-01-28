from lxml import etree as et

test = './Data/XML_releases/xml/ted_nl-20160408.xml'

tree = et.parse(test)
root = tree.getroot()

print(root.attrib)

talks = root.findall('file')
print(len(talks))

# damn y'all really making it tuff on a boys local storgae 

test_talk = talks[5]
for ch in test_talk.find('head').getchildren().find('wordnum'):
    print(ch)
    
