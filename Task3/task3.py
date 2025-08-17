"""Задача 3. """

import json
import sys

def load_jsons(values_path, test_path):
    with open(values_path, 'r') as file:
        values_data = json.load(file)
    
    with open(test_path, 'r') as file:
        test_data = json.load(file)
    
    return values_data, test_data


def update_structure(test_data, values_dict):
    
    if isinstance(test_data, dict):
        if 'id' in test_data and test_data['id'] in values_dict:
            test_data['value'] = values_dict[test_data['id']]
        
        for key, value in test_data.items():
            test_data[key] = update_structure(value, values_dict)
    
    elif isinstance(test_data, list):
        for i in range(len(test_data)):
            test_data[i] = update_structure(test_data[i], values_dict)
    
    return test_data



def main():
    values_path = sys.argv[1]
    test_path = sys.argv[2]
    report_path = sys.argv[3]
    values_data, test_data = load_jsons(values_path, test_path)    
    values_dict = {item['id']: item['value'] for item in values_data['values']}  
    report_data = update_structure(test_data, values_dict)
    with open(report_path, 'w') as file:
        json.dump(report_data, file, indent=2, ensure_ascii=False)
        
    print(f"Отчет успешно сгенерирован в {report_path}")
    
   
if __name__ == "__main__":
    main()