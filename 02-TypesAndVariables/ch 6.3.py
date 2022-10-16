word = input('Write down the word: ')
letter = input('Write down letter: ')
count = 0
for letter1 in word:
    if letter1 == letter:
        count = count+1
print(count)