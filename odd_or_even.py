''' Instruction: Welcome a user and ask them for a number between 1 and 1000.
Check if the number is odd or even and print a message letting them know. '''

try:
    user_num_input = int(input('Welcome, What number are you thinking of?'))

    if user_num_input < 1 or user_num_input > 1000:
        print("Invalid number range. Please try again")

    else:
        if user_num_input %2 == 0:
            print("That's an even number!")
        else:
            print("That's an odd number!")
            
except ValueError:
    print("Please input a number not a string")