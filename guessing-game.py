answer = "geurilla"

#Guess an animal and get the correct answer
while True:
 
    print("Guess an animal I am thinking of")
    guess = input().lower()
    if guess == answer:
        print("Congradulations, you guessed the animal I was thinking of")
        animal = input("Do you like this animal (Yes or no)?")
        if animal == 'y' or animal == 'yes':
            print ('you are not stupid')
            break
        if animal == 'n' or animal == 'no':
            print ('you are stupid')
            break
    if guess [0] == 'q':
        print("Goodbye") 
        break                     
#Guess animal and get the wrong answer
    else:
        print("Give it another try" )
