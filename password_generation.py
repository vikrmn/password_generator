import random
import string
def generate_password(length):
    lower = string.ascii_lowercase    
    upper = string.ascii_uppercase    
    digits = string.digits           
    special = string.punctuation      
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),  
        random.choice(upper),  
        random.choice(digits), 
        random.choice(special) 
    ]
    password += random.choices(all_characters, k=length-4)
    random.shuffle(password)
    return ''.join(password)
password_length = int(input("Enter the desired password length: "))
generated_password = generate_password(password_length)
print(f"Generated Password: {generated_password}")
