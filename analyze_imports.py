# Save as analyze_imports.py
import os
import re

def find_imports():
    imports = set()
    pattern = re.compile(r'^import\s+([a-zA-Z0-9_.]+)|^from\s+([a-zA-Z0-9_.]+)\s+import')
    
    for root, _, files in os.walk('.'):
        if '__pycache__' in root or 'venv' in root:
            continue
        for file in files:
            if file.endswith('.py') and file != 'test.py':
                try:
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        for line in f:
                            match = pattern.match(line.strip())
                            if match:
                                module = match.group(1) or match.group(2)
                                top_level = module.split('.')[0]
                                imports.add(top_level)
                except Exception as e:
                    print(f'Error processing {filepath}: {e}')
    
    return sorted(imports)

if __name__ == '__main__':
    print('Packages imported in your code:')
    for imp in find_imports():
        if not imp in ['os', 're', 'sys', 'time', 'math', 'json', 'datetime']:
            print(imp)