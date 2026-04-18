message = "Hello World"

print(message)

# to lower case
print(message.lower())

# to upper case
print(message.upper())

# count
print(message.count('l'))

# find index
print(message.find('llo'))
print(message.find('u'))

# replace
new_message = message.replace('World', "Universe")
print(new_message)

# concatenation
greeting = "Hello"
name = "Simar"
print('Hello' ' ' 'World')
print(greeting + ' ' + name)

# Concatenation format
greeting = "Hello"
name = "Simar"
print(f"{greeting} {name}", end='!')

# dir
print(dir(message))
print(help(str.lower))
