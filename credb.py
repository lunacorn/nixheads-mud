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
    db = sqlite3.connect('creaturedatabase')
    init_db(db)
    return db

# Initiate the database or create one
# if it does not exist.

def init_db(db):
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS creature(room, name, desc, clvl, cstr, cdmg, cdef, clfe, life, moves, drops, cspc, csnm, ctmr, corp)')


### load creatures 
def cload(room, name, desc, clvl, cstr, cdmg, cdef, clfe, life, moves, drops, cspc, csnm, ctmr, corp):
    cursor = db.cursor()
    cursor.execute('INSERT INTO creature(room, name, desc, clvl, cstr, cdmg, cdef, clfe, life, moves, drops, cspc, csnm, ctmr, corp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
            (room, name, desc, clvl, cstr, cdmg, cdef, clfe, life, moves, drops, cspc, csnm, ctmr, corp))
    db.commit()
    return


##this updates the creature in the database, the values you might not want to change them all, so we can remove the static ones from this command
def cupdate(room, name, desc, clvl, cstr, cdmg, cdef, clfe, life, moves, drops, cspc, csnm, ctmr, corp):
    cursor = db.cursor()
    cursor.execute("UPDATE creature SET room = ?, name = ?, desc = ?, clvl = ?, cstr = ?, cdmg = ?, cdef = ?, clfe = ?, life = ?, moves = ?, drops = ?, cspc = ?, csnm = ?, ctmr = ?, corp =? WHERE name = ?",(room, name, desc, clvl, cstr, cdmg, cdef, clfe, life, moves, drops, cspc, csnm, ctmr, corp))
    db.commit()
    return

# A way to delete creatures from database

def ccorpse(db, name):
    cursor = db.cursor()
    cursor.execute('DELETE from creature WHERE name = ?', (name,))
    db.commit()
    return

### this lets you pull a row of data that matches
## i.e of you load creature[id]["name"]   , it will pull the results into a array for you to map to creature values when needed.
def cspawn(db, name):
    cursor = db.cursor()
    rows = cursor.execute('SELECT room, name, desc, clvl, cstr, cdmg, cdef, clfe, life, moves, drops, cspc, csnm, ctmr, corp FROM creature').fetchall()
    player = [row for row in rows if name in row[0]]
    return player
