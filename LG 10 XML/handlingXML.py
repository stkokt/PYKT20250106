from xml.etree import ElementTree as ET 

tree = ET.parse('Fresstempel.xml')
root = tree.getroot()
print(root.findall('Restaurant'))

# for restaurant in root.findall('Restaurant'):
#     name = restaurant.get('name')
#     print(f"Restaurant: {name}")
#     menu = restaurant.find('Menu')
#     for dish in menu.findall('Dish'):
#         dish_name = dish.get('name')
#         price = dish.get('price')
#         print(f"  Gericht: {dish_name}, Preis: {price}")

namen = {restaurant.get('name'):{dish.get('name'):dish.get('price') 
                                 for dish in restaurant.find('Menu')} 
                                 for restaurant in root.findall('Restaurant')}



print(namen)

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

# Speichern der XML-Datei
xml_file_path = 'restaurants.xml'
tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)