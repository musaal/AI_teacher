import json

# Replace with the path to your JSON file
file_path = 'C:/Users/NTC/Desktop/scrping_data/3blue1brown_lessons_scraped_2.json'

with open(file_path, 'r') as file:
    data = json.load(file)

def count_keys(obj):
    if isinstance(obj, dict):
        return len(obj)
    elif isinstance(obj, list):
        return sum(count_keys(item) for item in obj)
    return 0

key_count = count_keys(data)
print(f'Total number of keys: {key_count}')

def print_structure(obj, indent=0):
    if isinstance(obj, dict):
        for key, value in obj.items():
            print('  ' * indent + str(key))
            print_structure(value, indent + 1)
    elif isinstance(obj, list):
        for index, item in enumerate(obj):
            print('  ' * indent + f'[{index}]')
            print_structure(item, indent + 1)

print('JSON Structure:')
print_structure(data)