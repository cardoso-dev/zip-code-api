# pip install xmltodict
import json
import xmltodict

def create_json_data_from_xml(source_file='CPdescarga.xml'):
    with open(source_file, 'r') as source:
        print(" >>>>>> Processing {} xml file".format(source_file))
        xml_data = xmltodict.parse(source.read())

    print(" >>>>>> building json structure")
    clean_data = {}

    for item in xml_data['NewDataSet']['table']:
        if item['d_codigo'] not in clean_data.keys():
            clean_data[item['d_codigo']] = {
                "zip_code": item['d_codigo'],
                "locality": item.get('d_ciudad', item['D_mnpio']),
                "federal_entity": {
                    "key": int(item['c_estado']),
                    "name": item['d_estado'],
                    "code": None
                },
                "settlements": [],
                "municipality": {
                    "key": int(item['c_mnpio']),
                    "name": item['D_mnpio']
                }
            }
        clean_data[item['d_codigo']]['settlements'].append({
            "key": int(item['id_asenta_cpcons']),
            "name": item['d_asenta'],
            "zone_type": item['d_zona'],
            "settlement_type": {
                "name": item['d_tipo_asenta']
            }
        })
    
    print(" >>>>>> saving json to data.json")
    with open('data.json', 'w') as destination:
        destination.write(json.dumps(list(clean_data.values())))

if '__main__' == __name__:
    create_json_data_from_xml()
