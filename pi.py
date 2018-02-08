import math
def main():
    sign=1
    train=0
    n= int(input(" Enter number of terms to use: "))
    for i in range(1, n * 2 + 1, 2):
        result= 4/i * sign
        train = train + result 
        sign= sign * -1
    print(train)
    print ("pi=",math.pi)
    print ("The difference is", train-math.pi)
main()
