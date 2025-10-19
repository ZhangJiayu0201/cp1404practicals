"""
Word Occurrences
Estimate: 20 minutes
Actual:   28 minutes
"""

text = input("Text: ")
words = text.split(" ")
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

keys = sorted(word_to_count.keys())
width = max(len(k) for k in keys)
for k in keys:
    print(f"{k:{width}} : {word_to_count[k]}")
