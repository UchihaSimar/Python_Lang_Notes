nums = [1,2,3,4,5,6,7,8,9,10]

# def gen_func(nums):
#     for num in nums:
#         yield num *num

# my_gen = gen_func(nums)

my_gen = (n*n for n in nums)


for generated_num in my_gen:
    print(generated_num)