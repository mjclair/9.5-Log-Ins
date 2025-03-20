class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
    
    def describe_user(self):
        """Prints a summary of the user’s information."""
        print(f"User Profile:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}\nLocation: {self.location}\n")
    
    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back!\n")

user1 = User("Michael", "Clair", 43, "mjclair81@gmail.com", "")
user2 = User("Cameron", "Clair", 41, "cameron.clair@gmail.com", "")
user3 = User("Brian", "Clair", 72, "brian.clair@outlook.com", "")

for user in (user1, user2, user3):
    user.describe_user()
    user.greet_user()


class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        """Prints a summary of the user’s information."""
        print(f"User Profile:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}\nLocation: {self.location}\n")
    
    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back!\n")
    
    def increment_login_attempts(self):
        """Increments the login_attempts attribute by 1."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Resets the login_attempts attribute to 0."""
        self.login_attempts = 0

user = User("Michael", "Clair", 43, "mjclair81@gmail.com", "")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"Login attempts: {user.login_attempts}")

user.reset_login_attempts()

print(f"Login attempts after reset: {user.login_attempts}")

