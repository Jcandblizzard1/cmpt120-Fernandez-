# This function adds, subtracts, multiplies and divides two numbers 
import math

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

def percentage(x):
   return x / 100

def squareroot(x):
   return math.sqrt(x)

def square(x):
   return x * x

def inverse(x):
   return 1 / x

def memplus(string, mem):
   string, mem = (float(string),float(mem))
   ans = add (string, mem)
   return str(ans)

def memsubtract(string, mem):
   string, mem = (float(string), float(mem))
   ans = subtract (string, mem)
   return str(ans)
   
def determine(string):
   if '+' in string:
      string = string.split('+')
      string = add(float(string[0]), float(string[1]))
      return string
   elif '-' in string:
      string = string.split('-')
      string = subtract(float(string[0]), float(string[1]))
      return string
   elif '*' in string:
      string = string.split('*')
      string = multiply(float(string[0]), float(string[1]))
      return string
   elif '/x' in string:
      string = string.split('/x')
      string = inverse(float(string[0]))
      return string
   elif '/' in string:
      string = string.split('/')
      string = divide(float(string[0]), float(string[1]))
      return string                     
   elif '%' in string:
      string = string.split('%')
      string = percentage(float(string[0]))
      return string
   elif '√' in string:
      string = string.split('√')
      string = squareroot(float(string[-1]))
      return string
   elif '^2' in string:
      string = string.split('^2')
      string = square(float(string[0]))
      return string
   

   
      
            
