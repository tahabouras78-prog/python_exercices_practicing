def checkpassword (password):
   if len (password) < 8:
       return "Weak password: must be at least 8 characters long."
   has_upper = False
   has_lower = False
   has_digit = False
   for char in password :
       if char.isupper():
           has_upper = True
       elif char.islower():
           has_lower = True
       elif char.isdigit():
            has_digit = True
            
   if has_digit and has_lower and has_upper:
      return "Strong password"
   else:
      return "Weak password: must contain at least one uppercase letter, one lowercase letter, and one digit."
   
pw = input("Enter a password to check its strength: ")        
print(checkpassword(pw))
