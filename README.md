# Trie Data Structure - Homework Assignment

## Overview
This project focuses on implementing additional functionalities for the Trie data structure. The tasks involve extending the base Trie class to support suffix-based word counting and prefix existence checking. Additionally, the second task involves implementing a method to find the longest common prefix among a set of words.

## Task 1: Extending Trie Functionality

### Objectives
1. Implement a method `count_words_with_suffix(pattern)` to count the number of words ending with a given suffix.
2. Implement a method `has_prefix(prefix)` to check if there are any words with a given prefix.

### Technical Requirements
- The class `Homework` must inherit from the base `Trie` class.
- The methods must handle incorrect input data types.
- The input parameters must be strings.
- The method `count_words_with_suffix` must return an integer.
- The method `has_prefix` must return a boolean value.

### Acceptance Criteria
1. **`count_words_with_suffix` returns the correct count of words ending with the given suffix.** *(10 points)*
2. **Returns `0` if no words match.** *(10 points)*
3. **`has_prefix` returns `True` if at least one word with the given prefix exists, otherwise `False`.** *(10 points)*
4. **The implementation passes all provided tests.** *(10 points)*
5. **Incorrect input data is properly handled.** *(10 points)*
6. **Methods perform efficiently on large datasets.** *(10 points)*

## Task 2: Finding the Longest Common Prefix

### Objectives
1. Implement a class `LongestCommonWord` that inherits from `Trie`.
2. Implement a method `find_longest_common_word(strings)` that finds the longest common prefix among the input words.

### Technical Requirements
- The class `LongestCommonWord` must inherit from `Trie`.
- The input parameter `strings` must be a list of strings.
- The method `find_longest_common_word` must return a string representing the longest common prefix.
- Execution time should be **O(S)**, where **S** is the total length of all strings.

### Acceptance Criteria
1. **`find_longest_common_word` correctly finds the longest prefix common to all words.** *(10 points)*
2. **Returns an empty string if there is no common prefix.** *(10 points)*
3. **Handles empty arrays or invalid input correctly.** *(10 points)*
4. **The implementation passes all provided tests.** *(20 points)*

## Example Usage
```python
trie = Homework()
words = ["apple", "application", "banana", "cat"]
for i, word in enumerate(words):
    trie.put(word, i)

# Check suffix count
assert trie.count_words_with_suffix("e") == 1  # apple
assert trie.count_words_with_suffix("ion") == 1  # application
assert trie.count_words_with_suffix("a") == 1  # banana
assert trie.count_words_with_suffix("at") == 1  # cat

# Check prefix existence
assert trie.has_prefix("app") == True  # apple, application
assert trie.has_prefix("bat") == False
assert trie.has_prefix("ban") == True  # banana
assert trie.has_prefix("ca") == True  # cat

# Test Longest Common Prefix
trie = LongestCommonWord()
strings = ["flower", "flow", "flight"]
assert trie.find_longest_common_word(strings) == "fl"

trie = LongestCommonWord()
strings = ["interspecies", "interstellar", "interstate"]
assert trie.find_longest_common_word(strings) == "inters"

trie = LongestCommonWord()
strings = ["dog", "racecar", "car"]
assert trie.find_longest_common_word(strings) == ""

trie = LongestCommonWord()
strings = []
assert trie.find_longest_common_word(strings) == ""
```

## Expected Output
If implemented correctly, the assertions should pass without errors, confirming that all methods function as intended.

## Conclusion
By completing this assignment, you will understand how to:
- Traverse a Trie efficiently.
- Implement suffix-based searching in a Trie.
- Check for prefix existence using Trie traversal.
- Find the longest common prefix among words efficiently.


