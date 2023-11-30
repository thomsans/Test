sentence = input("Enter a sentence: ")
word_dict = {}

for word in sentence.split():
    if word.lower() in word_dict:
        word_dict[word.lower()] += 1
    elif word.lower():
        word_dict[word.lower()] = 1

print(word_dict)