from collections import defaultdict

""" Problem 51: Write a function mutate to compute all words generated by a single mutation on a given word. A
mutation is defined as inserting a character, deleting a character, replacing a character, or swapping 2 consecutive
characters in a string. For simplicity consider only letters from a to z.
"""

# creating helper functions

def insert_char(word):
    mutated_words = []
    for i in range(len(word) + 1):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            mutated_words.append(word[:i] + char + word[i:])
    return mutated_words


def delete_char(word):
    mutated_words = []
    for i in range(len(word)):
        mutated_words.append(word[:i] + word[i+1:])
    return mutated_words

def replace_char(word):
    mutated_words = []
    for i in range(len(word)):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            mutated_words.append(word[:i] + char + word[i+1:])
    return mutated_words

def swap_char(word):
    mutated_words = []
    for i in range(len(word) - 1):
        mutated_words.append(word[:i] + word[i + 1] + word[i] + word[i+2:])
    return mutated_words



def mutate(word):
    if not word:
        raise ValueError("Word is Empty")
    all_mutations = set()
    all_mutations.update(insert_char(word))
    all_mutations.update(delete_char(word))
    all_mutations.update(replace_char(word))
    all_mutations.update(swap_char(word)) # Mutation of  hello  :  {'ehllo', 'hello', 'helol', 'hlelo'}

    return all_mutations

word = "hello"

mutations = mutate(word)

# print("Mutation of ", word, " : ", mutations)


""" Problem 52: Write a function nearly_equal to test whether two strings are nearly equal. Two strings a and
b are nearly equal when a can be generated by a single mutation on b. 
"""

def nearly_equal(word1, word2):
    if not word1 or not word2:
        raise ValueError("Word is Empty")
    
    mutations_of_word2 = mutate(word2)
    return word1 in mutations_of_word2

# string1 = "hello"
# string2 = "hallo"
# string1 = "python"
# string2 = "perl"
string1 = "python"
string2 = "jython"
# string1 = "man"
# string2 = "woman"

# print("Are", string1, "and", string2, "nearly equal?", nearly_equal(string1, string2))





""" Dictionaries """

""" 
Dictionaries are like lists, "but they can be indexed with non integer keys also". Unlike lists, dictionaries are not
ordered

"""
a = {
    'a': 1,
    'b': 2,
    'c': 3
}

# print(a['b']) 2

b = {}
b['x'] = 5
b[2] = 'foo'
b[(1, 2)] = 3

# print(b) # {'x': 5, 2: 'foo', (1, 2): 3}
# print(b[(1,2)]) # 3

""" The "del" keyword can be used to delete an item from a dictionary. """

del a['b']
# print(a) {'a': 1, 'c': 3}

del b[(1,2)]
# print(b) {'x': 5, 2: 'foo'}

""" The "keys method" returns all keys in a dictionary, the "values method" returns all values in a dictionary and
"items method" returns all key-value pairs in a dictionary. """

# print(a.keys()) dict_keys(['a', 'c'])
# print(a.values()) dict_values([1, 3])
# print(a.items()) dict_items([('a', 1), ('c', 3)])

""" The "for statement" can be used to iterate over a dictionary.
"""

# for key in a: print(key) a c

# for key, value in a.items(): print(key, value) a 1 c 3

""" Presence of a key in a dictionary can be tested using "in operator" or "has_key method." """

# print('c' in a) true

""" # print(a.has_key('c')) # deprecated since 2.3 now "in operator is used"
 """


""" Other useful methods on dictionaries are get and setdefault. """

d = {'x': 1, 'y': 2, 'z': 3}

# print(d.get('y', 'abc')) # 2
# print(d.get('a', 'abc')) # abc when key is not in the dictionary then given value is used

d.setdefault('p', 0)
# print(d) {'x': 1, 'y': 2, 'z': 3, 'p': 0}

""" Dictionaries can be used in "string formatting to specify named parameters". """

# print('hello %(name)s' % {'name': 'python'}) hello python

# print('chapter %(index)d: %(name)s' % {'index': 3, 'name': 'Data Structures'}) chapter 3: Data Structures



