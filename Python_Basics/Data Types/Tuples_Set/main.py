# Tuple
tuple_1 = ('Histoy','Math','Physics','CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

# Some methods
tuple_1 = ('Histoy','Math','Physics','CompSci')
tuple_1.index('Art')

# Set
courses = {'Histoy','Math','Physics','CompSci'}
courses.add('Math')
print(courses)
print('Math' in courses) # -> Most optimised membership test