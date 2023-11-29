from roleInput import *

class Role:
    def __init__(self):
        while True:
            self.username = usernameInput()
            if self.username in usernameChck():
                break
        self.password = passwordInput()
    