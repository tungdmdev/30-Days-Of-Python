sis = ('a','c','e')
bro = ('b','d','f')
sib = sis + bro

new = ('g','h')
fam_mem = new + sib

# ----------------------------------------------------
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animals = ('cat', 'dog', 'bird')

food_stuff_tp = fruits + vegetables + animals

food_stuff_lt = list(food_stuff_tp)

mid_index = len(food_stuff_tp) // 2
middle_item = food_stuff_tp[mid_index]

first_three = food_stuff_lt[:3]
first_three = food_stuff_lt[-3:]

del food_stuff_tp

ordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in ordic_countries)
print('Iceland' in ordic_countries)