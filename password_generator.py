import string
import secrets

def password_generator(length = 10):
   
    
    letter = string.ascii_letters
    digits = string.digits
    symbol = string.punctuation
   
    
    all_chars = letter + digits + symbol
   
   
    password = [
       
        secrets.choice(letter),
        secrets.choice(digits),
        secrets.choice(symbol)
    ]
   
   
   
    for i in range(length - 3):
        password.append(secrets.choice(all_chars))
       
   
   
    secrets.SystemRandom().shuffle(password)
   
    
    return  "".join(password)
 
#---------------------------------------------------------------
# Display the application title Name
#---------------------------------------------------------------
print("=" * 40)
print("       SECURE PASSWORD GENERATOR")
print("=" * 40)

 

while True:
   
    try:
       
        length = int(input("Enter password length (3-128): "))
       
        if not  3 <= length <=128:
            print("Length must be between 3 and 128.")
           
            continue
       
        print("Your Password : ", password_generator(length))
       
    except ValueError:
        print("Error: Please enter a valid whole number.")
       
        continue
     
  
    choice = input("Generate another password? (yes/no): ")
       
    if choice.strip().lower() not in ("yes", "y"):
        print("\nThank you for using Password Generator!")
        break
       
           
   
   
   
   
   
   