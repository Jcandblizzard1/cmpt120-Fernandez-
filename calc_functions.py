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
   return x ** 2

def inverse(x):
   return 1 / x

def power(x, y):
   return math.pow(x, y)

def cos(x):
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

def ln(x):
   return math.log(x)

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
      print(string)
      string = eval(str(string))

      return str(string)
   except:
      print('except')
   
   if 'sin' in string:
      i = string.index('sin')
      num = string[i-1:i]
      num = sin(float(num))
      string = determine(string[:i-1]+"("+str(num)+")")
      return string
   elif 'cos' in string:
      i = string.index('cos')
      num = string[i-1:i]
      num = cos(float(num))
      string = determine(string[:i-1]+"("+str(num)+")")
      return string
   elif 'tan' in string:
      i = string.index('tan')
      num = string[i-1:i]
      num = tan(float(num))
      string = determine(string[:i-1]+"("+str(num)+")")
      return string
   elif 'log' in string:
      i = string.index('log')
      num = string[i-1:i]
      num = log(float(num))
      string = determine(string[:i-1]+"("+str(num)+")")
      return string
   elif '/x' in string:
      i = string.index('/x')
      num = string[i-1:i]
      num = inverse(float(num))
      string = determine(string[:i-1]+"("+str(num)+")")
      return string
   elif '%' in string:
      i = string.index('%')
      num = string[i-1:i]
      num = percentage(float(num))
      string = determine(string[:i-1]+"("+str(num)+")")
      return string
   elif '√' in string:
      i = string.index('√')
      num = string[i-1:i]
      num = squareroot(float(num))
      string = determine(string[:i-1]+"("+str(num)+")")
      return string
   elif '^2' in string:
      i = string.index('^2')
      num = string[i-1:i]
      num = square(float(num))
      string = determine(string[:i-1]+"("+str(num)+")")
      return string
   elif '10^x' in string:
      i = string.index('10^x')
      num = string[i-1:i]
      num = tenpowerx(float(num))
      string = determine(string[:i-1]+"("+str(num)+")")
      return string
   elif 'arcsne' in string:
      i = string.index('arcsne')
      num = string[i-1:i]
      num = arcsne(float(num))
      string = determine(string[:i-1]+"("+str(num)+")")
      return string
   elif 'arctne' in string:
      i = string.index('arctne')
      num = string[i-1:i]
      num = arctne(float(num))
      string = determine(string[:i-1]+"("+str(num)+")")
      return string
   elif 'arccsne' in string:
      i = string.index('arccsne')
      num = string[i-1:i]
      num = arcsne(float(num))
      string = determine(string[:i-1]+"("+str(num)+")")
      return string
   elif 'ln' in string:
      i = string.index('ln')
      num = string[i-1:i]
      num = ln(float(num))
      string = determine(string[:i-1]+"("+str(num)+")")
      return string

   elif '+/-' in string:
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

   elif '/' in string:
      string = string.split('/')
      string = divide(float(string[0]), float(string[1]))
      return string                     
   elif 'x^y' in string:
      string = string.split('x^y') 
      string = power(float(string[0]), float(string[1]))
      return string
   return string
         


                 


