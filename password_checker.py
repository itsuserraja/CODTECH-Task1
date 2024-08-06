import re

common_passwords = set([
    "password", "123456", "123456789", "12345678", "12345", 
    "1234567", "123123", "qwerty", "abc123", "111111"
])

def password_strength(password):
    strength = {
        'length': False,
        'uppercase': False,
        'lowercase': False,
        'numbers': False,
        'special': False,
        'common_password': False,
        'overall': 'Weak'
    }

    if len(password) >= 8:
        strength['length'] = True

    if re.search(r'[A-Z]', password):
        strength['uppercase'] = True
    if re.search(r'[a-z]', password):
        strength['lowercase'] = True
    if re.search(r'[0-9]', password):
        strength['numbers'] = True
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength['special'] = True

    if password.lower() in common_passwords:
        strength['common_password'] = True

    if all([strength['length'], strength['uppercase'], strength['lowercase'], strength['numbers'], strength['special']]) and not strength['common_password']:
        strength['overall'] = 'Strong'
    elif (strength['length'] and ((strength['uppercase'] and strength['lowercase']) or (strength['numbers'] and strength['special']))):
        strength['overall'] = 'Moderate'
    
    return strength

def provide_feedback(strength):
    feedback = []
    
    if not strength['length']:
        feedback.append("Password should be at least 8 characters long.")
    if not strength['uppercase']:
        feedback.append("Password should include at least one uppercase letter.")
    if not strength['lowercase']:
        feedback.append("Password should include at least one lowercase letter.")
    if not strength['numbers']:
        feedback.append("Password should include at least one number.")
    if not strength['special']:
        feedback.append("Password should include at least one special character (e.g., !@#$%^&*).")
    if strength['common_password']:
        feedback.append("Password is too common. Choose a more unique password.")
    
    if not feedback:
        feedback.append("Your password is strong.")
    
    return feedback

def main():
    password = input("Enter a password to check its strength: ")
    strength = password_strength(password)
    feedback = provide_feedback(strength)
    
    print(f"Password Strength: {strength['overall']}")
    for comment in feedback:
        print(comment)

if __name__ == "__main__":
    main()
