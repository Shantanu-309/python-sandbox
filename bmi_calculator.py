#BMI
print("# BMI CALCULATOR #")

sys = input("do u use the metric system or the imperial system??").lower()

if sys == "metric":

 heightm = float(input("height in meters "))
 weightm =  int(input("weight in kilograms"))
 heightm = heightm*heightm
 bmim = weightm/heightm
 print(f"your bmi is {bmim}")

elif sys == "imperial":
 heighti = int(input("height in inches "))
 weighti =  int(input("weight in pounds "))
 heighti = heighti*heighti
 weighti =  weighti*703
 bmii = weighti/heighti
 print(f"your bmi is {bmii}")

else :
 while sys not in ["metric", "imperial"]:
  print("what do u mean?? try again ")
  sys = input("do u use the metric system or the imperial system??").lower()

