# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Your Name Here
     # Created: YYYY-MM-DD
def main():
    
    # get user's first and last names
    first = input("Enter your first name: ").lower()
    last = input("Enter your last name: ").lower()
    # TODO modify this to generate a Marist-style username
    uname = first[0] + "." + last[:7] + "1"
    print(uname)
    # ask user to create a new password
    passwd = input("Create a new password: ")

    characters = len(passwd)
    upper = passwd.upper()
    lower = passwd.lower()
    # TODO modify this to ensure the password has at least 8 characters
    while characters < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
        characters = len(passwd)
    print("The force is strong in this one...")
    print("Account configured. Your new email address is", uname + "@marist.edu")
main()
