# Task 1
#Calculate the area of a rectangle from user input.
length = int(input("enter the length: "))
breadth = int(input("enter the breadth: "))
def rectangle(length,breadth):
    if length > 0 and breadth > 0:
        return print(length*breadth)
    else:
        return print("please enter a Non zero integer")
rectangle(length,breadth)


# Task 2
# Print numbers from 1 to 20 divisible by 3
n = int(input("enter the number : "))
for i in range(n):
    if i == 0:
        continue #continue is removed the will get 0 in the output
    if i % 3 == 0:
        print(i)

# Task 3
# Function to check if a number is even or odd.
even_odd = int(input("enter the number to check even or odd: "))
def oddeven(even_odd):
    if even_odd % 2 == 0:
         print(f"{even_odd} is even")
    else:
         print(f"{even_odd} is odd")
oddeven(even_odd)
# Task 4
# Take 3 numbers from user and print the largest.
checknum_1 = int(input("enter the number 1 to check: "))
checknum_2 = int(input("enter the number 2 to check: "))
checknum_3 = int(input("enter the number 3 to check: "))
print(f"{max(checknum_1,checknum_2,checknum_3)} is the largest number")

#Task 5
# Create a dictionary for 5 cities and their populations, then print them.
city = {"Delhi":500,"Kol":400,"Chennai":300,"blr":600,"Gujrat":200}
print(city)

# --After review
# day1_practice.py
# 30 Days Python Mastery - Day 1 Practice Tasks

def rectangle_area(length: int, breadth: int) -> int:
    """Return area of rectangle if positive values, else None."""
    if length > 0 and breadth > 0:
        return length * breadth
    return None

def numbers_divisible_by_3(n: int) -> list[int]:
    """Return a list of numbers from 1 to n divisible by 3."""
    return [i for i in range(1, n + 1) if i % 3 == 0]

def check_even_odd(num: int) -> str:
    """Return 'even' or 'odd' based on the number."""
    return "even" if num % 2 == 0 else "odd"

def largest_of_three(a: int, b: int, c: int) -> int:
    """Return the largest of three numbers."""
    return max(a, b, c)

def display_cities_population(cities: dict[str, int]):
    """Print each city and its population in a formatted way."""
    print("City populations:")
    for city, population in cities.items():
        print(f"{city}: {population:,}")  # adds comma for readability

def main():
    # Task 1: Rectangle Area
    length = int(input("Enter rectangle length: "))
    breadth = int(input("Enter rectangle breadth: "))
    area = rectangle_area(length, breadth)
    if area:
        print(f"Area of rectangle: {area}")
    else:
        print("Please enter positive non-zero integers.")

    print("\n" + "-"*30 + "\n")

    # Task 2: Numbers divisible by 3
    n = int(input("Enter a number to list numbers divisible by 3: "))
    divisible_numbers = numbers_divisible_by_3(n)
    print(f"Numbers divisible by 3 up to {n}: {divisible_numbers}")

    print("\n" + "-"*30 + "\n")

    # Task 3: Even or Odd
    number = int(input("Enter a number to check even or odd: "))
    result = check_even_odd(number)
    print(f"{number} is {result}")

    print("\n" + "-"*30 + "\n")

    # Task 4: Largest of 3 numbers
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    num3 = int(input("Enter number 3: "))
    print(f"Largest number is: {largest_of_three(num1, num2, num3)}")

    print("\n" + "-"*30 + "\n")

    # Task 5: Cities and populations
    cities = {
        "Delhi": 5000000,
        "Kolkata": 4000000,
        "Chennai": 3000000,
        "Bangalore": 6000000,
        "Gujarat": 2000000
    }
    display_cities_population(cities)

if __name__ == "__main__":
    main()
# best we practices