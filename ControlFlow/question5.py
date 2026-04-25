earth_weight = float(input("Enter your Earth weight : "))
planet_num = int(input("Enter a planet number : "))
dest_weight = 0

if planet_num == 1:
  dest_weight = earth_weight * 0.38
elif planet_num == 2:
  dest_weight = earth_weight * 0.91
elif planet_num == 3:
  dest_weight = earth_weight * 0.38
elif planet_num == 4:
  dest_weight = earth_weight * 2.53
elif planet_num == 5:
  dest_weight = earth_weight * 1.07
elif planet_num == 6:
  dest_weight = earth_weight * 0.89
elif planet_num == 7:
  dest_weight = earth_weight * 1.14
else:
  print("Invalid number")

print(dest_weight)