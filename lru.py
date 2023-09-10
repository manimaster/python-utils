class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head, self.tail = Node(None, None), Node(None, None)
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove_node(self, node):
        """Remove a node from the doubly linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_node(self, node):
        """Add a node to the head of the doubly linked list."""
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev, self.head.next = node, node

    def get(self, key: int) -> int:
        """Get the value of the key if the key exists, otherwise return -1."""
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._add_node(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """Set or insert the value if the key is not already present."""
        if key in self.cache:
            # Remove the old value
            self._remove_node(self.cache[key])

        node = Node(key, value)
        self._add_node(node)
        self.cache[key] = node
        self.size += 1

        if self.size > self.capacity:
            # Remove the tail node
            node_to_remove = self.tail.prev
            self._remove_node(node_to_remove)
            del self.cache[node_to_remove.key]
            self.size -= 1

# Sample usage:
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1)) # returns 1
lru.put(3, 3)     # evicts key 2
print(lru.get(2)) # returns -1 (not found)
lru.put(4, 4)     # evicts key 1
print(lru.get(1)) # returns -1 (not found)
print(lru.get(3)) # returns 3
print(lru.get(4)) # returns 4
