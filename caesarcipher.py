#!/usr/bin/python3

#Created by: Breana J. Rabasca
#Updated on: March 29, 2022
#Filename: caesarcipher.py

#Program caesarcipher.py takes user input and
#encrypts it using a Caesar Cipher. Then the new
#message is printed to the screen. The user is
#prompted to start decryption. If validated, the
#possible messages are printed to screen.
#Repeatable.

#This simple Caesar Cipher will increment by set
#value within range of character type.
#[0-9],[a-z],[A-Z]

#Imports secrets module for random cipher pattern.
import secrets

#Function to return encrypted version of input text.
def encrypt(text):
    #Blank string for output.
    encrypt_msg = ""

    #cipher increment randomized.
    inc = secrets.randbelow(26)

    #For length of message:
    for i in text:
        value = ord(i)
        #Want to catagorize type of character:
        #Using Unicode character set table
        #(Only changing alphanumerics!)
        if i.isdigit():
            will_add = chr(((value + inc - 48) % 10) + 48)
        elif i.isupper():
            will_add = chr(((value + inc - 65) % 26) + 65)
        elif i.islower():
            will_add = chr(((value + inc - 97) % 26) + 97)
        else:
            will_add = i

        #Updated character is added to string.
        encrypt_msg += will_add
    
    return encrypt_msg

#Function to brute force decrypt the alphanumeric characters into keys.
def decryptAlphaNum(msg):
    keys = 0
    #traverse entire alphabet
    while (keys < 26):
        decrypt_msg = ""
        dec = 26 - keys
        #For each character in message: if alphanumeric
        #will try each cipher pattern.
        for i in msg:
            if i.isalnum():
                if i.isupper():
                    add_this = chr(((ord(i) + keys - 65) % 26) + 65)
                elif i.islower():
                    add_this = chr(((ord(i) + keys - 97) % 26) + 97)
                else:
                    add_this = chr(((ord(i) - dec - 48) % 10) +48)
            else:
                add_this = i
            decrypt_msg += add_this

        #Prints each cipher key.
        print(" \nKey " + str(keys) + ": " + decrypt_msg)
        keys = keys + 1

def main():
    usr_cont = ""

    #While user chooses to continue.
    while usr_cont not in ['NO','No','no','N','n']:
        #Prompt user for input.
        to_encrypt = input("\nEnter: \n")
        encrypt_msg = encrypt(to_encrypt)

        #Prints encrypted message to screen and asks
        #If decryption keys are wanted.
        print(" \nThe encrypted message is: \n" + encrypt_msg)
        print(" \nDo you want to decrypt the message? [y/n]")
        usr_dec = input()
        
        #If user chooses to continue:
        if usr_dec not in ['NO','No','no','N','n']:
            
            #Decrypts text into all possible keys.
            decryptAlphaNum(encrypt_msg)
    
        #Determines if while loop continues.
        usr_cont = input("\nDo you want to encrypt another message? [y/n]\n")

    print("\nProgram Completed.")
    return

main()
