#!/usr/bin/python3
"""implements the Least Frequent Used Caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """caching system Class that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.lru_cache = OrderedDict()
        self.lfu_cache = {}

    def put(self, key, item):
        """Assign item value to the dictionary"""
        if key in self.lru_cache:
            del self.lru_cache[key]
        if len(self.lru_cache) > BaseCaching.MAX_ITEMS - 1:
            min_value = min(self.lfu_cache.values())
            lfu_keys = [k for k, v in self.lfu_cache.items() if v == min_value]
            if len(lfu_keys) == 1:
                print("DISCARD:", lfu_keys[0])
                self.lru_cache.pop(lfu_keys[0])
                del self.lfu_cache[lfu_keys[0]]
            else:
                for k, _ in list(self.lru_cache.items()):
                    if k in lfu_keys:
                        print("DISCARD:", k)
                        self.lru_cache.pop(k)
                        del self.lfu_cache[k]
                        break
        self.lru_cache[key] = item
        self.lru_cache.move_to_end(key)
        if key in self.lfu_cache:
            self.lfu_cache[key] += 1
        else:
            self.lfu_cache[key] = 1
        self.cache_data = dict(self.lru_cache)

    def get(self, key):
        """Return value linked to the key"""
        if key in self.lru_cache:
            value = self.lru_cache[key]
            self.lru_cache.move_to_end(key)
            if key in self.lfu_cache:
                self.lfu_cache[key] += 1
            else:
                self.lfu_cache[key] = 1
            return value
