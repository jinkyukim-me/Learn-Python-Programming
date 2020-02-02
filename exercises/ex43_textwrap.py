import textwrap

text = "The textwrap module provides some convenience functions, as well as TextWrapper, the class that does all the work. If you're just wrapping or fillinf one or two next strings, the convenience functions should be good enough; otherwise, you should use an instance of TextWrapper for efficiency."

print(text, end='\n')

print("-" * 50)

print("textwrap.wrap(text, width=70, **kwargs)\n")
print("textwrap.wrap(text, width=14)\n", textwrap.wrap(text, width=14))
print("textwrap.wrap(text, width=15)\n", textwrap.wrap(text, width=15))

print("textwrap.fill(text, width=70, **kwargs)\n")
print("textwrap.fill(text, width=15)\n", textwrap.fill(text, width=15))

print("textwrap.shorten(text, width, **kwargs)\n")
print("textwrap.shorten(text, width=20)\n", textwrap.shorten(text, width=20))

print("textwrap.shorten(text, width=20, placeholder='...')\n", textwrap.shorten(text, width=20, placeholder="..."))
print("textwrap.shorten(text, width=30, placeholder='~~~')\n", textwrap.shorten(text, width=30, placeholder="~~~"))

s = '''\
hello
  world
    hi
        hi
            hi
'''
print(s)
print(repr(s))
print("textwrap.dedent(s)\n", textwrap.dedent(s))
print(repr(textwrap.dedent(s)))
print(textwrap.dedent(text))

print("textwrap.indent(text, prefix, predicate=None)")
t = "hello\n\n \nworld"
print(t)
print(textwrap.indent(t, '$$$'))
print()
print(textwrap.indent(t, '$$$', lambda line:True))
print()
print(textwrap.indent(s, '***'))



