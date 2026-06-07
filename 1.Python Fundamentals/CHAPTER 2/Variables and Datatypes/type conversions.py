#Sometimes you need to change one type to another
#string to integer
age_text = "20"
age_num = int(age_text)
print(age_num + 5)

#integer to string
age=20
age_text=str(age)
print("I am " + age_text + " years old")

#int to float
num=1309
decimal=float(num)
print(decimal)

#float to int
height = 172.3
whole = int(height)
print(whole)

#str to float
price_text = "99.9"
price = float(price_text)
print(price + 1)

#Real Example
user_age = input("Enter ur age:")
print(type(user_age))

user_age = int(input("Enter your age:"))
print(type(user_age))