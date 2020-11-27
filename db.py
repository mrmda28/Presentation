from peewee import *


db = SqliteDatabase('Data/Review.db')

class Review(Model):
    class Meta:
        database = db

class Users(Review):
    id = PrimaryKeyField(null=False)
    name = TextField(null=False)
    text = TextField(null=False)

db.connect()
db.create_tables([Users])

def add(name, text):
    try:
         with db.atomic():
             Users.create(
                 name = name,
                 text = text)
    except:
        print('Ошибка при добавлении отзыва')