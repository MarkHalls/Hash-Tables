# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def find(self, key):
        if self.key is key:
            return self.value
        if self.next is None:
            return None

        return self.next.find(key)

    def for_each(self, cb):
        if self.next is None:
            return cb(self.key, self.value)
        cb(self.key, self.value)
        self.next.for_each(cb)

    def append(self, key, value):
        if self.key is key:
            self.value = value
            return
        if self.next is None:
            self.next = LinkedPair(key, value)
            return
        self.next.append(key, value)

    def delete(self, key):
        if self.key is key:
            return self.next
        self.next = self.next.delete(key)
        return self


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return hash(key)

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)
        """
        """
        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        """
        self.count += 1
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            return self.storage[index].append(key, value)
        self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        """
        self.count -= 1
        index = self._hash_mod(key)

        if self.storage[index] is None:
            return print(f"Warning: key {key} not found")

        # delete returns the entire list tree after removing the correct node
        self.storage[index] = self.storage[index].delete(key)

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        """
        if self.storage[self._hash_mod(key)] is None:
            return None

        # find returns None if key doesn't exist
        return self.storage[self._hash_mod(key)].find(key)

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        """
        self.capacity *= 2

        # create a temporary hash table we can insert to with new capacity
        temp = HashTable(self.capacity)

        for item in self.storage:
            if item is not None:
                # use the new hash tables insert method to hash keys on every node
                item.for_each(temp.insert)
        # replace current storage with new hash tables storage
        self.storage = temp.storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
