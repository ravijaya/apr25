#!/usr/bin/env python3

import peewee
import datetime

db = peewee.SqliteDatabase('test.db')


class Note(peewee.Model):
    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = 'notes'


note3 = Note.select().where(Note.id == 3)
print note3.sql()
