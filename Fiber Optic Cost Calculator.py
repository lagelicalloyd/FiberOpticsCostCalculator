''' 
Lagelica Lloyd 
March 20223
Module 3 Assignment
'''

# write a program that will calculate the cost of installing fiber optic cable at a cost of .87 per ft for a company. 
# Your program should display the company name and the total cost.

Welcome_Message = "Welcome to the Fiber Optic Cost Calculator!" # Assigning a Variable for the Welcome Message
print(Welcome_Message) # This code sends the welcome message as soon as the program is ran

Company_Name = input("Enter Company Name:") # This code prompts the user to enter the company name

Feet = input("Enter the number of feet of fiber optic to be installed:") # This code prompts the user to enter the number of feet

Calculation = .87 * int(Feet) # This code assigns a variable name for the fiber optic cost calculation

# The below code is the main deliverable for the program. It states the company and the total cost.
print("The total cost of fiber optic installation for",Company_Name,"is $",Calculation)

# This code is just to keep the program from immediately closing so the user can see the calculation.
input("Press enter to exit program:")
