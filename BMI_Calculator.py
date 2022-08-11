# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese

def bmi_calc(weight, height):
    '''
    Calculates the BMI
    bmi = weight / height^2
    '''
    bmi = weight / pow(height, 2)
    print(f'Your BMI is {bmi:.2f}')
    if bmi < 18.5:
        print('You are considered Underweight.')
    elif bmi > 18.5 and bmi < 25:
        print('Your weight is normal.')
    elif bmi > 25 and bmi < 30:
        print("You are slightly overweight.")
    elif bmi > 30 and bmi < 35:
        print("You are obese.")
    elif bmi > 35:
        print("You are clinically obese.")

def lbs_to_kg(lbs):
    '''
    Converts lbs to kgs
    '''
    kgs = lbs * 0.45359237
    return kgs


def inch_to_meters(inch):
    '''
    Converts inches to meters
    '''
    meters = inch * 0.0254
    return meters


#----------------------------------------------------------------------------#
# Added conversion functions because i dont typically work with metric sadly #
#----------------------------------------------------------------------------#
lbs = float(input("Enter your weight in lbs: "))
weight = lbs_to_kg(lbs)

inch = float(input("Enter your height in inches: "))
height = inch_to_meters(inch)

results = bmi_calc(weight, height)




