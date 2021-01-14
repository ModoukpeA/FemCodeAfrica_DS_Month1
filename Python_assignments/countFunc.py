"""
word = 'banana'
count = 0
for letter in word:
if letter == 'a':
count = count + 1
print(count)
"""

"""
Encapsulate this code in a function named count
and generalize it so that it accepts the string and the letter as arguments.
"""

def count (word,letter):
    i = 0
    for ltr in word:
        if ltr == letter:
            i +=1
    print(i)

print(count("choukou",'o'))
print(count("iamwhoyousayiam",'a'))