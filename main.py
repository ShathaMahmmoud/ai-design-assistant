from validator import validate_brief

user_input = input("Enter your design request: ")

is_valid = validate_brief(user_input)

print(is_valid)