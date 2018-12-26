#########################
# creature Database File#
#########################
# Database file for the nixheads-mud codebase
# Written by Dragonkeeper
# Edited by Lunacorn to fit into the list of
# variables needed to be saved.
# Dec 25th-26th, 2018

# Import the sqlite3 library
import sqlite3

# connect to the database
def connect():
    db = sqlite3.connect('credatabase')
    init_db(db)
    return db

# Initiate the database or create one
# if it does not exist.

def init_db(db):
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS creature(room, name, desc, clvl, cstr, cdmg, cdef, clfe, life, moves, drops, cspc, csnm, ctmr, corp)')

# Execute 'save' command

def cre_load():
    cursor = db.cursor()
    cursor.execute('INSERT INTO creature(room, name, desc, clvl, cstr, cdmg, cdef, clfe, life, moves, drops, cspc, csnm, ctmr, corp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
            (room, name, desc, clvl, cstr, cdmg, cdef, clfe, life, moves, drops, cspc, csnm, ctmr, corp))
    db.commit()
    return

# Not sure how to add the other features yet

def cre_update(room, name, desc, clvl, cstr, cdmg, cdef, clfe, life, moves, drops, cspc, csnm, ctmr, corp):
    cursor = db.cursor()
    cursor.execute("UPDATE creature SET room = ? name = ? desc = ? clvl = ? cstr = ? cdmg = ? cdef =? clfe = ? life = ? moves = ? drops = ? cspc = ? csnm = ? ctmr = ? corp =? WHERE name = ?",(room, name, desc, clvl, cstr, cdmg, cdef, clfe, life, moves, drops, cspc, csnm, ctmr, corp))
    db.commit()
    return

# A way to delete players from database

def cre_corpse(db, name):
    cursor = db.cursor()
    cursor.execute('SET from creature WHERE corp = yes', (name,))
    db.commit()
    return

#

def spawn_name(db, name):
    '''reloads creature onto map'''
    cursor = db.cursor()
    rows = cursor.execute('add load from file').fetchall()
    player = [row for row in rows if name in row[0]]
#    delete_player(db, name)
    return player

