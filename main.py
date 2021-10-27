from os import write
import xml.etree.ElementTree as ET
import csv 
import pandas as pd

def xml_to_csv(xml_file_path, csv_output_name) -> None:
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    with open(csv_output_name, 'w', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        headers = (child.tag for child in root[0])
        writer.writerow(headers)
        num_records = len(root)

        for record in range(num_records):
            rec = [child.text for child in root[record]]
                
            writer.writerow(rec)

def csv_to_excel(csv_doc_name):
    df = pd.read_csv(csv_doc_name)
    writer2 = pd.ExcelWriter('output.xlsx')
    df.to_excel(writer2, index=False)
    writer2.save()
        

if __name__ == '__main__':
    import sys
    import pathlib

    try:
        xml_file_path = sys.argv[1]
        csv_name = sys.argv[2]

    except IndexError:
        sys.exit('Tow arguments required. One xml path and one save file name')


    with pathlib.Path(xml_file_path) as xml_file:
        if xml_file.is_file():
            xml_to_csv(xml_file_path, csv_name)
            csv_to_excel(csv_name)

        else:
            sys.exit(f'Did not find {xml_file_path}')