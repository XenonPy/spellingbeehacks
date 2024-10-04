from english_words import get_english_words_set
web2lowerset = list(get_english_words_set(['web2'], lower=True, alpha=True))
letters = ['', '', '', '', '', '', '']
center = input("Please enter the center letter: ")
letters[0] = center

for i in range(1, len(letters)):
        print(i)
        letter = input("Please input the next letter: ")
        letters[int(i)] = letter

print(letters)
foundWords = []
idx = 0
for item in web2lowerset:
        buffer = 0
        for char in item:
                if char not in letters:
                        buffer += 1
        if buffer == 0 and len(item) >= 4 and center in item:
                foundWords.append(item)
        idx += 1 
print(foundWords)
