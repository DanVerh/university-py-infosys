from productManager import prInterface
from warehouseWorker import wwInterface
from .role import Role


def roleInterface():
    role = Role()
    if role.username == "productmanager":
        prInterface()
    elif role.username == "warehouseworker":
        wwInterface()
