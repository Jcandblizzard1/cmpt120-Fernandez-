answer = 'gorilla'
guess = input("guess an animal")


while True:
    if guess [0] == 'q':       
       print ("bye")
       break
    if guess != answer:
        print("give it another try")

    elif guess == answer:
        print ("congrats")
        break
    
    
