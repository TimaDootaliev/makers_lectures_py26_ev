import json
from json.decoder import JSONDecodeError

class CRUD:
    def write_to_db(self, data):
        with open('db.json', 'w') as db:
            json.dump(data, db, indent=4)
    
    def read_db(self):
        try:
            with open('db.json', 'r') as db:
                return json.load(db)
        except JSONDecodeError:
            return {'items': []}

    def get_object(self, uuid):
        with open('db.json', 'r') as db:
            for item in json.load(db)['items']:
                if uuid == item['uuid']:
                    return item
            return 'Нет такого объекта'

"""  
{
    "items": [
        {
            "title": kdkd,
            "price": 38372,
            "description": fdslksdfljsd,
            "uuid": 32d2d2
        }
    ]
}
"""
    
