from peewee import *
from models import *


if __name__ == "__main__":

    db.connect()
    db.create_tables([Renders])

    data = [
        {'status': 'pending', 'type': 'vp9', 'force': 10},
        {'status': 'pending', 'type': 'x264', 'force': 15},
        {'status': 'pending', 'type': 'new', 'force': 20},
        {'status': 'pending', 'type': 'vp9-hd', 'force': 10},
        {'status': 'pending', 'type': 'vp9-hd+', 'force': 15},
        {'status': 'pending', 'type': 'audio_x264', 'force': 17},
        {'status': 'pending', 'type': 'audio_vp9', 'force': 17},
    ]

    for item in data:
        Renders.create(**item)

    query = Renders.select().where(Renders.status == 'pending').order_by(Renders.force.desc()).get()
    print(f'Render ID with highest priority: {query.id}')