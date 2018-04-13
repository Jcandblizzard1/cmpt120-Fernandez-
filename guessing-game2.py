answer = "gorilla"
guess = input("Guess an animal? ")
#Guess an animal and get the correct answer
while True:
    if guess[0] == "q":
        print("Goodbye")
        break
    elif guess == answer:
        print("Congrats you guessed it right! ")
        break
    else:
        guess = input("Give it another try ")
        
