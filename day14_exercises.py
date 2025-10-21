countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use for loop to print each country in the countries list.
for country in countries:
    print(country)
# Use for to print each name in the names list.
for name in names:
    print(name)
# Use for to print each number in the numbers list.
for n in numbers:
    print(n)

# Use map to create a new list by changing each country to uppercase in the countries list
uppercase_countries = list(map(str.upper, countries))
print(uppercase_countries) 

# Use map to create a new list by changing each number to its square in the numbers list
def square(x):
    return x**2
square_number = list(map(square, numbers))

# Use map to change each name to uppercase in the names list
uppercase_names = list(map(str.upper, names))
print(uppercase_names)

# Use filter to filter out countries containing 'land'.
def does_not_contain_land(country):
    return 'land' not in country.lower()

filtered_countries = list(filter(does_not_contain_land, countries))
print(filtered_countries)

# Use filter to filter out countries having exactly six characters.
def exactly_six_char_country(country):
    return len(country) != 6
six_char_filtered = list(filter(exactly_six_char_country, countries))

# Use filter to filter out countries containing six letters and more in the country list.
def six_more_country(country):
    return len(country) < 6
six_more_filtered = list(filter(six_more_country, countries))

# Use filter to filter out countries starting with an 'E'
def does_not_start_with_e(country):
    return not country.startswith('E')
without_start_e = list(filter(does_not_start_with_e, countries))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]
result = reduce(
    lambda acc, x: acc + x,
    filter(
        lambda x: x % 2 == 0,
        map(lambda x: x ** 2, numbers)
    )
)
print(result)

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(items):
    return list(filter(lambda item: isinstance(item, str), items))

# Use reduce to sum all the numbers in the numbers list.
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers_str)
print(total)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def concatenate_countries(acc, country):
    # acc is the accumulated string, country is the current item
    return acc + ", " + country
all_but_last = countries[:-1]
last_country = countries[-1]
concatenated = reduce(concatenate_countries, all_but_last)
# Add the last country with ", and "
sentence = f"{concatenated}, and {last_country} are north European countries"
print(sentence)

# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(pattern):
    return [country for country in countries if pattern.lower() in country.lower()]

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def count_countries_by_starting_letter(countries):
    result = {}
    for country in countries:
        first_letter = country[0].upper()  # Normalize to uppercase
        result[first_letter] = result.get(first_letter, 0) + 1
    return result

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(file_path):
    return countries[:10]

file_path = 'data/countries.js'
first_ten = get_first_ten_countries(file_path)
print(first_ten)
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list. 
def get_last_ten_countries(countries):
    return countries[-10:]
last_ten = get_last_ten_countries(file_path)
print(last_ten)

# Sort countries by name, by capital, by population
# Sort by name (alphabetically)
sorted_by_name = sorted(countries, key=lambda c: c['name'])

# Sort by capital (alphabetically)
sorted_by_capital = sorted(countries, key=lambda c: c['capital'])

# Sort by population (descending)
sorted_by_population = sorted(countries, key=lambda c: c['population'], reverse=True)

# Sort out the ten most spoken languages by location.
from collections import Counter

def top_ten_languages(countries):
    all_languages = [lang for country in countries for lang in country['languages']]
    language_counts = Counter(all_languages)
    return language_counts.most_common(10)

# Get top ten languages
top_languages = top_ten_languages(countries)

# Sort out the ten most populated countries.
top_ten_populated_countries = sorted_by_population[:10]