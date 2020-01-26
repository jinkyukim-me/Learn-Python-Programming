#i Exercise 5. More Variables and Printing

my_name = 'Jinkyu Kim'
my_age = 40 # This is not a lie
my_height = 180 # centimeters
my_weight = 80 # kilograms
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} centimeters tall.")
print(f"He's {my_weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

