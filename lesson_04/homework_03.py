# Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,
# которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.
# Написать также функцию xor_decipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.


# Defining function
def xor_cipher(s, key):
    s = ''.join([bin(ord(s[i]))[2:] for i in range(len(s))])
    string_array = list(s)
    print(string_array)
    key = ''.join([bin(ord(s[i]))[2:] for i in range(len(key))])
    key_array = list(key)
    for i in range(len(string_array)):
        if int(string_array[i]) + int(key_array[i]) == 1:
            
    print(key_array)


# Defining required vars
s = input(f"Input a phrase for ciphering: ")
print(f"Length of your phrase is: {len(s)}")
key = input(f"Input same length key: ")
print(f"Length of your key is: {len(key)}")
# if len(key) != len(s):
#     while True:
#         key = input(f"Wrong length! Try again: ")
#         if len(key) == len(s):
#             print(f"Length of your key is: {len(key)}")
#             break
#         else:
#             print(f"Length of your key is: {len(key)}")
#             continue
print(s)

# Calling out function for print
xor_cipher(s, key)
