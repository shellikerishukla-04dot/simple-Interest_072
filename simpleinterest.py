import sys

if len(sys.argv) == 4:
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
    print("user provided input values:")
else:
    print("No (or not enough) input given - using default values")
    principal = 1000.0
    rate = 5.0
    time = 2.0

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Print results
print("Principal Amount:", principal)
print("Rate of Interest (% per annum):", rate)
print("Time Period (years):", time)
print("Simple Interest =", simple_interest)
