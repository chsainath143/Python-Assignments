# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    return principal * rate * time / 100

# Get customer details
gender = input("Enter customer gender (M or F): ")
age = int(input("Enter customer age: "))
principal = float(input("Enter fixed deposit amount: "))
time = int(input("Enter time duration (in years): "))

# Calculate interest rate based on customer's gender and age
if gender == "F" and age >= 60:   # Senior citizen female
    rate = 8
elif gender == "F" and age < 60:  # Non-senior citizen female
    rate = 6
elif gender == "M" and age >= 60: # Senior citizen male
    rate = 7
else:                            # Non-senior citizen male
    rate = 5

# Calculate simple interest
interest = calculate_simple_interest(principal, rate, time)

# Print output
print("Customer gender: ", gender)
print("Customer age: ", age)
print("Fixed deposit amount: ", principal)
print("Interest rate: ", rate)
print("Time duration (years): ", time)
print("Simple interest earned: ", interest)
