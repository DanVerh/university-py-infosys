from . import roleInput


class Role:
    def __init__(self):
        while True:
            self.username = roleInput.usernameInput()
            if self.username in roleInput.usernameCheck():
                break
            else:
                print("Username is incorrect")
        while True:
            self.password = roleInput.passwordInput()
            if self.password == roleInput.passwordCheck(self.username):
                print("Login succeeded")
                break
            else:
                print("Password is incorrect")