""" 
Example: Word Frequency
Suppose we want to find number of occurrences of each word in a file. Dictionary can be used to store the number
of occurrences for each word.
Lets first write a function to count frequency of words, given a list of words. 

"""

def word_frequency(words):
    """Returns frequency of each word given a list of words. 
            word_frequency(['a', 'b', 'a'])
            {'a': 2, 'b': 1}
    """

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# print(word_frequency(['a', 'b', 'a']))

# Getting words from a file is very trivial.

def read_words(filename):
    return open(filename).read().split()

# We can combine these two functions to find frequency of all words in a file.


def main():
    filename = sys.argv[1]
    words = read_words(filename)
    # print(word_frequency(words)) returns in the form of dictionary  {'She': 1, 'sells': 3, ...}
    frequency = word_frequency(words)
    for key, value in frequency.items():
        print(key, value) # return in form of key and value  sells 3

# if __name__ == "__main__":
#     main()


""" Problem 53: Improve the above program to print the words in the descending order of the number of occurrences. """

""" 
import sys

def word_frequency(words):
    # Returns frequency of each word given a list of words. 
    #         word_frequency(['a', 'b', 'a'])
    #         {'a': 2, 'b': 1}
    #

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Getting words from a file is very trivial.

def read_words(filename):
    return open(filename).read().split()

def main():
    filename = sys.argv[1]
    words = read_words(filename)
    # print(word_frequency(words)) 
    frequency = word_frequency(words)
    
    # Regarding the line sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True), let's break it down:

    # frequency.items(): This returns a list of tuples, where each tuple contains a word and its frequency, "extracted from the frequency dictionary".

    # key=lambda x: x[1]: This specifies the key used for sorting. Here, "x represents each tuple in the list of items",
    #  and x[1] refers to the frequency (the second element of the tuple), indicating that we want to sort based on the frequency of each word.

    # reverse=True: This parameter indicates that the sorting should be in descending order.

    # Therefore, the entire line sorts the list of tuples based on the frequency (the second element of each tuple) in descending order, resulting in a list of tuples sorted by frequency.
    # 
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    # for key, value in frequency.items():
    #     print(key, value)
    for key, value in sorted_frequency:
        print(key, value)
if __name__ == "__main__":
    main()
"""



"""  
Problem 54: Write a program to count frequency of characters in a given file. Can you use character frequency
to tell whether the given file is a Python program file, C program file or a text file?
"""


"""  
import sys
import string

def count_char_frequency(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            frequency = {char: text.count(char) for char in set(text)}
            return frequency
    except FileNotFoundError:
        print("File not Found")
        return None

def identify_file_type(char_frequency):
    # We can make some assumptions based on character frequencies
    # to determine the file type.
    if '#' in char_frequency and char_frequency['#'] > 10:
        return " Python program file"
    elif ';' in char_frequency and char_frequency[';'] > 10:
        return " C program file"
    else: 
        return " Text file"


def main():
    if len(sys.argv) != 2:
        print("Usage: python identify_file_type.py <filename>")
        return 

    filename = sys.argv[1]
    char_frequency = count_char_frequency(filename)
    print(identify_file_type(char_frequency))

if __name__ == "__main__":
    main()
"""

"""  
Problem 55: Write a program to find anagrams in a given list of words. Two words are called anagrams if one
word can be formed by rearranging letters of another. For example ‘eat’, ‘ate’ and ‘tea’ are anagrams.
"""

#understanding required
""" from collections import defaultdict

def find_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        print(sorted_word)
        anagrams[sorted_word].append(word)
        print(anagrams)
    
    return [anagram_group for anagram_group in anagrams.values() if len(anagram_group)> 1]

def main():
    # words = ["eat", "tea", "tan", "ate", "eat", "tea", "tan", "ate"]
    words = ["eat", "ate", "tea", "hello", "world", "cat", "act", "listen", "silent"]

    anagram_groups = find_anagrams(words)

    if anagram_groups:
        print("Anagram groups found:")
        for group in anagram_groups:
            print(group)
    else:
        print("No anagram groups found.")

if __name__ == "__main__":
    main() """