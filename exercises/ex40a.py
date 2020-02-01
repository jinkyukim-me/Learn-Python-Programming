# Exercise 40. Modules, Classes, and Objects

mystuff = {'OOP' : 'object-oriented-programming'}

# dict style
print(mystuff['OOP']) # get apple from dict

# put a variable in it named coffee
import mystuff
# module style
mystuff.coffee() # get coffee from the module
print(mystuff.tangerine) # same thing, it's just a variable

print("""
        This means we have a very common pattern in Python:
        1. Take a key=value style container.
        2. Get something out of it by the key's name.
""")

print("""
        Classes Are Like Modules
""")

# class style
thing = mystuff.MyStuff() # `instantiate` operation, and it's like calling a function
print(thing.tangerine)
thing.apple()
