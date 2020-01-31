# Excercise 36. Designing and Debugging

print("""
        Rules for if-statements

        1. Every `if-statement` must have an `else`.
        
        2. If this `else` should never run because it doesn't make sense, 
        then you must use a `die` function in the `else` that prints out an error message 
        and dies, just like we did in the last exercise. This will find many errors.
        
        3. Never nest `if-statements` more than two deep and always try to do them on deep.
        
        4. Treat `if-statements` like paragraphs, where each `if-elif-else` grouping is like 
        a et of sentences. Put blank lines before and after.
        
        5. Your Boolean tests should be simple. If they are complex, move their calculations 
        to variables earlier in your function and use a good name for variable.
        """)
print("""
        Rules for Loops
        
        1. Use a `while-loop` only to loop forever, and that means probably never.
        This only applies to Python; other languages are differnet.
        
        2. Use a `for-loop` for all other kinds of looping, especially if there is fixed
        or limited number of things to loop over.
        """)
print("""
        Tips for Debugging
        
        1. Do not use a "debugger." 
        A debugger is like doing a full-body scan on a sick person. 
        You do not get any specific useful information, 
        and you find a whole lot of information that doesn't help and is just confusing.
        
        2. The best way to debug a program is to use `print` to print out values of variables
        at points in the program to see where they fo wrong.

        3. Make sure parts of your programs work as you work on them. Do not write massive
        files of code before you try to run them. Code a little, run a little, fix a little.
        """)

