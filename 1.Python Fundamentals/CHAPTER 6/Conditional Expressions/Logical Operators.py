age = 21
has_license = True

# AND - both must be True
if age > 18 and has_license:
    print("You can drive !")
    
# OR - one condition needs to True
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("You can spend much time with family today !")
    
 # NOT - reverses True/False
is_sunny = True
if not is_sunny:
    print("Take umbrella")
else:
    print("No need umbrella ")
    
    