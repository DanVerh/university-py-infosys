from productManager import prInterface
from .role import Role


def roleInterface():
    role = Role()
    if role.username == "productmanager":
        prInterface()