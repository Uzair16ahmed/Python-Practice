import sys

def word_frequency(words):
    """Returns frequency of each word given a list of words. 
            word_frequency(['a', 'b', 'a'])
            {'a': 2, 'b': 1}
    """

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
    """ 
    Regarding the line sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True), let's break it down:

    frequency.items(): This returns a list of tuples, where each tuple contains a word and its frequency, "extracted from the frequency dictionary".

    key=lambda x: x[1]: This specifies the key used for sorting. Here, "x represents each tuple in the list of items",
     and x[1] refers to the frequency (the second element of the tuple), indicating that we want to sort based on the frequency of each word.

    reverse=True: This parameter indicates that the sorting should be in descending order.

    Therefore, the entire line sorts the list of tuples based on the frequency (the second element of each tuple) in descending order, 
    resulting in a list of tuples sorted by frequency.
    """
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    # for key, value in frequency.items():
    #     print(key, value)
    for key, value in sorted_frequency:
        print(key, value)
if __name__ == "__main__":
    main()