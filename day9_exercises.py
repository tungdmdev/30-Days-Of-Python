# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    years_left = 18 - age
    print(f"You need to wait {years_left} more year(s) to drive.")
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.        
your_age = int(input("Enter your age: "))
my_age = 25
if my_age > your_age:
    diff = my_age - your_age
    if diff == 1:
        print(f"I am {diff} year older than you.")
    else:
        print(f"I am {diff} years older than you.")
if my_age < your_age:
    diff = my_age - your_age
    if diff == 1:
        print(f"I am {diff} year younger than you.")
    else:
        print(f"I am {diff} years younger than you.")
else:
    print("We are the same age!")

# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.            
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a is equal to b")

# Write a code which gives grade to students according to theirs scores
score = int(input("Enter your score: "))
if 80 <= score <= 100:
    grade = "A"
elif 70 <= score <= 79:
    grade = "B"
elif 60 <= score <= 69:
    grade = "C"
elif 50 <= score <= 59:
    grade = "D"
elif 0 <= score <= 49:
    grade = "F"
else:
    grade = "Invalid score"
print(f"Your grade is: {grade}")

# Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter the month: ")
if month in ["September", "October", "November"]:
    season = "Autumn"
elif month in ["December", "January", "February"]:
    season = "Winter"
elif month in ["March", "April", "May"]:
    season = "Spring"
elif month in ["June", "July", "August"]:
    season = "Summer"
else:
    season = "Invalid month"
print(f"The season is {season}.")

# The following list contains some fruits
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ")
if fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit)
    print("Modified list:", fruits)

# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'Python' in skills:
    print("Has Python skill:", True)
else:
    print("Has Python skill:", False)
# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if skills == ['JavaScript', 'React']:
    print("He is a front end developer")
elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
    print("He is a backend developer")
elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
    print("He is a fullstack developer")
else:
    print("Unknown title")
# If the person is married and if he lives in Finland, print the information in the following format:
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")