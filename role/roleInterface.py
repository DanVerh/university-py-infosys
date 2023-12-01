from productManager import prInterface
from warehouseWorker import wwInterface
from salesManager import salesManagerInterface
from .role import Role


def roleInterface():
    role = Role()
    if role.username == "productmanager":
        prInterface()
    elif role.username == "warehouseworker":
        wwInterface()
    elif role.username == "salesmanager":
        salesManagerInterface()

