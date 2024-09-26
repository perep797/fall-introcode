
# Print a blank line
print("\n")

# Ask the user for a filename
filename = input("Please enter the name of a file in this directory: ")

# Open that file
file = open(filename)

print("Name is: " + file.readline())
print("Title is: " + file.readline())
print("Phone number is: " + file.readline())
print("Address is: " + file.readline())

#I typed c:/Users/pauli/fall-24-introcode/unit-1/lesson-1/business_card_read.py when prompted by the program, and there was nothing in the title/phone number fields. I'm not sure what 'other name' I'm supposed to input, so I tried other files in the folder, but no new .txt files were created.