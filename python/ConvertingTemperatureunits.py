# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Sample input
temperature_celsius = 30

# Convert to Fahrenheit
temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)

# Convert to Kelvin
temperature_kelvin = celsius_to_kelvin(temperature_celsius)

# Print the results
print(f"Temperature in Fahrenheit: {temperature_fahrenheit}")
print(f"Temperature in Kelvin: {temperature_kelvin}")
