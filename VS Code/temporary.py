# FUNCTIONS

def display_dict():
    print("Your current books:")
    for book, release_date in book_dict.items():
        print(f"Title: {book}, Release: {release_date}")

# MAIN

dict_size = int(input("How many books do you want to store?: "))
book_dict = {}

for i in range(dict_size):
    book_name = input("Enter book name: ")
    book_release = input(f'Enter "{book_name}" release date: ')
    book_dict[book_name] = book_release

display_dict()

with open("book_storage.txt",'w') as file_name:
    for book, release_date in book_dict.items():
        file_name.write(f"Title: {book}, Release: {release_date} \n")
    file_name.close()
      

