# CMPT 120 - Lab #6
# John Fernandez
# 19-March-2018
###
def showIntro():
       print("Welcome to the Arithmetic Engine!")
       print("=================================\n")
       print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'")
       
  
def doLoop():
    while True:
       cmd = input("What computation do you want to perform? ").lower()
       if cmd == 'quit':
              break             
       try:              
              num1 = int(input("Enter the first number: "))
              num2 = int(input("Enter the second number: "))
              if cmd == 'div':
                     num1 // num2
       except ValueError:
              print("Only use numbers")
              continue
       except:
              print("Can't divide by zero")
              continue
       if cmd == "add":
            result = num1 + num2
       elif cmd == "sub":
            result = num1 - num2
       elif cmd == "mult":
            result = num1 * num2
       elif cmd == "div":
           result = num1 // num2
       print("The result is " + str(result) + ".\n")

def showOutro():
       print("\nThank you for using the Arithmetic Engine...")
       print("\nPlease come back again soon!")

def main():
       showIntro()
       doLoop()
       showOutro()
main()
