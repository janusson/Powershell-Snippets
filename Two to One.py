# Two to One.py

"""
Take 2 strings s1 and s2 including only letters from a to z. Return a new
sorted string, the longest possible, containing distinct letters,
each taken only once - coming from s1 or s2.
Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

# find unique letters in the combination of two strings

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
c = a + b  # string combo
twoToOne = []
for i in c:
    if i not in twoToOne:
        twoToOne.append(i)
print("Unique letters: ")
c.join(twoToOne)
