# ⚡ High-Performance Zero-Dependency LRU Cache

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

An ultra-fast, zero-dependency **Least Recently Used (LRU) Cache** implementation in Python. Designed with $O(1)$ time complexity for both `get` and `put` operations using a Hash Map combined with a Doubly Linked List.

---

## 🚀 Features

* **$O(1)$ Time Complexity:** Constant time read and write performance.
* **Zero Dependencies:** Pure Python with no external libraries required.
* **Memory Efficient:** Automatic eviction of least recently used items when capacity is reached.

---

## 🛠️ Quickstart & Usage

```python
from lru_cache import LRUCache

# Initialize cache with a capacity of 2 items
cache = LRUCache(2)

cache.put("a", 1)
cache.put("b", 2)
print(cache.get("a"))  # Output: 1

cache.put("c", 3)      # Evicts key "b" (least recently used)
print(cache.get("b"))  # Output: None
# 🧊 Go 3D Model Generator

A lightweight, zero-dependency 3D model generator written in Go. 

It procedurally generates 3D geometry (such as roof panels and radiative cooling sheets) and exports them directly into standard `.obj` files that GitHub can render natively in 3D!

## 🚀 How to Generate the 3D Model

```bash
go run main.go
