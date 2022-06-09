# -*- coding: utf-8 -*-
"""
Created on Tue May 31 11:07:30 2022

@author: ShendR
"""
import xml.etree.ElementTree as ET

# # Create XML
# data = ET.Element('data')
# items = ET.SubElement(data, 'items')
# item1 = ET.SubElement(items, 'item')
# item2 = ET.SubElement(items, 'item')
# item1.set('name','item1')
# item2.set('name','item2')
# item1.text = 'item1abc'
# item2.text = 'item2abc'

# mydata = ET.ElementTree(data)
# mydata.write('test.xml')



# Read XML
tree = ET.parse('abes_parameters.xml')
root = tree.getroot()

# all item attributes
print('\nAll attributes:')
for elem in root:
    for subelem in elem:
        print(subelem.attrib)

# all items data
print('\nAll item data:')
for elem in root:
    for subelem in elem:
        print(subelem.text)
        
        
#  APDCam attributes
apdcam = root[0].attrib
print(apdcam)

mirror = root[1].attrib
mirror_motor = root[1][0].attrib
mirror_motor_calib = root[1][0][0]
mirror_encode = root[1][1].attrib
mirror_encode_calib = root[1][1][0].attrib

camera = root[2].attrib
camera_motor = root[2][0].attrib

lens = root[3].attrib

file = ET.ElementTree(root)
file.write('abes_parameters.xml')
