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
    #greeting user
    print("✨ Welcome to User Input Number Tracker!✨")

    #asking user name for formality
    user_name = input("Kindly enter your name to start: ")

    #start tracker
    print(f"Thank you for entering your name. Welcome, {user_name}! \n🟢 Tracker starting!🟢")

    #now making this from the previous demo
    #making this a list
    inputted_number = []

    while True:    
            try:
                user_number = int(input("Kindly enter a number ranging from 1 to 50 only: "))
                        
                if 0 < user_number <= 50:
                    inputted_number.append(user_number) #store in an array

                    #how the user will continue inputting numbers
                    continue_input = input("Your input has been recorded. 📝 \nWould you like to input a number again? (yes/no): ")
                    
                    if continue_input == "no":
                        print("Thank you for using User Input Number Tracker!🎉 \nHere are your inputted numbers: ")
                        #printing them one by one
                        print(f"1 - 10 = {sum(1 for x in inputted_number if 1 <= x <= 10)}")
                        print(f"11 - 20 = {sum(1 for x in inputted_number if 11 <= x <= 20)}")
                        print(f"21 - 30 = {sum(1 for x in inputted_number if 21 <= x <= 30)}")
                        print(f"31 - 40 = {sum(1 for x in inputted_number if 31 <= x <= 40)}")
                        print(f"41 - 50 = {sum(1 for x in inputted_number if 41 <= x <= 50)}")
                        break
                    elif continue_input != "yes":
                        print("Invalid answer. Enter either yes or no only.")
            except:
                print("Invalid input. Enter a number ranging from 1 to 50 only.")
                continue

#call funtion
get_user_input()