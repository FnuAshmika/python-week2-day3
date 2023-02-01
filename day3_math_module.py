# EXERCISE-2
#Create a Module in VS Code and Import It into jupyter notebook
# Module should have the following capabilities:

# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area
def area_house(length,width):
    area=length * width 
    return(area)
# 2) Has a function to calculate the circumference of a circle
def circle(radius):
    pi = 3.14
    circumference = 2*pi*radius
    return (circumference)