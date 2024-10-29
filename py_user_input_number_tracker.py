#Create a program that ask user to input a number ranging from 1 to 50. 
#Ask the user to input again until the user input is invalid. 
#When the user input is invalid, display how many inputted numbers are in the following range:
#1 - 10 = ?
#11- 20 = ?
#21- 30 = ?
#31- 40 = ?
#41- 50 = ?

#to get user input
def get_user_input():

    print("Welcome to User Input Number Tracker!")

    while True:
        user_name = input("Kindly enter your name to start: ")

        print("Thank you for inputting you name.\nTracker starting!")

        user_number = int(input("Kindly enter a number ranging from 1 to 50 only: "))

#contiunuing the user input
def continue_user_input():
    filler1 = print("filler1")

#displaying all of the inputted number within their ranges
def display_user_input():
    filler2 = print("filler2")

get_user_input()