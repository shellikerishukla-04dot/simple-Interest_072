import sys

if len(sys.argv) == 4:
    try:
        principal = float(sys.argv[1])
        rate = float(sys.argv[2])
        time = float(sys.argv[3])
        print("User provided input values:")
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        sys.exit(1)
else:
    print("No input given - using default values:")
    principal = 1000
    rate = 5
    time = 2

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display values
print("Principal =", principal)
print("Rate =", rate)
print("Time =", time)
print("Simple Interest =", simple_interest)
