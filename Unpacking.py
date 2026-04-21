"""
    Multiple ways to unpack data
"""

# Basic Unpacking
print("------------ Basic Unpacking -----------------")
a,b = (1,2)
c,d = [3,4]
c,h,a,r = "char"
print(f"a = {a}, b = {b}, c = {c}, d = {d}")
print(f"c = {c}, h = {h}, a = {a}, r = {r}")


# Extended Unpacking (The "Splat" *)
print("------------ Extended Unpacking (The 'Splat' *) -----------------")
a, *b, c = [1,2,3,4]
print(f"a = {a}, b = {b}, c = {c}")

d, *e, f = (1,2,3,4)
print(f"d = {d}, e = {e}, f = {f}")

# Dictionary Unpacking (The **)
print("------------ Dictionary Unpacking (The **) -----------------")
dic1 = {
  "a":"a",
  "b":"b",
  "c":"c"
}
dic2 = {
  "a":"a1",
  "b":"b1"
}
print({ **dic1, **dic2})

# Deep Unpacking (Nested Structures)
print("------------ Deep Unpacking (Nested Structures) -----------------")
data = ("Banglaore", [1,2], "Karnataka")
city, (num1, num2), state = data
print(f"city = {city}, num1 = {num1}, num2 = {num2}, state = {state}")
city, *nums, state = data
print(f"city = {city}, *nums = {nums}, state = {state}")

#Function Call Unpacking (The "Splat" at Call-time)
print("------------ Function Call Unpacking (The 'Splat' at Call-time) -----------------")

def splatFunction(x,y,z):
    return x+y+z

point = [10,20,30]
metadata = {"y":100}

print(splatFunction(*point))
print(splatFunction(x=1,z=3,**metadata)) # because the / and * are not used in function definition, every argument is standard.