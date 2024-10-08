# Welcome ascii art and message
print("""
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || |      __      | || |  _______     | || |     ____     | || |  _________   | |
| | |  _   _  |  | || |     /  \     | || | |_   __ \    | || |   .'    `.   | || | |  _   _  |  | |
| | |_/ | | \_|  | || |    / /\ \    | || |   | |__) |   | || |  /  .--.  \  | || | |_/ | | \_|  | |
| |     | |      | || |   / ____ \   | || |   |  __ /    | || |  | |    | |  | || |     | |      | |
| |    _| |_     | || | _/ /    \ \_ | || |  _| |  \ \_  | || |  \  `--'  /  | || |    _| |_     | |
| |   |_____|    | || ||____|  |____|| || | |____| |___| | || |   `.____.'   | || |   |_____|    | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
""")

print("Welcome Friend.\n")
print("I can give you a Tarot reading based on your Past, Present and Future.\n")
# Ask users permission to give a reading
def give_reading():
    reading_prompt = input("Would you like a reading today? y/n  ")
    if reading_prompt == "y":
        print("Wonderful!  Let's see what the cards can tell you today")
        # Call past_reading function
    elif reading_prompt == "n":
        print("No problem.  Come back anytime to get your reading.") 
    else:
        print("Please type either 'y' or 'n'.")
        return give_reading()

print(give_reading())   

# Create dictionary of tarot cards

# Make past_reading function

# Make present_reading function

# Make future_reading function

# Give farewell message
