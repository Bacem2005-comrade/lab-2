import xml.etree.ElementTree as ET

def parse_currency_xml(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    names = []
    values = []
    
    # Extract data from the XML
    for currency in root.findall('Currency'):
        name = currency.find('Name').text
        value = float(currency.find('Rate').text)  # Convert rate to float
        
        names.append(name)
        values.append(value)

    return names, values

def main():
    file_path = 'currency.xml'  # Path to your XML file
    names, values = parse_currency_xml(file_path)
    
    # Display extracted data
    print("Currency Names:")
    print(names)
    
    print("nCurrency Values:")
    print(values)

if __name__ == "__main__":
    main()
