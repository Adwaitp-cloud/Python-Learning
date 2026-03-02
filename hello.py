print("Hello World")
print("I'm learning Python for Ai")
print("My name is Adwait Pimple")
print("Today is a great day to code!") 
import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200

# Basic of file handling moodels read "r", write "w", append "a", create "x"

f = open("hello.txt", "x")
f = open("hello.txt", "r")
print(f.readline())
print(f.readline())
f = open("hello.txt", "a")
f.write("\nThis is line was added by using the append model.\n")
f = open("hello.txt", "r")
print(f.read())
f.close()



# 1D Array

import numpy as np 
a = np.array([1,2,3])
print(a)


# 2D Array

import numpy as np 
a = np.array([[1,2,3],[4,5,6]])
print(a)


try:
    # Read a number from a file
    with open('hello.txt', 'r') as f:
        text = f.read()
    number = int(text)
    result = 100 / number
    print(f"Result: {result}")
except FileNotFoundError:
    print("Could not find number.txt")
except ValueError:
    print("File doesn't contain a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")