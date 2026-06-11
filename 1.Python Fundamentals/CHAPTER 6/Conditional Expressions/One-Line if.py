# Long way
age =20
if age>=18:
    status = "major"
else:
    status = "minor"
    
#short way - ternary operator
status = "major" if age>=18 else "minor"
print(status)
