
user_data = {
    "username": "sajjad",
    "pass": "12345678",
    "name": "Sajjad Abdulwahid",
    "age": 21,
    "mail": "edusajjad1@gmail.com",
}


attempts_left = 3

print("--- Welcome to the Login System ---")


while attempts_left > 0:
    print(f"\nYou have {attempts_left} attempt(s) left.")
    
    
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    
    if username_input == user_data.get("username") and password_input == user_data.get("pass"):
        print("\n==============================")
        print(f" Login Successful! Welcome, {user_data['name']}.")
        print("Your Account Information:")
        
        
        for key, value in user_data.items():
            
            if key != "pass":
                print(f"- {key.capitalize()}: {value}")
        print("==============================")
        
        
        break
    else:
        
        attempts_left -= 1
        print("❌ Invalid username or password. Please try again.")

else:
    print("\n==============================")
    print("🔒 Too many failed attempts. Your account is now locked for security.")
    
    user_data.clear()
    
    print("User data has been deleted.")
    print(f"Current data state: {user_data}")
    print("==============================")