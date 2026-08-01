# File: main.py
import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_basic_get_and_put(self):
        cache = LRUCache(2)
        cache.put("a", 100)
        self.assertEqual(cache.get("a"), 100)

    def test_eviction_policy(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.get("a")  # Moves 'a' to front, making 'b' least recently used
        cache.put("c", 3)  # Evicts 'b'

        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("a"), 1)
        self.assertEqual(cache.get("c"), 3)

    def test_overwrite_existing_key(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("a", 99)  # Update value
        self.assertEqual(cache.get("a"), 99)

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            LRUCache(0)


if __name__ == "__main__":
    print("Running automated unit tests...")
    unittest.main()
