# Task 1
#Calculate the area of a rectangle from user input.
length = int(input("enter the length: "))
breadth = int(input("enter the breadth: "))
def rectangle(length,breadth):
    if length > 0 and breadth > 0:
        return print(length*breadth)
    else:
        print("please enter a Non zero integer")
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