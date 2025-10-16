# Writ a function which generates a six digit/character random_user_id
import random
import string
def random_user_id():
    characters = string.ascii_letters + string.digits  # gồm a-z, A-Z, 0-9
    user_id = ''.join(random.choices(characters, k=6))  # chọn ngẫu nhiên 6 ký tự
    return user_id
print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num_chars = int(input("Enter number of characters per ID: "))
    num_ids = int(input("Enter number of IDs to generate: "))

    characters = string.ascii_letters + string.digits
    ids = []

    for _ in range(num_ids):
        user_id = ''.join(random.choices(characters, k=num_chars))
        ids.append(user_id)

    for user_id in ids:
        print(user_id)

user_id_gen_by_user()

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"

print(rgb_color_gen())

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(num_colors):
    hex_chars = '0123456789abcdef'
    colors = []

    for _ in range(num_colors):
        color = '#' + ''.join(random.choices(hex_chars, k=6))
        colors.append(color)

    return colors

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f"rgb({r}, {g}, {b})")
    return colors

# Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors (type_color, num_colors):
    if type_color == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif type_color == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        return "Error"

print(generate_colors('hexa', 5))
print(generate_colors('rgb', 3))

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    shuffled = lst.copy()
    random.shuffle(shuffled)
    return shuffled

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def seven_unique_random_numbers():
    return random.sample(range(0, 10), 7)

print(seven_unique_random_numbers())