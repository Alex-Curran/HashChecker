import hashlib, os, time
title = """ _   _           _       _   _       _ _     _       _
| | | |         | |     | | | |     | (_)   | |     | |
| |_| | __ _ ___| |__   | | | | __ _| |_  __| | __ _| |_ ___  _ __
|  _  |/ _` / __| '_ \  | | | |/ _` | | |/ _` |/ _` | __/ _ \| '__|
| | | | (_| \__ \ | | | \ \_/ / (_| | | | (_| | (_| | || (_) | |
\_| |_/\__,_|___/_| |_|  \___/ \__,_|_|_|\__,_|\__,_|\__\___/|_|

                                                               """

def validate_file(file_name):
    try:
        open(file_name)
    except Exception as e:
        print("Invalid File! Check the location and try again!")
        time.sleep(5)
        main()
def compare_hash(computed_hash, user_hash,algorithm):
    os.system('cls')
    if(computed_hash == user_hash):
        print('Match!')
    else:
        print("No Match!")

    print(algorithm)
    print("Computed Hash = " + computed_hash)
    print("Supplied Hash = " + user_hash)

def hash(file_name, secure_hash):
    os.system('cls')
    print('Comptuing hash of ' + file_name + '\nDepending on the size of the file this may take a while!')
    with open(file_name, 'rb') as file:
        i = 1
        buffer_size = 4096
        buffer = file.read(buffer_size)
        while len(buffer) > 0:
            secure_hash.update(buffer)
            buffer = file.read(buffer_size)
        return secure_hash.hexdigest()
def main():
    os.system('cls')
    print(title)
    file_name = input("  What is the path of the file? (including extension!): ")
    file_name = file_name.strip(' \t\n\r')
    validate_file (file_name)
    user_hash = input("  What is the expected hash?")
    user_hash = user_hash.strip(' \t\n\r')
    print(" Select hashing algorithm")
    print("  1: sha1")
    print("  2: sha256")
    print("  3: md5")
    print("  0: Quit")
    user_input = input()

    if user_input == '1':
        hash_type = 'sha1'
        computed_hash = hash(file_name, hashlib.sha1())
    elif user_input == '2':
        hash_type = 'sha256'
        computed_hash = hash(file_name, hashlib.sha256())
    elif user_input == '3':
        hash_type = 'md5'
        computed_hash = hash(file_name, hashlib.md5())
    elif user_input == '0':
        print('Good Bye!')
        quit()
    else:
        print("Please try again!")
        time.sleep(5)
        main()

    compare_hash(computed_hash, user_hash, hash_type)
    user_continue = input("would you like to test another file(1) or quit(0)")
    if user_continue == '1':
        main()
    elif user_continue == '0':
        quit()
    else:
        print("Error!!")
        time.sleep(5)
        main()

main()
