while True:
    weight = input("What is your weight in kg? ")
    if not weight.isnumeric():
        print("That's not a whole number.")
    else:
        break

while True:
    height = input("What is your height in cm? ")
    if not height.isnumeric():
        print("That's not a whole number.")
    else:
        break
BMI = round(int(weight) / (int(height) / 100) ** 2, 1)
print("Your Body Mass Index is " + str(BMI))
print("BMI under 18.5 is underweight, BMI between 18.5 and 24.9 is healthy, BMI between 25.0 and 29.9 is overweight,"
      " BMI over 30.0 is obese.")
if BMI < 18.5:
    print("You're underweight!")
elif 18.5 <= BMI <= 24.9:
    print("You're healthy.")
elif 25.0 <= BMI <= 29.9:
    print("You're overweight!")
elif BMI >= 30.0:
    print("You're obese!")
