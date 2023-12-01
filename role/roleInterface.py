from productManager.prInterface import prInterface
from role.role import Role


def roleInterface():
    role = Role()
    if role.username == "productmanager":
        prInterface()