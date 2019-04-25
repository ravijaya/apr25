import peewee
import datetime

db = peewee.SqliteDatabase('test.db')


class Note(peewee.Model):
    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = 'notes'


note2 = Note.get(Note.text == 'Listened to music')

print(note2.id)
print(note2.text)
print(note2.created)
