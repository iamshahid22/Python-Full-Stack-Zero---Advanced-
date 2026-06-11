# *args = Accept ANY NUMBER of arguments as a TUPLE
def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(add_all(1,2,3,4))

# Example for *args
def pack_luggage(*items):
    print("Packing the following:")
    for item in items:
        print(f"- {item}")
        
pack_luggage("shirt","shoes","tshirts")

# example for *args
def calculate_sum(*args):
    total = 0
    for num in args:
        total+=num
    return total

print(calculate_sum(10,18,16))


# **kwargs = Accept ANY NUMBER of keyword arguments as DICT
def show_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
show_user_info(name="Shahid", age= 20, City="Kurnool")