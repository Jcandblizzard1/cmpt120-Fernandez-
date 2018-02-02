# File: chaos.py
# A simple prograam illustrating chaotic behavior

def main():
    print("this program illustrates a chaotic function")
    x=eval(input(".5: "))
    for i in range(10) :
        x = 3.9 * x * (1 - x)
        y = 3.9 * x - (3.9 * y) * y
        print(x)
        print(y)
