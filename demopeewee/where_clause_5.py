import peewee
import datetime

db = peewee.SqliteDatabase('test.db')


class Note(peewee.Model):
    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = 'notes'


notes = Note.select().where(Note.id > 3)
notes = Note.select().where((Note.id > 2) & (Note.id < 6))

for note in notes:
    print '{:>44} {} on {}'.format(note.id, note.text, note.created)
