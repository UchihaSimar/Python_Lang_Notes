# =========================== List Comprehentions========================
nums = [1,2,3,4,5,6,7,8,9,10]

# my_list = []
# for num in nums:
#   my_list.append(num)
# print(my_list)

my_list = [num for num in nums]
print(my_list)

# my_square_list = []
# for num in nums:
#   my_square_list.append(num*num)
# print(my_square_list)

my_square_list = [num*num for num in nums]
print(my_square_list)

my_square_list = map(lambda num: num*num, nums)
print(list(my_square_list))


# my_even_list = []
# for num in nums:
#   if num%2 == 0:
#     my_even_list.append(num)
# print(my_even_list)

my_even_list = [num for num in nums if num%2 == 0]
print(my_even_list)

my_even_list = filter(lambda num: num%2==0, nums)
print(list(my_even_list))


# my_data_list= []
# for letter in 'abcd':
#   for num in range(4):
#     my_data_list.append((letter,num))
# print(my_data_list)
my_data_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_data_list)


# =========================== Dictionary Comprehentions========================
names = ['Bruce','Clark','Peter','Logan','Wade']
heros = ['Batman','Superman','Spiderman','Wolverine','Deadpool']

# my_dict = {}
# for name, hero in zip(names,heros):
#   my_dict[name] = hero
# print(my_dict)

my_dict = {name:hero for name,hero in zip(names,heros)}
print(my_dict)

my_dict = {name:hero for name,hero in zip(names,heros) if name != 'Peter'}
print(my_dict)

# =========================== Set Comprehentions========================
nums = [1,1,2,2,3,3,4,5,5,6,7,7,8,9,9,10]

# my_set = set()
# for n in nums:
#   my_set.add(n)
# print(my_set)


my_set = { num for num in nums }
print(my_set)