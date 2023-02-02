from dataclasses import dataclass, asdict
import uuid

class Model:
    def dict(self):
        return asdict(self)

@dataclass
class Product(Model):
    uuid: uuid
    title: str
    price: int
    description: str


# prod1 = Product(str(uuid.uuid4())[:8], 'Утюг', 500, 'Гладит одежду')
# print(prod1.dict())