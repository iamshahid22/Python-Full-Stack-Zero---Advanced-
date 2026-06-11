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


# **kwargs = 