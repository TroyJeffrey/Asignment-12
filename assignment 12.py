# Troy Amegashie
# Assignment 12
# Regular Expressions
# 04.20.20

import re

word = input("Hi There! Type a word to proceed.\n>")

option = 0

while option != 11:
    print("What do you want to know about the word(s) you entered? Select one of the checks below.")
    print("1. Check if my word contains a 'q'")
    print("2. Check if my word contains 'the'")
    print("3. Check if my word contains a '*'")
    print("4. Check if my word contains a digit")
    print("5. Check if my word contains a '.'")
    print("6. Check if my word contains at least 2 consecutive vowels")
    print("7. Check if my word contains a 'white space'")
    print("8. Check if my word has any letters that repeat three times in a single word")
    print("9. Check if my word contains the word 'Hello'")
    print("10. Check if my word contains an email address")
    print("11. Exit the program.")

    option = int(input("\n > "))

    if option == 1:
        regex = '[q]'
        if re.search(regex, word):
            print("Check Complete : True")

        else:
                # If re.search() does not match, the check returns False
            print("Check Complete : False")

    elif option == 2:
        regex = 'the'
        if re.search(regex, word):
            print("Check Complete : True")
        else:
            print("Check Complete: False")

    elif option == 3:
        regex = '[*]'
        if re.search(regex, word):
            print("Check Complete : True")
        else:

            print("Check Complete : False")

    elif option == 4:
        regex = '[\d]'
        if re.search(regex, word):
            print("Check Complete :True")
        else:
            print("Check Complete : False")

    elif option == 5:
        regex = '[\.]'
        if re.search(regex, word):
            print("Check Complete : True")
        else:
            print("Check Complete : False")

    elif option == 6:
        #here i will the {2} to tell the program that the vowels need to be together.
        regex = '[aeiou]{2}'
        if re.search(regex, word):
            print("Check Complete : True")
        else:
            print("Check Complete : False")

    elif option == 7:
        regex = '\s'
        if re.search(regex, word):
            print("Check Complete : True")
        else:
            print("Check Complete : False")

    elif option == 8:
        regex = '.{3}'
        if re.match(regex, word):
            print("Check Complete : True")
        else:
            print("Check Complete : False")

    elif option == 9:
        # An expression to find 'Hello' at the beginning of the string.
        regex = "[^Hello]"
        if re.search(regex, word):
            print("Check Complete : True")
        else:
            print("Check Complete : False")

    elif option == 10:
        # An expression to match the input if it has '@' between two words
        regex = '\S+@\S+'
        if re.search(regex, word):
            print("Check Complete : True")
        else:
            print("Check Complete : False")
