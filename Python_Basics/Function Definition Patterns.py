"""
    progression from the "Wild West" to the "Master Template."

    "Data flows positionally; Settings flow by keyword."
"""

print("----------------------- The Standard Pattern (The 'Wild West') -----------------------")
def add(a,b):
    """
        How this works: Users can bind to your internal names (a, b). 
        Problem : If you rename them later, their code breaks.
    """
    return a+b
print(add(1,2))

print("----------------------- The Positional-Only Gate (/) -----------------------")
def pos_only_func(data, factor, /):
    return [i * factor for i in data]

#Valid
print(pos_only_func([1, 2, 3], 10))

#Invalid, cause data and factor are position only arguments. can't be passed using keywords. (Uncomment, the below code to see how it breaks)
# pos_only_func(data=[1, 2], factor=10)

print("----------------------- The Keyword-Only Gate (*) -----------------------")
def keyword_only_func(data=1,*,mode="fast"):
    print(data,mode)

#valid
keyword_only_func(1,mode=2)
keyword_only_func([1,2],mode="slow")
keyword_only_func([1,2])
keyword_only_func(mode="slow")
keyword_only_func(data = [1, 2], mode = "slow") 

#invalid
# keyword_only_func([1, 2], "slow") # keyword_only_func() takes from 0 to 1 positional arguments but 2 were given

print("----------------------- The Master Template (The 'API Architect') -----------------------")
def master_template(pos_only, /, standard, *args, kw_only, **kwargs):
    """
    Zone 1: pos_only  | Must be positional.
    Zone 2: standard  | Flexible (either).
    Zone 3: *args     | Collects extra unlabeled data (Tuple).
    Zone 4: kw_only   | Must be labeled.
    Zone 5: **kwargs  | Collects extra labeled data (Dict).
    """
    print(f"Pos-Only: {pos_only}")
    print(f"Standard: {standard}")
    print(f"Args: {args}")
    print(f"KW-Only: {kw_only}")
    print(f"KW-Args: {kwargs}")
# Example Call:
master_template(
    1,                  # pos_only
    2,                  # standard
    3, 4, 5,            # *args (The "Overflow")
    kw_only="Safety",   # kw_only
    extra_flag=True     # **kwargs
)
