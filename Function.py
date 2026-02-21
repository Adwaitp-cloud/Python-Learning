

def greet():
    print("Hello!")
    print("Hello again!")


greet()


def say_goodbye():
    print("Goodbye!")
    print("See you later!")

# Call it multiple times
say_goodbye()
say_goodbye()
say_goodbye()


def check_weather(temperature):
    if temperature > 30:
        print("The weather is really hot!!")
    elif temperature < 18:
        print("The weather is cold!")
    else:
        print("The weather is normal")


temperature = int(input("Enter the temperature"))
check_weather(temperature)


def greet(first_name,last_name):
     print(f"Hello, {first_name} {last_name}")

greet(first_name="Adwait",last_name="Pimple")
greet("Adwait","Pimple")


def greet(first_name="Adwait",last_name="Pimple"):
     print(f"Hello, {first_name} {last_name}")

greet()
greet(first_name="Dave")
greet(last_name="John")
greet(first_name="Dave",last_name="John")


def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

# Order matters!
calculate_total(100, 0.08, 10)  # $98



discount=10  # Global Variable

def calculate_total(price):
     # Default values
     tax_rate=0.08  # local variables

     # Calculation 
     tax=price * tax_rate
     final_price=price + tax - discount

     # Print the final  price
     print(f"Total: ${final_price}")

calculate_total(100)

# function using return statement

def add_return (a ,b):
    return a + b

result = add_return(a= 55, b =45 )
print(result)

def calculate_area(height,width):
    area = height * width
    return area

room_area = calculate_area(12 ,10)
print(f"Room size: {room_area} sq ft")


def double(number):
    return number * 2

# Store in variable
result = double(5)

# Use in expressions
total = double(5) + double(3)  # 10 + 6 = 16

# Pass to other functions
print(double(10))  # 20

# Use in conditions
if double(7) > 10:
    print("Big number!")