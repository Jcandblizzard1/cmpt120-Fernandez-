from random import random

def main():
    ai = ["angry", "disgusted", "fearful", "happy", "sad", "suprised"]
    aiEmotion = int(random() * 6);
    C = [
        [1,0,4,3,3,3],
        [2,0,2,4,4,4],
        [0,1,2,4,4,2],
        [1,0,4,3,4,3]
    ]

    # Get the mode of interaction from the user
    # Params: none
    # Returns: an integer indicating one of reward, punish, joke, or threaten
    def getInteraction():
        cmd = input('I am ' + ai[aiEmotion] + ': ')
        if cmd == "reward":
            return 0
        elif cmd == "punish":
            return 1
        elif cmd == "threaten":
            return 2
        elif cmd == "joke":
            return 3
        else:
            return -1 # Invalid command
        
    # Based on a given emotion and action, determine the next emotional state
    # Params:
    # currEmotion - a current emotion
    # userAction - a user interaction
    # Returns: an emotion
    def lookupEmotion(currEmotion, userAction):
        return C[userAction][currEmotion]

    # loop
    while True:
        action = getInteraction()
        if action != -1:
            aiEmotion = lookupEmotion(aiEmotion, action)
        else:
            print("Invalid Command")

main()

    
    









