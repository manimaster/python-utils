import time

class TTLCache:
    def __init__(self):
        self.cache = {}
        self.cleanup_interval = 300  # 5 minutes

    def set(self, key, value, ttl):
        expire_time = time.time() + ttl
        self.cache[key] = (value, expire_time)
    
    def get(self, key):
        if key in self.cache:
            value, expire_time = self.cache[key]
            if time.time() <= expire_time:
                return value
            else:
                del self.cache[key]
        return None

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
    
    def cleanup(self):
        current_time = time.time()
        keys_to_delete = [key for key, (_, expire_time) in self.cache.items() if current_time > expire_time]
        for key in keys_to_delete:
            del self.cache[key]

    def start_cleanup(self):
        while True:
            time.sleep(self.cleanup_interval)
            self.cleanup()
