from roleInput import *

class Role:
    def __init__(self):
        while True:
            self.username = usernameInput()
            if self.username in usernameCheck():
                break
        while True:
            self.password = passwordInput()
            if self.password == passwordCheck(self.username):
                print("Login succeeded")
                break