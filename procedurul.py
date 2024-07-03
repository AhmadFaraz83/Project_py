def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius_temp = 25
fahrenheit_temp = 77

converted_to_fahrenheit = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is {converted_to_fahrenheit}°F")

converted_to_celsius = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is {converted_to_celsius}°C")
