# Project_py
# Temperature Conversion README

## Overview
This README provides details on two approaches to temperature conversion between Celsius and Fahrenheit: a procedural approach and an object-oriented approach.

## Procedural Approach

### Code

```python
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Example usage
celsius_temp = 25
fahrenheit_temp = 77

# Converting Celsius to Fahrenheit
converted_to_fahrenheit = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is {converted_to_fahrenheit}°F")

# Converting Fahrenheit to Celsius
converted_to_celsius = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is {converted_to_celsius}°C")
```

### Description
The procedural approach uses standalone functions to perform the temperature conversions. 

- **celsius_to_fahrenheit(celsius)**: Converts a Celsius temperature to Fahrenheit.
- **fahrenheit_to_celsius(fahrenheit)**: Converts a Fahrenheit temperature to Celsius.

### Example Usage
In the provided example:
- A temperature of 25°C is converted to Fahrenheit, resulting in 77°F.
- A temperature of 77°F is converted to Celsius, resulting in 25°C.

## Object-Oriented Approach

### Code

```python
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# Example usage
celsius_temp = 25
fahrenheit_temp = 77

# Creating an instance of TemperatureConverter (although we use static methods, so it's not necessary)
converter = TemperatureConverter()

# Converting Celsius to Fahrenheit
converted_to_fahrenheit = converter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is {converted_to_fahrenheit}°F")

# Converting Fahrenheit to Celsius
converted_to_celsius = converter.fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is {converted_to_celsius}°C")
```

### Description
The object-oriented approach defines a `TemperatureConverter` class with static methods to perform the temperature conversions. 

- **celsius_to_fahrenheit(celsius)**: Converts a Celsius temperature to Fahrenheit.
- **fahrenheit_to_celsius(fahrenheit)**: Converts a Fahrenheit temperature to Celsius.

### Example Usage
In the provided example:
- A temperature of 25°C is converted to Fahrenheit, resulting in 77°F.
- A temperature of 77°F is converted to Celsius, resulting in 25°C.

## Conclusion
Both approaches effectively convert temperatures between Celsius and Fahrenheit. The choice between procedural and object-oriented methods depends on the specific requirements and design preferences of the project. The procedural approach is simpler and more straightforward, while the object-oriented approach provides a more structured and reusable design.