courses = ['History','Math','Physics','CompSci']

# view
print(courses)

# length
print(len(courses))

# accesses / slicing
print(courses[0])
print(courses[0:])
print(courses[-1])
print(courses[-4:])
print(courses[-1:0])

# append
courses.append('Art') 
print(courses)

# insert
courses.insert(0, 'Early Maths')
print(courses)

# extend -> Append for multiple values ( If, you try thus using insert or append, it will create arrays inside arrays)
courses.extend(['Maths 2', 'History 2'])
print(courses)

# remove
courses.remove('Math')
removed_course = courses.pop() # -> Removes last value, useful in stack or queue
print(courses)
print(removed_course)

# reverse
courses.reverse()
print(courses)

# sort
nums = [1.5,2,4,3]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# sorting ( returns a copy without touching )
nums = [1.5,2,4,3]
sorted_nums = sorted(nums)
print(nums)
print(sorted_nums)
print(min(nums))
print(max(nums))
print(sum(nums))

# finding
courses = ['History','Math','Physics','CompSci']
print(courses.index('History'))
print('Art' in courses) # -> useful to check without throwing errors

# Looping
courses = ['History','Math','Physics','CompSci']
for course in courses:
    print(course)

for index, course in enumerate(courses, start=1):
    print(f"{index}. {course}")

# Join
courses = ['History','Math','Physics','CompSci']
print(courses)
courses_str = ','.join(courses)
print(courses_str)
courses_split = courses_str.split(',')
print(courses_split)

# Copy

list_1 = ['Histoy','Math','Physics','CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

# Copy - Shallow
list_1 = ['Histoy','Math','Physics','CompSci']
list_2 = list_1[:]

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)