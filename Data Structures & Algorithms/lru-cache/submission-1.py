class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Remove from current position
        node.prev.next = node.next
        node.next.prev = node.prev

        # Insert at the end (MRU)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            # Remove from current position
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node = Node(key, value)
            self.cache[key] = node

        # Insert at the end (MRU)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.head.next = lru.next
            lru.next.prev = self.head
            del self.cache[lru.key]