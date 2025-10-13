# Create an empty dictionary called dog
dog = {'name':'value1', 'color':'value2', 'breed':'value3', 'legs':'value4', 'age':'value5'}
# Add name, color, breed, legs, age to the dog dictionary
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
stu_dic = {
    'first_name':'',
    'last_name':'',
    'gender':'',
    'age':'',
    'marital status':'',
    'skills':[''],
    'country':'',
    'city':'',
    'address':''
}
# Get the length of the student dictionary
print(len(stu_dic))
# Get the value of skills and check the data type, it should be a list
print(stu_dic.get('skills'))
# Modify the skills values by adding one or two skills
stu_dic['skills'].append('HTML')
# Get the dictionary keys as a list
keys = stu_dic.keys()
# Get the dictionary values as a list
values = stu_dic.values()
# Change the dictionary to a list of tuples using items() method
tuple_list = list(stu_dic.items())
# Delete one of the items in the dictionary
del stu_dic['name']
# Delete one of the dictionaries
del stu_dic