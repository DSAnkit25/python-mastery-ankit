# A dictionary is a data structure that stores information in key–value pairs.
# JSON = dictionary in Python
# ✔ Used in:
# APIs
# AWS automation
# LLM output parsing
# CLI tools
# Data processing
# Config files

User = {
    "name": "Ankit",
    "age": 27,
    "city": "San Diego"
}
print(User)#entire dict
print(User["name"]) #look for key and print out the pair value
print(User["age"])
print(User.keys())
#new Key-value
User["email"] = "ankit@pythonmaster.com"
print(User)
#update age
User["age"] = 28
print(User)
#lets try to add another same key
User["city"] = "london"
print(User)

for key, value in User.items():
    print(key,":", value)

if "city" in User:
    print("city name is present")
    print(User["city"])

# Nested Dictionary
# Dictionaries within a dictionary

employees = {
    "emp1": {"name": "Ankit", "dept": "Data"},
    "emp2": {"name": "Mira", "dept": "HR"},
    "emp3": {"name": "Raj", "dept": "Finance"}
}

for employee in employees:
    print(employee) #this will just give keys
    print(employees[employee]) # geraters entire dictionary

for emp_id,details in employees.items():
    print(f"{emp_id}:{details['name']}-{details['dept']}")

if "age" in employees["emp1"]:
        print(employees["emp2"]["name"])
else:
        print(employees["emp3"]["name"])
# Sets Unique value & operators
nums = [10, 20,20, 30, 40,60, 50, 60]
uniq_nums = set(nums)
print(uniq_nums)

#set operations
a={1,2,3,4,5}
b={1,5,7,9}
print(a & b) #this will give common value between 2 sets #intersection
print(a | b) #all the unique values between the 2 sets #union
print(a ^ b) #this will give non common values
print(b.difference(a)) #give diffrence bwtn the 2