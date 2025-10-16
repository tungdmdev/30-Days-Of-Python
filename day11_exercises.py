# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
import math
def circle_area ():
    r = 5
    area = math.pi * r * r
    print(area)
circle_area ()   

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. 
# If not do give a reasonable feedback.
def add_all_nums (*args):
    total = 0
    for i in args:
        if isinstance(i, (int,float)):
            total += i
    return total    
    
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit (celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit(26))

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season (month):
    if not 1 <= month <= 12:
        return "Invalid month"
    
    match month:
        case 1 | 2 | 3:
            return "Spring"
        case 4 | 5 | 6:
            return "Summer"
        case 7 | 8 | 9:
            return "Autumn"
        case 10 | 11 | 12:
            return "Winter"
print (check_season(2))   

# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope (a,b,c,d):
    if c == d:
        return "Error"
    slope = (a - b) / (c - d)
    return slope
print(calculate_slope(4,52,32,7))

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn (a, b, c):
    if a == 0:
        return "Error"
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Error"
    elif delta == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return (x1, x2)
print(solve_quadratic_eqn(1, 2, 1))   

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list (lst):
    for item in lst:
        print(item)
fruits = ["apple", "banana", "mango", "orange"]
print_list(fruits)

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list (lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items (lst):
    for i in range(len(lst)):
        lst[i] = lst[i].capitalize()
    return lst
print(capitalize_list_items(['aaa','bbb','ccc']))

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, item):
    lst.append(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      #[2, 3, 7, 9, 5]

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item (lst, item):
    lst.remove(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    total = 0
    for i in range(1, num + 1):
        if i % 2 != 0:
            total += i
    return total  
print(sum_of_odds(10))      

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num):
    total = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            total += i
    return total  
print(sum_of_even(10))

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num):
    even_count = 0
    odd_count = 0
    for i in range(0, num + 1):
        if i % 2 ==0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
print(evens_and_odds(100))

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        res = 1
        for i in range(2, num + 1):
            res *= i
        return res
number = 5
result = factorial(number)

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(data):
    if not data:
        return True
    else:
        return False
    
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(nums):
    total = 0
    for n in nums:
        total += n
        mean = total / len(nums)
    return mean

def calculate_median(nums):
    nums.sort()
    n = len(numbers)
    middle = n // 2

    if n % 2 == 0:  # nếu có số phần tử chẵn
        median = (numbers[middle - 1] + numbers[middle]) / 2
    else:  # nếu có số phần tử lẻ
        median = numbers[middle]

    return median

def calculate_mode(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_count = max(frequency.values())
    mode = [key for key, value in frequency.items() if value == max_count]
    
    return mode[0] if len(mode) == 1 else mode

def calculate_range(lst):
    value_range = max(lst) - min(lst)
    return value_range

def calculate_variance(lst):
    mean = sum(lst) / len(lst)
    total = 0
    for x in lst:
        total += (x - mean) ** 2
    variance = total / len(lst)
    return variance


def calculate_std(lst):
    variance = calculate_variance(lst)
    return math.sqrt(variance)

# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Write a functions which checks if all items are unique in the list.
def is_unique(lst):
    return len(lst) == len(set(lst))

# Write a function which checks if all the items of the list are of the same data type.
def same_data_type(lst):
    if not lst:
        return True  # danh sách trống thì xem như cùng kiểu
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return False
    return True
# Write a function which check if provided variable is a valid python variable
import keyword

def is_valid_variable(var):
    return var.isidentifier() and not keyword.iskeyword(var)

# Go to the data folder and access the countries-data.py file.
from data.countries_data import countries_data
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages(lang_count):
    language_count = {}
    for country in countries_data:
        for lang in country["languages"]:
            language_count[lang] = language_count.get(lang, 0) + 1
    most_spoken = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return most_spoken[:lang_count]
print(most_spoken_languages(10))
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(n):
    sorted_countries = sorted(countries_data, key=lambda x: x["population"], reverse=True)

    top_countries = sorted_countries[:n]

    return [(country["name"], country["population"]) for country in top_countries]
