from random import randint, sample
import string
from getquote import get_quote

password = ""

words = []
quote = get_quote()
words = quote.split(' ')
first_letters = ""

for w in words:
    fl = w[:1]
    if fl != '':
        first_letters += fl

quote2 = get_quote()
words2 = quote2.split(' ')
words_add = []

for i in range(5):
    words_add.append(string.capwords(words2[randint(0, len(words2))]))

password += first_letters
password += string.punctuation[randint(0, len(string.punctuation))]
password += ''.join(words_add)
password += string.punctuation[randint(0, len(string.punctuation))]
password += ''.join(sample(string.digits, 6))

print(password)
