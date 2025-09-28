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
    if word[0] in vowels:
        pig_word_list.append(word + suffix)
    else:
        temp: str = ""
        for i in range(len(word)):
            if word[i] not in vowels:
                temp += word[i]
            else:
                pig_word_list.append(word[i:] + temp.lower() + "ay")
                break

print(pig_word_list)