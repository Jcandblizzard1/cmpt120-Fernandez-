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

def plusminus(x):
   return x * -1

def square(x):
   return x * x

def inverse(x):
   return 1 / x

def power(x, y):
   return math.pow(x, y)

def cosine(x):
   return math.cos(x)

def sin(x):
   return math.sin(x)

def tan(x):
   return math.tan(x)

def tenpowerx(x):
   return x ** 10

def log(x):
   return math.log10(x)

def arcsne(x):
   return math.sin(math.pi / 2)

def arctne(x):
   return math.tan(math.pi / 2)

def arccsne(x):
   return math.cos(math.pi / 2)

##def openparen:
##   return (
##
##def closeparen:
##   return )

def const(x):
   return math.e(x)

def memplus(string, mem):
   string, mem = (float(string),float(mem))
   ans = add (string, mem)
   return str(ans)

def memsubtract(string, mem):
   string, mem = (float(string), float(mem))
   ans = subtract (string, mem)
   return str(ans)
   
def determine(string):
   try:
      string = str(eval(string))
      print('Evaled')
   except:
      print('except')
      if '+/-' in string:
         string = string.split('+/-')
         string = plusminus(float(string[0]))
         return string       
      elif '+' in string:
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
      elif 'x^y' in string:
         string = string.split('x^y')
         string = power(float(string[0]), float(string[1]))
         return string
      elif 'cos' in string:
         string = string.split('cos')
         string = cosine(float(string[0]))
         return string
      elif 'sin' in string:
         string = string.split('sin')
         string = sin(float(string[0]))
         return string
      elif 'tan' in string:
         string = string.split('tan')
         string = tan(float(string[0]))
         return string
      elif '10^x' in string:
         string = string.split('10^x')
         string = tenpowerx(float(string[0]))
         return string
      elif 'log' in string:
         string = string.split('log')
         string = log(float(string[0]))
         return string
      elif 'arcsne' in string:
         string = string.split('arcsne')
         string = arcsne(float(string[0]))
         return string
      elif 'arctne' in string:
         string = string.split('arctne')
         string = arctne(float(string[0]))
         return string
      elif 'arccsne' in string:
         string = string.split('arccsne')
         string = arccsne(float(string[0]))
         return string
##      elif '(' in string or ')' in string:
##         string = string.split('(')(')')
##         string = parentheses(float(string[0]), float(string[1]))
##         return string
      elif 'cont' in string:
         string = string.split('const')
         string = const(float(string[0]))
         return string
      return string
            

   
                    
   

   
      
            
