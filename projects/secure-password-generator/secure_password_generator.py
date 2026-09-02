import random


def generate_password(length, include_numbers, include_special, include_uppercase):
    # Build the available character pool
    characters = "abcdefghijklmnopqrstuvwxyz"

    if include_numbers:
        characters += "0123456789"

    if include_special:
        characters += "!@#$%^&*"

    if include_uppercase:
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Generate the password
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def check_password_strength(password, include_numbers, include_special, include_uppercase):
    # Calculate the simple project strength score
    score = len(password)

    if include_numbers:
        score += 2

    if include_special:
        score += 3

    if include_uppercase:
        score += 2

    if score < 10:
        return "Weak"
    elif score < 16:
        return "Medium"
    else:
        return "Strong"


def test_generate_password():
    # Run the mini length test
    test_password = generate_password(12, True, True, True)

    if len(test_password) == 12:
        print("Test passed: generated password has the correct length.")
    else:
        print("Test failed: generated password has the wrong length.")


def main():
    # Collect and validate user input
    while True:
        try:
            length_input = input("Enter password length (minimum 8): ")
            length = int(length_input)

            if length < 8:
                print("The password must be at least 8 characters long.")
                continue

            include_numbers_input = input("Include numbers? (yes/no): ").lower()
            include_numbers = include_numbers_input == "yes"

            include_special_input = input(
                "Include special characters? (yes/no): "
            ).lower()
            include_special = include_special_input == "yes"

            include_uppercase_input = input(
                "Include uppercase letters? (yes/no): "
            ).lower()
            include_uppercase = include_uppercase_input == "yes"

            # Generate and display the final result
            new_password = generate_password(
                length,
                include_numbers,
                include_special,
                include_uppercase,
            )
            strength = check_password_strength(
                new_password,
                include_numbers,
                include_special,
                include_uppercase,
            )

            print(f"Generated password: {new_password}")
            print(f"Password strength: {strength}")

            break

        except ValueError:
            print("Please enter a whole number for the password length.")


if __name__ == "__main__":
    main()
