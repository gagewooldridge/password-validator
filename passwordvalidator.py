# This program will 'shuffle' a deck of cards and return a
# random combination of five cards

# Written by Gage Wooldridge

# Prompt user for input and give password requirements
input('''Please enter a password:

        Password must have,
            1) 8 to 12 characters
            2) at least one numeric digit
            3) at least one letter
            4) must not have space or backslash (/)
            5) at least one Capital letter
            6) starting character must not be a number

            ''')

# Verify password is between 8 and 12 characters
def char_count_validate(input, char):
    i = 0
    for c in input:
        if char == c:
            i += 1
            if i <= 12 and i >= 8:
                return True
            else:
                return False

# Verify password has one numeric digit
def numeric_digit_validate(input):
    if any(char.isdigit() for char in input):
        return True
    else:
        return False

# Verify password has at least one letter
def letter_validate(input):
    if any(char.isAlpha() for char in input):
        return True
    else:
        return False

# Verify password does not have a space or backslash
def space_slash_validate(input):
    if any(char for char in input) == ' ' or any(char for char in input) == "\\":
        return True
    else:
        return False

# Verify Password has a capital letter
def capital_validate(input):
    if any(char.isUpper() for char in input):
        return True
    else:
        return False

# Verify the first character is not a number
def numeric_first_validate(input):
    if input[0].isNumeric():
        return True
    else:
        return False

# Main function
def main(input):
    correct_length = char_count_validate(input)
    has_number = numeric_digit_validate(input)
    has_letter = letter_validate(input)
    no_space_slash = space_slash_validate(input)
    has_capital = capital_validate(input)
    first_number = numeric_digit_validate(input)








