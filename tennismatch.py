# tennisplayer.py
from random import *

class Player:
    def __init__(self, probability):
        self.probability = probability
        self.score = 0
        self.thescore = 0
        self.setscore = 0
        self.setswon = 0

    def winsServe(self):
        # Returns true with probability self.prob
        return random() <= self.probability

    def incScore(self):
        # Add a pouint to this player's score
        self.score = self.score + 1

    def getScore(self):
        # Return this player's current score
        return self.score

    def getGameScore(self):
        return self.thescore

    def resetGame(self):
        self.thescore = 0

    def incSetScore(self):
        self.setscore += 1

    def getSetScore(self):
        return self.setscore

    def incSetWon(self):
        self.setswon += 1

    def getSetsWon(self):
        return self.setswon

    def incGScore(self):
        if self.thescore == 0:
            self.thescore = 15
        elif self.thescore == 15:
            self.thescore = 30
        elif self.thescore == 30:
            self.thescore = 40
        elif self.thescore == 40:
            self.thescore = 1
