import sys

if len(sys.argv) == 4:
    principal = sys.argv[1]
    rate = sys.argv[2]
    time = sys.argv[3]
    print("User Provided input values:")
else:
    print("No input given - using default values:")
    principal = "10000"
    rate = "18"
    time = "2"

simple_interest = (eval(principal) * eval(rate) * eval(time)) / 100

print("Principal Amount:", principal)
print("Rate of Interest:", rate)
print("Time Period (years):", time)
print("Simple Interest =", simple_interest)
