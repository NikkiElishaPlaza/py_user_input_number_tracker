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

    user_name = input("Kindly enter your name to start: ")

    print("Thank you for inputting you name.\nTracker starting!")
    
    while True:    
        try:
            user_number = int(input("Kindly enter a number ranging from 1 to 50 only: "))
                    
            if 0 < user_number <= 50:
                continue_input = input("Your input has been recorded. Would you like to input a number again? (yes/no): ")
                
                if continue_input == "no":
                    print("Thank you for using User Input Number Tracker! Here are your inputted numbers: ")
                    break
                elif continue_input != "yes":
                    print("Invalid answer. Enter either yes or no only.")
        except:
            print("Thank you for using User Input Number Tracker! Here are your inputted numbers: ")

get_user_input()