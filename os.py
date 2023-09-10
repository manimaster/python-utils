import os
import json
import zipfile
import psutil

def gather_system_info(os_type='centos'):
    data = {
        'memory': dict(psutil.virtual_memory()._asdict()),
        'cpu': dict(psutil.cpu_stats()._asdict())
    }

    log_files = {
        'centos': ['/var/log/messages', '/var/log/syslog'],
        'windows': []  # Windows logs are more complex and need other methods
    }

    with zipfile.ZipFile('system_info.zip', 'w') as zipf:
        zipf.writestr('system_info.json', json.dumps(data))
        
        for log in log_files.get(os_type, []):
            if os.path.exists(log):
                zipf.write(log)

    return 'system_info.zip'
