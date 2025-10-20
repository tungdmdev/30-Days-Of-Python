# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_and_zero = [n for n in numbers if n <= 0]
print(negatives_and_zero)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [num for sublist in list_of_lists for inner in sublist for num in inner]
print(flattened)
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using list comprehension create the following list of tuples:
result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)

# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_list = [[country.upper(), country[:3].upper(), capital.upper()] for [(country, capital)] in countries]

# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = [{'country': country.upper(), 'city': capital.upper()} for [(country, capital)] in countries]
print(result)

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
result = [f"{first} {last}" for [(first, last)] in names]
print(result)

# Write a lambda function which can solve a slope or y-intercept of linear functions.
points = [((2, 3), (5, 11)), ((1, 2), (3, 6)), ((0, 1), (4, 9))]
results = [
    (
        (y2 - y1) / (x2 - x1),              # slope m
        y1 - ((y2 - y1) / (x2 - x1)) * x1   # intercept b
    )
    for ((x1, y1), (x2, y2)) in points
]

print(results)