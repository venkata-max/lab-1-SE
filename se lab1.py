def temperature_modeling(a, b, c, time):
    # Calculate temperature based on time using the quadratic equation
    temperature = a * time**2 + b * time + c
    return temperature



a_hardcoded, b_hardcoded, c_hardcoded = 0.1, 2, 10

# Display results
print(" Hard-coded Variables for Weather Modeling")
time_hardcoded = 5  # Example time value
print("Temperature for hardcoded coefficients at time", time_hardcoded, "hours:", temperature_modeling(a_hardcoded, b_hardcoded, c_hardcoded, time_hardcoded))
print("\n")

print(" Keyboard Input for Weather Modeling")

a_keyboard = float(input("Enter coefficient a: "))
b_keyboard = float(input("Enter coefficient b: "))
c_keyboard = float(input("Enter coefficient c: "))

# Get time from user input
time_keyboard = float(input("Enter time in hours: "))

# Display results
print("Temperature for keyboard input coefficients at time", time_keyboard, "hours:", temperature_modeling(a_keyboard, b_keyboard, c_keyboard, time_keyboard))
print("\n")



with open('weather.txt', 'r') as file:
    lines = file.readlines()
    a_file, b_file, c_file, time_file = map(float, lines[0].split())

# Display results
print("Read from a File for Weather Modeling")
print("Temperature for file input coefficients at time", time_file, "hours:", temperature_modeling(a_file, b_file, c_file, time_file))
print("\n")
