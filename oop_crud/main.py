from app.models import Product
from app.crud import CRUD
from app.mixins import CreateMixin, ReadMixin, ReadDetailMixin, UpdateMixin

class Interface(CreateMixin, ReadMixin, ReadDetailMixin, UpdateMixin, CRUD):
    model = Product


interface = Interface()
# interface.create()
# interface.read()
# interface.retrieve()
# interface.update()

# TODO: реализовать DeleteMixin в файле mixins.py
# TODO: реализовать интерфейс