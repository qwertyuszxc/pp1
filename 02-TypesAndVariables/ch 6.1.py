word = input('Input word ')
i = len(word)+1
while 0-len(word) != len(word)+1-i:
    letter = word[len(word)-i]
    i = i+1
    print(letter)