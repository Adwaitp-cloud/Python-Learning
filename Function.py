

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

from helpers import check_weather

temperature = int(input("Enter the temperature: "))
weather = check_weather(temperature)
print(weather)

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


from helpers import calculate_total

total = calculate_total(100)
print(total)
# function using return statement

def add_return (a ,b):
    return a + b

result = add_return(a= 55, b =45 )
print(result)

def calculate_area(height,width):
    area = height * width
    area = area * 1.05
    return area

room_area = calculate_area(12 ,10)
print(f"Room size: {room_area} sq ft")


def double(number):
    return number * 2

# Store in variable 
result = double(5)

# Use in expressions
total = double(5) + double(3)

# Pass to other functions
print(double(10))

# Use in conditions
if double(7) > 10:
    print("Big number!")


if double(3) < 10:
    print("Small number!") 


def simple_function():
    numbers = [1, 2, 3, 4, 5]
    first_num = numbers[0]
    last_num = numbers[-1]
    return first_num, last_num

f, l = simple_function()

print(f)
print(l)



def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")

result = get_min_max([34,65,4,12,785,1,2345,4554,4656,546])
print(result)


def greet(name):
    print(f"Hello, {name}!")
    # No return statement

result = greet("Adwait")  # Prints: Hello, Adwait!
print(result)  # None


def greet(name):
    return f"Hello, {name}!"
    # With return statement

result = greet("Adwait") # Stores the value
print(result)  # Hello, Adwait!

def tables (number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

table_number = int(input("Enter a number to see its multiplication table: "))