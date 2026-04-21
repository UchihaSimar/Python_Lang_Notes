"""
    Lambda Functions
"""

result = (lambda x: x * 2)(4)
print(result)

data = [1,2,3,4]
data_result =list(map(lambda x: x*2, data))
print(data_result)