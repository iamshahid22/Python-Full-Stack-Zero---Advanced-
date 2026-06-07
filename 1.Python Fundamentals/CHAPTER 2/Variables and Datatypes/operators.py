#Arithmetic Operators
a = 10
b = 3

print(a + b)    # Addition → 13
print(a - b)    # Subtraction → 7
print(a * b)    # Multiplication → 30
print(a / b)    # Division → 3.3333... (always float!)
print(a // b)   # Floor Division → 3 (removes decimal)
print(a % b)    # Modulus (remainder) → 1 (10÷3 remainder is 1)
print(a ** b)   # Power → 1000 (10³ = 10×10×10)


#Shortcut Assignment Operators
score = 100

score += 10    # score = score + 10 → 110
score -= 5     # score = score - 5  → 105
score *= 2     # score = score * 2  → 210
score /= 3     # score = score / 3  → 70.0
score //= 2    # score = score // 2 → 35.0
score %= 6     # score = score % 6  → 5.0

print(score)   # 5.0