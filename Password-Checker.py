import re

def assess_password_strength(password):
    # Checking criteria
    has_numbers = any(char.isdigit() for char in password)
    has_upper_case = any(char.isupper() for char in password)
    has_lower_case = any(char.islower() for char in password)
    meets_length_requirement = len(password) >= 8
    has_special_characters = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Count the number of criteria met
    criteria_met = sum([has_numbers, has_upper_case, has_lower_case, meets_length_requirement, has_special_characters])

    # Determine password strength based on criteria met
    if criteria_met == 5:
        return "Password Strength Level: Very Strong (All criteria are met)."
    elif criteria_met == 4:
        return "Password Strength Level: Strong (4 out of 5 criteria are met)."
    elif criteria_met == 3:
        return "Password Strength Level: Moderate (3 out of 5 criteria are met)."
    else:
        return "Password Strength Level: Weak (Less than 3 criteria are met)."

def main():
    print("---------------- Password Complexity Checking Tool -----------------")
    

    # Get user input for the password (visible to the user)
    password_input = input("\nEnter your password: ")

    # Masked password for display
    if len(password_input) > 2:
        masked_password = password_input[0] + '#' * (len(password_input) - 2) + password_input[-1]
    else:
        masked_password = password_input

    # Assess the password strength
    result = assess_password_strength(password_input)

    # Display the masked password and strength result
    print("\nEntered Password: {}".format(masked_password))
    print("")
    print(result)

if __name__ == "__main__":
    main()
