import json

def read_file(file_path, return_type='text'):
    with open(file_path, 'r') as file:
        content = file.read()

    if return_type == 'json':
        return json.loads(content)
    
    return content
