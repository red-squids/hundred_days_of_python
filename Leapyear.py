# On Every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

print('Lets check if a year is a leap year.')
year = int(input('Enter a year: '))

if year % 4 != 0: # if year isn't divisible by 4, its not a leap year
    print(f'{year} is not a leap year.') 

elif year % 100 == 0: 
    if year % 400 == 0: # If it is evenly divisible by 100, is it also divisible by 400?
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')
else:
    print(f'{year} is a leap year.') # If its not divisible by 100 its a leap year.




