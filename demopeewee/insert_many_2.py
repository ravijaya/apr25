import peewee
import datetime

db = peewee.SqliteDatabase('test.db')


class Note(peewee.Model):
    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = 'notes'


Note.create_table()

data = [
    {'text': 'Tai chi in the morning', 'created': datetime.date(2019, 4, 20)},
    {'text': 'Visited friend', 'created': datetime.date(2019, 4, 12)},
    {'text': 'Went to cinema', 'created': datetime.date(2019, 4, 5)},
    {'text': 'Listened to music', 'created': datetime.date(2019, 4, 28)},
    {'text': 'Watched TV all day', 'created': datetime.date(2019, 4, 14)},
    {'text': 'Worked in the garden', 'created': datetime.date(2019, 4, 22)},
    {'text': 'Walked for a hour', 'created': datetime.date(2019, 4, 28)}
]

with db.atomic() as transaction:
    # The atomic() method puts the bulk operation in a transaction.
    query = Note.insert_many(data)
    query.execute()
    transaction.commit() # transaction.rollback
