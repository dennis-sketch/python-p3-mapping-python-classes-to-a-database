#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song


if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
Song.create_table()
CURSOR.execute("PRAGMA table_info(songs)").fetchall()
# => [(0, 'id', 'INTEGER', 0, None, 1), (1, 'name', 'TEXT', 0, None, 0), (2, 'album', 'TEXT', 0, None, 0)]
