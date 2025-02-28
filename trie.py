class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None
        self.is_end_of_word = False  # ✅ Додаємо атрибут для позначення кінця слова


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def put(self, key, value=None):
        if not isinstance(key, str) or not key:
            raise TypeError(
                f"Illegal argument for put: key = {key} must be a non-empty string"
            )

        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        if current.value is None:
            self.size += 1
        current.value = value
        current.is_end_of_word = True  # ✅ Позначаємо кінець слова

    def get(self, key):
        if not isinstance(key, str) or not key:
            raise TypeError(
                f"Illegal argument for get: key = {key} must be a non-empty string"
            )

        current = self.root
        for char in key:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.value
