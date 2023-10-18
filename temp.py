def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 9/5

# celsius = 25
# fahrenheit = celsius_to_fahrenheit(celsius)

fahrenheit = 82
celsius = fahrenheit_to_celsius(fahrenheit)

# print(f"{celsius} Celsius to Fahrenheit is {fahrenheit}")

print(f"{fahrenheit} Fahrenheit to Celsius is {celsius}")