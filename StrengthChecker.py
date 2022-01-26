import string

password = input("Parola : ")

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
specials = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, specials, digits]
length = len(password)

score = 0

with open('trwordlist.txt', 'r') as f:
    wordlist = f.read().splitlines()

if password in wordlist:
    print("Parola bir türkçe wordlist'in içinde bulundu. Skor : 0 ")
    exit()

if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 15:
    score += 1
if length > 20:
    score += 1

print(f"Parola uzunluğu : {str(length)}, eklenen skor : {str(score)}")

if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1

print(f"Parola {str(sum(characters))} farklı karakter tipine sahip, eklenen skor : {str(sum(characters) - 1)}")

print(f"Toplam skor : {str(score)} / 7")
if score < 4:
    print("Parola zayıf.")
elif 4 <= score < 6:
    print("Parola iyi.")
elif score >= 6:
    print("Parola güçlü.")
