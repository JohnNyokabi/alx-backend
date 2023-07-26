#!/usr/bin/env python3
"""Implements MRU Caching policy"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """caching system  Class that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.head, self.tail = 'head', 'tail'
        self.next, self.prev = {}, {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
        """handle elements in the MRU algorithm"""
        self.next[head], self.prev[tail] = tail, head

    def evict_item(self, key):
        """evict an item from the cache"""
        self.handle(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def add_item(self, key, item):
        """adding an item to the cache"""
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.prev[self.tail]))
            self.evict_item(self.prev[self.tail])
        self.cache_data[key] = item
        self.handle(self.prev[self.tail], key)
        self.handle(key, self.tail)

    def put(self, key, item):
        """Assign item value to the dictionary"""
        if key and item:
            if key in self.cache_data:
                self.evict_item(key)
            self._add(key, item)

    def get(self, key):
        """Return value linked to the key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            self.evict_item(key)
            self.add_item(key, value)
            return value
