### A FILE THAT WAS CREATED ONLY FOR EDUCATIONAL PURPOSES, DON'T USE IN PRODUCTION ###
import re
from collections import Counter

a = 'Your  your your appatment out in Houston, \n Where I waited'
print(a)

print(a.split(' '))
print(re.split(' |\n', a))
print(Counter(a.split()))
print(len(Counter(a.split())))

print(len(a.split()))

def get_number_of_words(text):
    coll = Counter(text.split())
    c = 0
    for item in coll.values():
        c+=item
    return c

print(get_number_of_words(a))