""" ORM - Object Relational Mapping - технология программирования, которая связывает код и работу с базой данных """

# from peewee import *
import peewee as pw

db_url = 'postgresql://tima:1@localhost:5432/cars'
db = pw.PostgresqlDatabase(db_url)

class Cars(pw.Model):
    brand = pw.CharField(50)
    year = pw.DateField()

    class Meta:
        database = db


db.connect()
db.create_tables([Cars])
db.close()