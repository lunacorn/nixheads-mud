# Database file for the nixheads-mud codebase
# Written by Dragonkeeper
# Edited by Lunacorn to fit into the list of
# variables needed to be saved.
# Dec 25th-26th, 2018

# Import the sqlite3 library
import sqlite3

# connect to the database
def connect():
    db = sqlite3.connect('invdb')
    init_db(db)
    return db

# Initiate the database or create one
# if it does not exist.

def init_db(db):
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS player(name, slota, slotb, slotc, slotd, slote, slotf, slotg, sloth)')

# Execute 'save' command

def save_name(db, name, slota, slotb, slotc, slotd, slote, slotf, slotg, sloth):
    cursor = db.cursor()
    cursor.execute('INSERT INTO player(name, slota, slotb, slotc, slotd, slote, slotf, slotg, sloth) VALUES(?,?,?,?,?,?,?,?,?)',
            (name, slota, slotb, slotc, slotd, slote, slotf, slotg, sloth))
    db.commit()
    return

# Not sure how to add the other features yet

def update_name(db, name, slota, slotb, slotc, slotd, slote, slotf, slotg, sloth):
    cursor = db.cursor()
    cursor.execute("UPDATE player SET slota = ?, slotb = ?, slotc = ?, slotd = ?, slote = ?, slotf = ?, slotg = ?, sloth = ? WHERE name = ?",(slota, slotb, slotc, slotd, slote, slotf, slotg, sloth, name))
    db.commit()
    return

# A way to delete players from database

def delete_name(db, name):
    cursor = db.cursor()
    cursor.execute('DELETE from player WHERE name = ?', (name,))
    db.commit()
    return

#

def get_name(db, name):
    '''Returns a list of rows representing "player"'''
    cursor = db.cursor()
    rows = cursor.execute('SELECT name, slota, slotb, slotc, slotd, slote, slotf, slotg, sloth FROM player').fetchall()
    player = [row for row in rows if name in row[0]]
#    delete_player(db, name)
    return player
