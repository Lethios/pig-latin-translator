import sys
import string

vowels: set = set("aAeEiIoOuU")
consonants: set = set(string.ascii_letters) - vowels
suffix_list = {0: "yay", 1: "way", 2: "hay"}

text: str = sys.argv[1]
word_list: list = text.split()
suffix: str = "yay" if len(sys.argv) < 3 else suffix_list[int(sys.argv[2])]

pig_word_list: list = []
for word in word_list:
    is_vowel = True if word[0] in vowels else False

    punctuation: str = ""
    if word[-1] not in vowels and word[-1] not in consonants:
        punctuation = word[-1]
        word = word[:-1]

    if is_vowel:
        pig_word_list.append(word + suffix + punctuation)
    else:
        temp: str = ""
        for i in range(len(word)):
            if word[i] not in vowels:
                temp += word[i]
            else:
                pig_word_list.append(word[i:] + temp.lower() + "ay" + punctuation)
                break

for index in range(len(pig_word_list)):
    if index == 0:
        print(pig_word_list[0].capitalize(), end=" ")
        continue
    print(pig_word_list[index], end=" ")