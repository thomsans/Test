dict_size = int(input("Enter dictionary size: "))
user_dict = {}

for i in range(dict_size):
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    user_dict[key] = value

def displayDict():
    print(f"Updated Dictionary: {user_dict}")

while True:
    action = input("Choose Action ['add','delete','exit']: ").lower()

    if action == 'add':
        key = input("Enter a key: ")
        value = input("Enter a value: ")
        user_dict[key] = value
        displayDict()

    elif action == 'delete':
        key = input("Enter the key to delete: ")
        user_dict.pop(key)
        displayDict()

print(user_dict)