#!/usr/bin/env python3
"""Class that implements the LRU cache policy algorithm"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """caching system class that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.head, self.tail = '-', '='
        self.next, self.prev = {}, {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
        """handles the BaseCaching items"""
        self.next[head], self.prev[tail] = tail, head

    def evict_item(self, key):
        """evicts the least recently used cache item"""
        self.handle(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def add_item(self, key, item):
        """adds items to the cache items"""
        self.cache_data[key] = item
        self.handle(self.prev[self.tail], key)
        self.handle(key, self.tail)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.next[self.head]))
            self.evict_item(self.next[self.head])

    def put(self, key, item):
        """ Assign item value to the dictionary """
        if key and item:
            if key in self.cache_data:
                self.evict_item(key)
            self.add_item(key, item)

    def get(self, key):
        """ Return value linked to the key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            self.evict_item(key)
            self.add_item(key, value)
            return value
