def validate_password(password):
    if len(password) < 8 or len(password) > 64:
        return "Password must be between 8 and 64 characters"

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isspace():
            return "Password must not contain spaces"
        elif char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True

    if not has_upper:
        return "Add at least one uppercase letter"
    if not has_lower:
        return "Add at least one lowercase letter"
    if not has_digit:
        return "Add at least one number"
    if not has_special:
        return "Add at least one special character"

    return "Strong password"


password = input("Create password: ")
result = validate_password(password)
print(result)
