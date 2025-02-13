import xml.etree.ElementTree as ET
from xml.dom import minidom

# Das gegebene Dictionary
data = {
    "Ali's Frittenbude": {'Gericht 1': '10.99', 'Gericht 2': '12.99', 'Gericht 3': '8.99'},
    "Frank's Kebab": {'Gericht A': '11.99', 'Gericht B': '14.99', 'Gericht C': '9.99'},
    "Luigi's Diner": {'Gericht X': '13.99', 'Gericht Y': '15.99', 'Gericht Z': '10.99'},
    "Olga's Sushi": {'Gericht Alpha': '12.99', 'Gericht Beta': '13.99', 'Gericht Gamma': '9.99'},
    "Émilienne's Burger": {'Gericht I': '14.99', 'Gericht II': '16.99', 'Gericht III': '11.99'}
}

# Funktion zum Umwandeln eines Dictionaries in XML
def dict_to_xml(tag, d):
    elem = ET.Element(tag)
    for key, val in d.items():
        child = ET.SubElement(elem, "Restaurant", name=key)
        menu = ET.SubElement(child, "Menu")
        for dish, price in val.items():
            ET.SubElement(menu, "Dish", name=dish, price=price)
    return elem

# Erstellen des XML-Baums
root = dict_to_xml("Location", data)

# Erstellen eines ElementTree-Objekts
tree = ET.ElementTree(root)

# Umwandeln des XML-Baums in einen String mit Einrückungen
xml_str = ET.tostring(root, encoding='utf-8')
parsed_xml = minidom.parseString(xml_str)
pretty_xml_as_string = parsed_xml.toprettyxml(indent="  ")

# Speichern der formatierten XML-Datei
xml_file_path = 'restaurants_formatted.xml'
with open(xml_file_path, 'w', encoding='utf-8') as file:
    file.write(pretty_xml_as_string)

xml_file_path
