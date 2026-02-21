print("Hello World")
print("I'm learning Python for Ai")
print("My name is Adwait Pimple")
print("Today is a great day to code!") 
import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200
