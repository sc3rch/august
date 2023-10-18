# def celsius_to_fahrenheit(celsius):
#     """ given a celsius value, returns conversion to fahrenheit """

#     fahrenheit = celsius * 9/5 + 32
#     return fahrenheit

# celsius = 25
# fahrenheit = celsius_to_fahrenheit(celsius)

# print(f"{celsius} Celsius to Fahrenheit is {fahrenheit}")

def fahrenheit_to_celsius(fahrenheit):
    """ given a fahrenheit value, returns conversion to celsius """

    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit = 82
celsius = fahrenheit_to_celsius(fahrenheit)

print(f"{fahrenheit} Fahrenheit to Celsius is {celsius}")