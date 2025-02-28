from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern: str) -> int:
        """Підраховує кількість слів, що закінчуються на заданий суфікс."""
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string")

        all_words = self._get_all_words(self.root, "")  # Отримання всіх слів з Trie
        print(f"Усі слова у Trie: {all_words}")  # 🔍 Додано для дебагу
        return sum(1 for word in all_words if word.endswith(pattern))

    def has_prefix(self, prefix: str) -> bool:
        """Перевіряє, чи існує хоча б одне слово із заданим префіксом."""
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string")

        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def _get_all_words(self, node, prefix):
        """Рекурсивно збирає всі слова в Trie."""
        words = []
        if getattr(node, "is_end_of_word", False):  # Перевіряємо, чи це кінець слова
            words.append(prefix)

        for char, child in node.children.items():
            words.extend(self._get_all_words(child, prefix + char))

        return words


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # 🔍 Перевіряємо, чи правильно працює Trie
    print("Перевіряємо наявність доданих слів...")
    for word in words:
        assert trie.has_prefix(word[:2]) == True  # Має знаходити префікси

    # 🔍 Перевіряємо правильність пошуку за суфіксом
    print("Тестуємо count_words_with_suffix...")
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # 🔍 Перевіряємо префікси
    print("Тестуємо has_prefix...")
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

    print("✅ Всі тести пройдено успішно!")
