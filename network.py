import psutil
import json

def get_network_info(adapters=None, data_type='string'):
    if adapters is None:
        adapters = []
    
    interfaces = psutil.net_if_addrs()
    
    data = {k: v for k, v in interfaces.items() if not adapters or k in adapters}
    
    if data_type == 'json':
        return json.dumps(data)
    
    return str(data)
