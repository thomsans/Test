text = input("Enter a text: ")
letter_dict = {}

clean_text = text.replace(" ","")

for letter in text:
    if letter.isalpha():
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1

print(letter_dict)