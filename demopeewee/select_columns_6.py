"""Peewee selecting specific columns"""

import peewee
import datetime

db = peewee.SqliteDatabase('test.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:

        database = db
        db_table = 'notes'


notes = Note.select(Note.text, Note.created).limit(2)

for row in notes.tuples():
    print '{:>44} on {}'.format(*row)