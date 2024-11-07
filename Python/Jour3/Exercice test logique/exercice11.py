def longestCommonPrefix(chaines):
    min_s = min(chaines)
    max_s = max(chaines)
    for i in range(len(min_s)):
        if max_s[i] != min_s[i]:
            return max_s[:i]
    return min_s[:]

chaines = ["flower", "flour", "flight"]

print(longestCommonPrefix(chaines))

# fl

chaines= ["apple", "appetite", "april"]

print(longestCommonPrefix(chaines))

# ap