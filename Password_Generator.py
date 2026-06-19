import random
import string

# collect user preferences
# length
# should contain uppercase?
# should contain special?
# should contain digits?

def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
    include_special = input("Include special characters? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()

# ensure length is valid
    if length < 6:
        print("Password length must be at least 6 characters.")
        return

# get all available characters
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all_characters = lower + uppercase + special + digits 

# randomly pick characters up to the length    
    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if include_special == "yes":
        required_characters.append(random.choice(special))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))
    remaining_length = length - len(required_characters)
    password = required_characters

# ensure we have at least one of each character type
    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)
    random.shuffle(password)
    
    str_password = "".join(password)
    return str_password

password = generate_password()
print(f"PassWord : {password}")
