from collections import defaultdict

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
    main()