"""
Word Occurrences
Estimate: 30 minutes
Actual:   23 minutes
"""

text = input("Text: ")
words = text.split(" ")
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

keys = sorted(counts.keys())
width = max(len(k) for k in keys)
for k in keys:
    print(f"{k:{width}} : {counts[k]}")
