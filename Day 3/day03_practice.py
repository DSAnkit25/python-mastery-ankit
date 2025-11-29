#Problem 1 — Student Marks Dictionary
#calulate total,average
from heapq import merge

student = {"math": 88, "physics": 92, "chemistry": 81}
a = student.values()
print("Total Marks:",sum(a))
print("Average Marks:",sum(a)/len(a))
print(sum(student.values())) #other ways
#Problem 2 — Remove Duplicates Using Set
# Convert to set (to remove duplicates)
# Convert back to sorted list
data = [12, 12, 33, 44, 55, 55, 55, 66]
con_data = sorted(set(data))
print(con_data)
lst=list(con_data)
lst.sort()
print(lst)
#Problem 3 — Character Frequency Counter
Word = "automation"
new={}
for char in Word:
    new[char]=new.get(char,0)+1 #Loop through characters & build a dictionary
print(new)
# Problem 4 — Merge Two Dictionaries
d1 = {"a": 10, "b": 20}
d2 = {"b": 30, "c": 40}
d = d1.update(d2)
D={**d1,**d2}
print(d)
print(D)
# Problem 5 — Unique Departments Using a Set
employees = [
    {"name": "Ankit", "dept": "Data"},
    {"name": "Mira", "dept": "Finance"},
    {"name": "Raj",  "dept": "Data"}
]
departments = {employee["dept"] for employee in employees}
print(departments)