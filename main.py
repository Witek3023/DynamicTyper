import string
import time

alphabet = list(string.ascii_uppercase + ' ')

word = input('Word to type: ')
out = []

for j in word.upper():
    for i in alphabet:
        if ''.join(out) == word.upper():
            print(''.join(out))
            break
        print(f"{''.join(out)} {i}")
        if i == j:
            out.append(i)
        time.sleep(0.02)
