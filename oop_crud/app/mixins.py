import uuid

class CreateMixin:
    def create(self):
        data = self.read_db()
        title = input('Введите название ')
        description = input('Введите описание ')
        price = int(input('Введите цену '))
        uuid_ = str(uuid.uuid4())[:7]
        model = self.model(uuid_, title, price, description).dict()
        data['items'].append(model)
        self.write_to_db(data)


class ReadMixin:
    def read(self):
        print(self.read_db())


class ReadDetailMixin:
    def retrieve(self):
        uuid_ = input('Введите id товара ')
        print(self.get_object(uuid_))


class UpdateMixin:
    def update(self):
        db = self.read_db()
        uuid_ = input('Введите id товара ')
        data = self.get_object(uuid_)
        if isinstance(data, dict):
            db['items'].remove(data)
            title = input('Введите название ') or data['title']
            description = input('Введите описание ') or data['description']
            uuid_ = data['uuid']
            try:
                price = int(input('Введите цену '))
            except ValueError:
                price = data['price']
            model = self.model(uuid_, title, price, description).dict()
            db['items'].append(model)
            self.write_to_db(db)
        else:
            print(data)










