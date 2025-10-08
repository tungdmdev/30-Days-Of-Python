# Exercises: Level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# Find the length of the set it_companies
len(it_companies)
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['item5','item6','item7'])
# Remove one of the companies from the set it_companies
it_companies.remove('item5')

# Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# Join A and B
C = A.union(B)
# Find A intersection B
A.intersection(B)
# Is A subset of B
A.issubset(B)
# Are A and B disjoint sets
A.isdisjoint(B)
# Join A with B and B with A
C = A.union(B)
D = B.union(A)
# What is the symmetric difference between A and B
A.difference(B)
# Delete the sets completely'
del C, D
# Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = set(sentence.split(''))
print(words)
