import hashlib

find = 0
input_hash = input("Hashed password: ")
pass_doc = input("Insert dictionary: ")
try:
    pass_file = open(pass_doc, 'r')
except:
    print("ERROR" + pass_doc + " has not been found")

for word in pass_file:
    encrypted_word = word.encode('utf-8')
    hashed_word = hashlib.md5(encrypted_word.strip())
    digest = hashed_word.hexdigest()

    if digest == input_hash:
        print("Password found!!!! \n The password is: " + word)
        find = 1
        break
if not find:
    print("The password was not found. " + pass_doc)