# 5-10. Checking Usernames

current_users = ['john', 'jane', 'mike', 'alex', 'sarah']
new_users = ['JOHN', 'dylan', 'ALEX', 'emma', 'mia']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")
