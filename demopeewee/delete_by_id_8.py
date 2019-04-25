import peewee
import datetime


db = peewee.SqliteDatabase('test.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = 'notes'

n2 = Note.delete_by_id(1)
print(n2)

# query = Note.delete().where(Note.id > 3)
# n = query.execute()
# print n
