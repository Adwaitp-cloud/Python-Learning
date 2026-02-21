# This is a comment in python

'''
This is a  multi line 
quote that can be written 
in python
'''

first_name= "Chaitali"
age= 19
name= "Adwait"
is_student= True
print(first_name)


#Integers
total=20+5
power=10**2
print(power)

#Strings

string="My name is adwait"

full_name="""
Adwait Pimple
Chaitali Damodar
"""

first_name="Adwait"
last_name="Pimple"

full_name= first_name + " " + last_name

long_dash="-" * 13

print(full_name)
print(long_dash)

len(first_name)

is_logged_in = False
type(is_logged_in)

age = 17
can_vote= age >= 18


age = 25
has_license = False

# AND - both must be true
can_drive = age >= 16 and has_license
print(can_drive)


day = "Friday"

# OR - at least one shouuld be true
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)

num= 5
# NOT - reverse the value
is_even = num%2==0
is_odd = not is_even
print(f"{is_odd} it is an odd number")


name= "Adwait"

string= f"Hi there, my name is {name}"


text = "adwait pimple"

print(text.lower())
print(text.upper())
print(text.title())

sentence = f"hi my name is {text}"
print(sentence.title())