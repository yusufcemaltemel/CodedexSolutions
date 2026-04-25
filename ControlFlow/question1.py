rating = float(input("Rate the restaurant (0-5) : "))

if rating > 4.5:
  print("Perfection")
elif rating > 4:
  print("Excellent")
elif rating > 3: 
  print("Good")
elif rating > 2: 
  print("Fair")
else:
  print("Poor")