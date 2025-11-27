# Problem 1 — Reverse a String
# User enters name → print reversed.
A = "Ankit"
print(A[::-1])
#other way to do it
b=""
for i in A:
    b = i+b
print(b)

# Problem 2 — Check Palindrome
# Examples:
# malayalam → palindrome
# ankit → not palindrome

def palindrome(s):
          if s == s[::-1]:
              return print("Palindrome")
          else:
              return print("Not Palindrome")

palindrome("malayalam")

# Problem 3 — Separate Even & Odd Numbers
# Given a list: [12, 3, 55, 6, 77, 22, 90]

def even_odd(n):
    c=[]
    d=[]
    for i in lst:
        if i % 2 == 0:
            c.append(i)
        else:
            d.append(i)
    return print("Even:",c," \n","Odd:",d)
lst = [12, 3, 55, 6, 77, 22, 90]
even_odd(lst)

# Problem 4 — Filter Names Starting With Vowel
names = ["Ankit", "Usha", "Raj", "Om", "Meera", "Ishan"]
vowels ="aeiouAEIOU"
vowels_name=[i for i in names if i[0] in vowels]
print(vowels_name)

# Problem 5 — Flatten Nested List and Find Sum
data = [[10,20], [30,40,50], [5]]
data=[n for sublist in data for n in sublist]
print(data)


