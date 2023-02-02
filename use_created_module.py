# EXERCISE-2
#Create a Module in VS Code and Import It into jupyter notebook
# Module should have the following capabilities:

# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area

# 2) Has a function to calculate the circumference of a circle

from module import area_house , circle
# calculate the circumference of a circle
#Formated it to show the result upto 3 decimal places
ques= input('What do you want to calculate-Circumference or Area? Enter(c/a): ')
if ques == 'c' :
    radius = float(input ('Enter circle radius: '))
    print(f'Circumference of the circle is: {circle(radius):.3f}')
elif ques == 'a' :
    # calculate the square footage of a house
    #Formated it to show the result upto 3 decimal places
    length = float(input('Enter length of your house: '))
    width = float(input('Enter width of your house: '))
    print(f'Area of your house is: {area_house(length,width):.3f}')

    