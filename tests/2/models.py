from peewee import *

db = SqliteDatabase("renders.db")

class Renders(Model):
    id = AutoField()
    status = CharField(choices=['pending'])
    type = CharField(choices=['vp9', 'x264', 'new', 'vp9-hd', 'vp9-hd+', 'audio_x264', 'audio_vp9'])
    force = IntegerField()

    class Meta:
        database = db
