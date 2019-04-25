import peewee
import datetime

db = peewee.SqliteDatabase('test.db')


class Note(peewee.Model):
    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = 'notes'


print 'Ascending order'
print '*****************************'

notes = Note.select(Note.text, Note.created).order_by(Note.created)

for note in notes:
    print(note.text, note.created)

print
print 'Descending order'
print '*****************************'

notes = Note.select(Note.text, Note.created).order_by(Note.created.desc())

for note in notes:
    print note.text, note.created
