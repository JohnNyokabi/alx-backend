#!/usr/bin/env python3
"""A caching system class that inherits from BaseCaching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.data = {}
        self.hit_next, self.evict_item = 0, 0

    def _pop(self):
        """remove an item"""
        self.evict_item += 1
        key = self.data[self.evict_item]
        del self.data[self.evict_item], self.cache_data[key]

    def _push(self, key, item):
        """add an item to the dictionary"""
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.data[self.evict_item + 1]))
            self._pop()
        self.cache_data[key] = item
        self.hit_next += 1
        self.data[self.hit_next] = key

    def put(self, key, item):
        """ Assigns item value to the dictionary """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self._push(key, item)

    def get(self, key):
        """ Return the value linked to key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
