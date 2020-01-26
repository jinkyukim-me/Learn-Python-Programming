# Exercise 6. Strings and Text

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
joke_evaluation1 = "Isn't that {} so {}?! {}"

# a variety of expressions 
print(joke_evaluation.format(hilarious))
print("Isn't that joke so funny?! {}".format(hilarious))
print("Isn't that joke so funny?! {}".format("False"))
print("Isn't that {} so {}?! {}".format('joke', 'funny', 'False'))
print("Isn't that {2} so {0}?! {1}".format('funny', 'False', 'joke'))


i = 'joke'
j = 'funny'
z = 'True'
print(joke_evaluation1.format(i, j, z))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

