#!/usr/bin/env python3
"""caching system class that inherits from BaseCaching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Uses self.cache_data to implement lifo cache access"""
    def __init__(self):
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """Assigns item value to the dictionary"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_key))
                self.cache_data.pop(self.last_key)
            self.last_key = key

    def get(self, key):
        """Return value linked to the key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
