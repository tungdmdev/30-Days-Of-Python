# Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)
i = 0
while i <= 10:
    print(i)
    i += 1
# Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i)
i = 10
while i >= 0:
    print(i)
    i -= 1
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(1, 8):
    print('#' * i)
# Use nested loops to create the following:
for i in range(8):
    print('#' * 8)
i = 0
while i < 8:
    print('# ' * 8)
    i += 1
# Print the following pattern:      
for i in range(1 , 10):
    sqrt = i * i
    print(f"{i} x {i} = {sqrt}")
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lists = ['Python', 'Numpy','Pandas','Django', 'Flask']
for list in lists:
    print(list)
# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(i)
# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 != 0:
        print(i)
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for i in range(101):
    sum += i 
print(sum)
# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
e_sum = 0
o_sum = 0
for i in range(101):
    if i % 2 == 0:
        e_sum += i
    else:
        o_sum += i
print(f"the sum of all evens is {e_sum} and the sum of all odds is {o_sum}")
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from data.countries import countries
for country in countries:
    if 'land' in country:
        print(country)
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_lists = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(fruit_lists) - 1, -1, -1):
    print(fruit_lists[i])
# Go to the data folder and use the countries_data.py file.
from data.countries_data import countries_data
# What are the total number of languages in the data
languages = set()
for country in countries_data:
    for lang in country["languages"]:
        languages.add(lang)
print("Total number of languages:", len(languages))
# Find the ten most spoken languages from the data
language_count = {}

for country in countries_data:
    for lang in country["languages"]:
        language_count[lang] = language_count.get(lang, 0) + 1

most_spoken = sorted(language_count.items(), key=lambda x: x[1], reverse=True)

print("10 most spoken languages:")
for lang, count in most_spoken[:10]:
    print(f"{lang}: {count} countries")
# Find the 10 most populated countries in the world
most_populated = sorted(countries_data, key=lambda x: x["population"], reverse=True)

print("10 most populated countries:")
for country in most_populated[:10]:
    print(f"{country['name']}: {country['population']}")