import sqlite3


def connect():
    db = sqlite3.connect('database')
    init_db(db)
    return db


def init_db(db):
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS player(name, room, password)')


def save_name(db, name, room, password):
    cursor = db.cursor()
    cursor.execute('INSERT INTO player(name, room, password) VALUES(?,?,?)',
            (name, room, password))
    db.commit()
    return

def update_name(db, name, room, password):
    cursor = db.cursor()
    cursor.execute("UPDATE player SET room = ? WHERE name = ?",(room, name))
    db.commit()
    return


def delete_name(db, name):
    cursor = db.cursor()
    cursor.execute('DELETE from player WHERE name = ?', (name,))
    db.commit()
    return


def get_name(db, name):
    '''Returns a list of rows representing "player"'''
    cursor = db.cursor()
    rows = cursor.execute('SELECT name, room, password FROM player').fetchall()
    player = [row for row in rows if name in row[0]]
#    delete_player(db, name)
    return player
