#Strings - Day 2 Learning
# Strings are sequence of characters : indexable,iterable,sliceable
from tkinter.font import names

from Tools.scripts.generate_global_objects import Printer

#Basic Operation
text = " Python MasTery " #see we added space before and after inside the text variable
print(text) #this will give us simple print of string value in the variable with whitespaces
print("Length", len(text)) #here the first and basic function we see is len() which count length of the value including space
#stripping spaces
print(text.strip()) #strip() removes whitespaces

#case conversions
print(text.lower()) #changes into lowercase
print(text.upper()) #changes into uppercase
print(text.title()) #Makes Fist letter of the word uppercases as a title

#slicing and Indexing - Slicing refers to slicing the words in specific was like "python" can be sliced into "thon"
#indexing refers to the place value a character of the string lies like "Python" here at 0 place "P" is present.
Name = "AnkitDS"
print(Name[0]) #this gives out A as at zero position A is present.
print(Name[-1]) #this gives out S at we added negative side so it look from right to left at 1 position "S" is present
print(Name[1:5]) #here we nkit why? as counting starts from 0 but still you can say it would be "nkitD" right? but no its a range last of value in a ranger is exclusive.

#Spliting and Joining
items = "apples, bananas, oranges"
fruits = items.split(",") #splits divides each words and the identfier we gave is comma"," here so its split the value into a list of items present in the variable
print(fruits) #['apples', ' bananas', ' oranges']
print(" - ".join(fruits)) #apples -  bananas -  oranges # we giving identifier for joining the values in the list

#replace
print("Hi AnkitDS!!".replace("Hi"," Bonjure "))

#Section 2 List Basics List are declared in [] square parethesis its a support for Arrays in python we dont have in-built Arrays
numbers = [10,20,30,40,50,60]
print(numbers)
print("First", numbers[0])
print("Last", numbers[-1])
print("slice", numbers[1:4])

#Adding items in the list
numbers.append(70) #directly inserted the value in the list
print(numbers)
numbers.insert(3,90) #inserts the value at specific placeholder
print(numbers)

#Removing Items from List
numbers.remove(20)
print(numbers) #directly removes 20
numbers.pop() #removes last placeholder value in this case 70
print(numbers)
numbers.pop(-2) #we can provide index what to remove in this case 50
print(numbers)
numbers.clear() #clear the list elements gives out [] known as empty list
print(numbers)
numbers = [10,20,30,40,50,60]
numbers.reverse() #reverse the list
print(numbers)
numbers.sort() #sorts the list
print(numbers)

#Loping + List Comprehension

#looping through the list
names = ["Ankit","Meera", "Rajesh"]
for n in names:
    print(n.title()) #iterates each names one by one like placing the first value on then n.it goes to second function title and do till end of list

#index + Value
for i,n in enumerate(names):
    print(i,n) #returns combination of Index and values

#list comprehension
square = [x*x for x in range(1,10)] # this type of short hand in python within list we define the function/steps and it iterates it as a list
print(square)

#Even numbers from list
even_nums = [x for x in range(1,11) if x%2==0]
print(even_nums)

#clean list of Strings
raw_names = [" Ankit","MeerA ", " RaJEsh"]
clean = [n.strip().title() for n in raw_names]
print(clean)

#Nested Lists + Flattening
nested = [[1, 2], [3, 4, 5], [6]]
flat = [n for sublist in nested for n in sublist]
print(flat)