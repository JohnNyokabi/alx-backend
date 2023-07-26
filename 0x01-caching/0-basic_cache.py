#!/usr/bin/env python3
"""Class BasicCache that inherits from BaseCaching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching with no limits"""
    def put(self, key, item):
        """
        assigns item value for the key to
        self.cache_data dictionary
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """returns the value"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
