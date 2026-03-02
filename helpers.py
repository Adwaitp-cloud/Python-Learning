def check_weather(temp):
    if temp > 30 :
        return "The weather is really hot!!"
    elif temp < 18 :
        return "The eather is cold!" 
    else :
        return "The weather is normal"


def calculate_total(price):
     # Default values
     tax_rate = 0.08  # local variables
     discount = 10
     # Calculation 
     tax=price * tax_rate
     final_price=price + tax - discount

     # Print the final  price
     return f"Total: ${final_price}"
