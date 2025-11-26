
# Ask user for age
age_years = int(input("Enter your age in years: "))

# Convert
days = age_years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# Output
print(f"You are approximately:")
print(f"{days} days")
print(f"{hours} hours")
print(f"{minutes} minutes")
print(f"{seconds} seconds")
