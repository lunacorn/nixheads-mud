#!/usr/bin/env python

"""A simple Multi-User Dungeon (MUD) game. Players can talk to each

other, examine their surroundings and move between rooms.

Some ideas for things to try adding:

    * More rooms to explore

    * An 'emote' command e.g. 'emote laughs out loud' -> 'Mark laughs

        out loud'

    * A 'whisper' command for talking to individual players

    * A 'shout' command for yelling to players in all rooms

    * Items to look at in rooms e.g. 'look fireplace' -> 'You see a

        roaring, glowing fire'

    * Items to pick up e.g. 'take rock' -> 'You pick up the rock'

    * Monsters to fight

    * Loot to collect

    * Saving players accounts between sessions

    * A password login

    * A shop from which to buy items

author: Mark Frimston - mfrimston@gmail.com

--------------------------------------------------------------------

Nix-mud 0.1.3                           https://nixheads.co.uk

--------------------------------------------------------------------

This version implements the following features

--------------------------------------------------------------------

-- refined player creation

--------------------------------------------------------------------

    New player creation pulls from the static race and job files
    it also populates the majority of neccessary variables for
    'sheet' command.  which is a work in progress to display
    most character information and stats.

    self made character description is to come in the finished
    'sheet' command.  As the level and combat system are developed
    the skills and spells will be shown on char sheet as well.
    expect unlocked jobs to appear in upcoming micro releases.

---------------------------------------------------------------------

-- Creature Database / Object Overhaul

---------------------------------------------------------------------

    As mentioned in the first minor release the objects and maps
    are going through an overhaul.  there is a creature database
    created though not yet implemented.  It will give creatures
    assigned unique numbers and seperate them from static maps.

    Allowing them to move and be interacted with and killed as
    well as looted once the inventory database is set up.

---------------------------------------------------------------------

-- Refined maps

---------------------------------------------------------------------

    Maps are currently being templated to work with the current
    manner of interaction.  They will be bare, however crash proof
    allowing characters to move around and get aquainted with the
    game.  There will be a few randoom poke objects to interact
    with and make use of some of the commands.

---------------------------------------------------------------------

-- Comment Cleanup

---------------------------------------------------------------------

    Though this does not affect the user, the goal is to provide
    clear documentation and templates for the nixmud codebase.
    Therefore it is essential to make sure current features have
    reasonably neat and readable comments.

    You will find that much more useable moving forward, and
    expect the documentation to continue with further releases.

----------------------------------------------------------------------

-- Emergency Reset

----------------------------------------------------------------------

    We have implemented a failsafe which in times of server crash
    risk it will disconnect the player in question, and send them
    back to a usable login screen.  This will help with error
    handling and is a nice bump to start for known issues.

    currently it is only used when issues of eternal loops occur.

----------------------------------------------------------------------

Team: Dragonkeeper, Lunacorn  Dec 26th, 2018

--------------------------------------------------------------------

Nix-mud 0.2.3                           https://nixheads.co.uk

--------------------------------------------------------------------

This version implements the following features

--------------------------------------------------------------------

-- full implementation of classes

--------------------------------------------------------------------

    At this point all json data is loaded from corefunctions or maps
    files, into classes to allow status changes or the ability for
    creatures to move.  This has been a large shift and we are
    excited for the possibilities this creates leading us from static
    files.  The creature database and object overhaul is finished.

---------------------------------------------------------------------

-- GM commands

---------------------------------------------------------------------

    Though not finished there are now gm specific commands like
    system message and shutdown of server which is neccessary as
    you obviously dont want players having this access.  The way to
    acquire gm is still undecided currently.

---------------------------------------------------------------------

-- Stabilization of Maps

---------------------------------------------------------------------

    Unfinished maps are now isolated and objects and names added to
    map files allowing for a crash free experience while exploring
    available areas.
---------------------------------------------------------------------

-- Fight Command

---------------------------------------------------------------------

    Fights are now possible though not finished.  You can soon
    expect the experience point system to be implemented and the
    ability to level up.  As well as skills and spells the fight
    command is a current focus of the project.

----------------------------------------------------------------------

-- Objects and Containers

----------------------------------------------------------------------

    Another current project focus is objects and containers.  soon
    You will see a new database allowing storage of items and a full
    implementation of commands allowing you to put and get items from
    containers like buckets or a backpack etc.

----------------------------------------------------------------------

-- Grab, Give, Drop

----------------------------------------------------------------------

    Among other commands these are highlights of this release
    including the ability to equip items and a new equipment sheet and
    fully functional inventory.

----------------------------------------------------------------------
Team: Dragonkeeper, Lunacorn  Jan 2nd, 2019

"""""""""""

# basic files to import
# including the json
# library
import datetime
import time
import db as database
import json
import invdb as invendb
import sys
import inspect
##used random for item numbers
import random
# import the MUD server class

from mudserver import MudServer



#sys.setrecursionlimit()
### create a class to map all the creatures into
### saving space and effort adding in all creatures
### automatically adding in new creatures added to json
class Creatures(object):
    creatures = {}
    def __init__(self, cid, name, room, desc, clvl, cstr ,cdmg ,cdef ,clfe ,life ,moves ,drops ,cspc ,csnm , ctmr, corp):
        self.cid = cid
        self.name = name
        self.room = room
        self.desc = desc
        self.clvl = clvl
        self.cstr = cstr
        self.cdmg = cdmg
        self.cdef = cdef
        self.clfe = clfe
        self.life = life
        self.moves = moves
        self.drops = drops
        self.cspc = cspc
        self.csnm = csnm
        self.ctmr = ctmr
        self.corp = corp
        Creatures.creatures[cid] = self

class Npcs(object):
    npcs = {}
    def __init__(self, nid, name, room, desc, nsay, nsayt, ngive, reward ,buytype):
        self.cid = nid
        self.name = name
        self.room = room
        self.desc = desc
        self.nsay = nsay
        self.nsayt = nsayt
        self.ngive = ngive
        self.reward = reward
        self.buytype = buytype
        Npcs.npcs[nid] = self

class Items(object):
    allitems = {}
    def __init__(self, iid, name, desc, room, type, eqtype, invdesc, bp, bpsize, eqstata, eqstatb, eqsvala, eqsvalb, sellval):#, eqstatus):
        self.iid = iid
        self.name = name
        self.desc = desc
        self.room = room
        self.type = type
        self.eqtype = eqtype
        self.invdesc = invdesc
        self.bp = bp
        self.bpsize = bpsize
        self.eqstata = eqstata
        self.eqstatb = eqstatb
        self.eqsvala = eqsvala
        self.eqsvalb = eqsvalb
        self.sellval = sellval
        Items.allitems[iid] = self

class Doors(object):
    doors = {}
    def __init__(self, did, ename, estatus, elock, dt, map, exits, mapto, gotopened):
        self.did = did
        self.name = ename
        self.status = estatus
        self.elock = elock
        self.dtimer = dt
        self.gotopened = gotopened
        self.map = map
        self.exits = exits
        self.mapto = mapto
        Doors.doors[did] = self

class Containers(object):
    containers = {}
    def __init__(self, cnid, cnname, cnmap, cnstatus, cnlock, slots, lockname):
        self.cnid = cnid
        self.name = cnname
        self.map  = cnmap
        self.status = cnstatus
        self.lock = cnlock
        self.slots = slots
        self.lockname = lockname
        Containers.containers[cnid] = self

# import core values
with open("corefunctions.json") as funcs:
    fun = json.load(funcs)

# import map files
with open("Maps/starter.json") as room:
    map1 = json.load(room)
with open("Maps/dungeon.json") as room:
    map2 = json.load(room)
with open("Maps/town.json") as room:
    map3 = json.load(room)
with open("Maps/townstores.json") as room:
    map4 = json.load(room)
with open("Maps/garden.json") as room:
    map5 = json.load(room)
with open("Maps/desert.json") as room:
    map6 = json.load(room)
with open("Maps/swamp.json") as room:
    map7 = json.load(room)
# all the map files together
rooms = {**map1, **map2, **map3, **map4, **map5, **map6, **map7}

# import creature files
with open("Creatures/creatures1.json") as cre:
    credb = json.load(cre)

# import ascii files
motd       = open("Art/MOTD")
logascii   = open("Art/login")
todo       = open("Art/todo")
helpo      = open("Help/helpnew")
helpt      = open("Help/helpnew2")

# import help files
# this will be implemented
# in the near future.
# currently still using
# 'help' command

with open("Help/help1.json") as helpfile:
    helpfiles = json.load(helpfile)

# move this next comment down and comment for class

# initilize dictionaries

playerprocess = {}
login = {}
setups = {}
players = {}

# start the server

mud = MudServer()

##connect to db for player saves
userdata = database.connect()
invdata = invendb.connect()

## list holds all data for creature names when they get dumped to class
allitemslist = []
defaultsitemslist = []
creaturelist = []
room = []
myroom = []
doorslist = []
containerslist = []
monstercount = 0
########### this grabs from the json for creatures
for cid in credb.keys():
    number = 0
    for stat in credb[cid]:
# pulls needed data as normal and removes any " " from results
        value = str(json.dumps(credb[cid][stat])).replace('"', '')
### quick ifs to check if values match what need and stores them to be imported after
        if stat == "cid":
            ncid = value
        if stat == "name":
            name = value
        if stat == "desc":
            desc = value
        if stat == "clvl":
            clvl = value
        if stat == "cstr":
            cstr = value
        if stat == "cdmg":
            cdmg = value
        if stat == "cdef":
            cdef = value
        if stat == "clfe":
            clfe = value
        if stat == "life":
            life = value
        if stat == "moves":
            moves = value
        if stat == "drops":
            drops = value
        if stat == "cspc":
            cspc = value
        if stat == "csnm":
            csnm = value
        if stat == "ctmr":
            ctmr = value
        if stat == "corp":
            corp = value
        if stat == "room":
            room = []
            for place in credb[cid][stat]:
                value = str(json.dumps(credb[cid][stat][place])).replace('"', '')
                room.append(place+":"+value)
############ loads every creature into class
    if room:
        for sweetpad in room:
            myroom = [x.strip() for x in sweetpad.split(':')]
            count = 1
            while count <= int(myroom[1]):
                count += 1
                monstercount += 1
                if not str(ncid+str(monstercount)) in creaturelist:
                    Creatures(str(ncid+str(monstercount)), name, myroom[0], desc, clvl, cstr, cdmg, cdef, clfe, life, moves, drops, cspc, csnm, ctmr, corp)
                    creaturelist.append(Creatures.creatures[str(ncid+str(monstercount))].cid)

#### we need to load the items into the class
for itemcat in fun ["corevalues"]["items"]:
    for item in fun["corevalues"]["items"][itemcat]:
        for stat in fun["corevalues"]["items"][itemcat][item]:
                value = str(json.dumps(fun["corevalues"]["items"][itemcat][item][stat])).replace('"', '')
                if stat == "iid":
                    iid = value
                if stat == "name":
                    name = value
                if stat == "desc":
                    desc = value
                if stat == "room":
                    room = value
                if stat == "type":
                    type = value
                if stat == "eqtype":
                    eqtype = value
                if stat == "invdesc":
                    invdesc = value
                if stat == "bp":
                    bp = value
                if stat == "bpsize":
                    bpsize = value
                if stat == "eqstata":
                    eqstata = value
                if stat == "eqstatb":
                    eqstatb = value
                if stat == "eqsvala":
                    eqsvala = value
                if stat == "eqsvalb":
                    eqsvalb = value
                if stat == "sellval":
                    sellval = value
        newiid = str(iid)+str(random.randint(100,10000000000))
        if not str(newiid) in allitemslist:
            Items(newiid ,name, desc, room, type, eqtype, invdesc, bp, bpsize, eqstata, eqstatb, eqsvala, eqsvalb, sellval) #, eqstatus)
            allitemslist.append(Items.allitems[str(newiid)].iid)

#### we need to load the items into the class defaultly
for itemcat in fun ["corevalues"]["items"]:
    for item in fun["corevalues"]["items"][itemcat]:
        for stat in fun["corevalues"]["items"][itemcat][item]:
                value = str(json.dumps(fun["corevalues"]["items"][itemcat][item][stat])).replace('"', '')
                if stat == "iid":
                    iid = value
                if stat == "name":
                    name = value
                if stat == "desc":
                    desc = value
                if stat == "room":
                    room = "fuckall"
                if stat == "type":
                    type = value
                if stat == "eqtype":
                    eqtype = value
                if stat == "invdesc":
                    invdesc = value
                if stat == "bp":
                    bp = value
                if stat == "bpsize":
                    bpsize = value
                if stat == "eqstata":
                    eqstata = value
                if stat == "eqstatb":
                    eqstatb = value
                if stat == "eqsvala":
                    eqsvala = value
                if stat == "eqsvalb":
                    eqsvalb = value
                #if stat == "eqstatus":
                #    eqstatus = value
        if not str(iid) in defaultsitemslist:
            Items(iid ,name, desc, room, type, eqtype, invdesc, bp, bpsize, eqstata, eqstatb, eqsvala, eqsvalb, sellval) #, eqstatus)
            defaultsitemslist.append(Items.allitems[str(iid)].iid)


for room in rooms:
    ename = ''
    estatus = ''
    elock = ''
    dt = ''
    omap = ''
    exits = ''
    mapto = ''
    for a in [rooms[room]]:
        for x in a:
            if x == "exits":
                for y in rooms[room][x]:
                    if y == '':
                        for z in rooms[room][x][y]:
                            dt = 60
                            gotopened = 0
                            if z == "object":
                                ename = rooms[room][x][y][z]
                            if z == "otimer":
                                dt = rooms[room][x][y][z]
                            if z == "status":
                                estatus = rooms[room][x][y][z]
                            if z == "locked":
                                elock = rooms[room][x][y][z]
                            omap = room
                            if z == "exits":
                                exits = rooms[room][x][y][z]
                            if z == "mapto":
                                mapto = rooms[room][x][y][z]
                        did = "door"+str(random.randint(100,10000000000))
                        Doors(did, ename, estatus, elock, dt, omap, exits, mapto, gotopened)
                        doorslist.append(did)

for container in fun["corevalues"]["containers"]:
    for cnvalue in fun["corevalues"]["containers"][container]:
        if cnvalue == "name":
            cnname = fun["corevalues"]["containers"][container][cnvalue]
        if cnvalue == "room":
            cnmap = fun["corevalues"]["containers"][container][cnvalue]
        if cnvalue == "status":
            cnstatus = fun["corevalues"]["containers"][container][cnvalue]
        if cnvalue == "locked":
            cnlock = fun["corevalues"]["containers"][container][cnvalue]
        if cnvalue == "lockname":
            lockname = fun["corevalues"]["containers"][container][cnvalue]
        if cnvalue == "slots":
            slots = fun["corevalues"]["containers"][container][cnvalue]
    cnid = "cntr"+str(random.randint(100,10000000000))
    Containers(cnid, cnname, cnmap, cnstatus, cnlock, slots, lockname)
    containerslist.append(cnid)

print(containerslist)

for xx in allitemslist:
    print(xx+" : "+Items.allitems[xx].room)
for yy in defaultsitemslist:
    print(yy+" : "+Items.allitems[yy].room)
    allitemslist.append(yy)

######function to assign blank ids for new players
def AssignNewPlayersIDsP():
    # customizable player process per id
    playerprocess[id] = {
        "process": None,
        "selection": None
        }

    login[id] = {
        "process": None,
        "name": None,
        "password": None
        }

        # The attributes of setups and players.  Notice the differences
        # between them.  See 'new' command for better understanding of
        # setups.
    setups[id] = {
        "setup": None,
        "confirm": None,
        "match": None,
        "name": None,
        "pickrace" : None,
        "race": None,
        "job": None,
        "pickjob": None,
        "user" : None,
        "email": None,
        "password": None,
        }
def AssignNewPlayersIDs():
    players[id] = {
        "name": None,
        "email": None,
        "password": None,
        "level":None,
        "exp": 0,
        "next": 3000,
        "hp": None,
        "maxhp": None,
        "mp": None,
        "maxmp": None,
        "tp": None,
        "str": None,
        "dex": None,
        "vit": None,
        "int": None,
        "mnd": None,
        "cha": None,
        "crit": None,
        "spells": None,
        "skills": None,
        "corp": None,
        "jskill": None,
        "inv": None,
        "room": None,
        "user": None,
        "race": None,
        "job": None,
        "ujob": None,
        "status": None,
        "statustimer": 0,
        "fightstarted": 0,
        "target": '',
        "outcome": '',
        "firstround": '',
        "goesfirst": '',
        "monster": '',
        "timer": 0,
        "fighttimer": 30,
        "pvp": None,
        "inventoryspace": 8,
        "inventoryused": 0,
        "inventoryslot": {
            "slot1": "Empty",
            "slot2": "Empty",
            "slot3": "Empty",
            "slot4": "Empty",
            "slot5": "Empty",
            "slot6": "Empty",
            "slot7": "Empty",
            "slot8": "Empty",
            },
        "ujoblevel": {
                  "warrior": 0,
                  "whitemage": 0,
                  "thief": 0,
                  "indecisive": 0,
                  "bard": 0,
                  "blackmage": 0,
                  "samurai": 0,
                  "ninja": 0,
                  "bartender": 0,
                  "mog": 0,
                  "linecook": 0,
                  "inventor": 0,
                  "landscaper": 0,
                  "druid": 0,
                  "witch": 0
                },
        "ujob": {
                "warrior": "X",
                "whitemage": "X",
                "thief": "X",
                "indecisive": " ",
                "bard": " ",
                "blackmage": "X",
                "samurai": " ",
                "ninja": " ",
                "bartender": " ",
                "mog": " ",
                "linecook": " ",
                "inventor": " ",
                "landscaper": " ",
                "druid": " ",
                "witch": " "
                },
        "head": "Empty",
        "body": "Empty",
        "hands": "Empty",
        "legs": "Empty",
        "feet": "Empty",
        "weapon": "Empty",
        "offhand": "Empty",
        "ear": "Empty",
        "neck": "Empty",
        "waist": "Empty",
        "ringl": "Empty",
        "ringr": "Empty",
        "back": "Empty",
        "bag": "Empty",
        "coin": 0
    }
#### functions for commands

# change job function
def ChangeJob(pr, pj):

    for stat in fun["corevalues"]["races"][pr]:
        if stat != "description":
            attribs = json.dumps(fun["corevalues"]["races"][pr][stat])
            statvalues = json.dumps(fun["corevalues"]["jobs"][pj])
            for jobs in fun["corevalues"]["jobs"][pj]:
                if stat == jobs:
                    value = int(attribs) + int(fun["corevalues"]["jobs"][pj][jobs])
                    players[id][stat] = value


def Login():
    AssignNewPlayersIDs()
    mud.send_message(id, "Are you a 'new' player or would you like to 'login'?")

## summon inventory list
def InventoryCommand():
    mud.send_message(id, "You can hold {} more items.".format((players[id]["inventoryspace"] - players[id]["inventoryused"])))
    mud.send_message(id, ":"*35)
    mud.send_message(id, ":::::::::::::INVENTORY::::::::::::::")
    mud.send_message(id, ":"*35)
    for x in players[id]["inventoryslot"]:
        if players[id]["inventoryslot"][x] != "Empty":
            for i in [players[id]["inventoryslot"][x]]:
                print(Items.allitems[i].iid)
                mud.send_message(id, "::"+str(Items.allitems[i].name))
        else:
            mud.send_message(id, "Empty")

def ShutdownCommand():
    print("Mud shutdown")
    print("Reason: ", params)
    for pid, pl in players.items():
        mud.send_message(pid, "Saving your data because server is shutting down.")
        SaveCommand()
    mud.shutdown()

def ResetCommand():

    login[id] = {x: None for x in login[id]}
    players[id] = {x: None for x in players[id]}
    setups[id] = {x: None for x in setups[id]}
    Login()

def SaveCommand():
    # checks database
    userlist = database.get_name(userdata, players[id]["name"])
    if not userlist:
        # function for when a userlist does not exists
        mud.send_message(id, "Creating new save")
        print(players[id]["status"])
        database.save_name(userdata, players[id]["name"], players[id]["room"], players[id]["password"], players[id]["email"], players[id]["user"], players[id]["race"], players[id]["job"], players[id]["coin"], json.dumps(players[id]["ujob"]), players[id]["exp"], json.dumps(players[id]["ujoblevel"]), players[id]["status"])
        invendb.save_name(invdata, players[id]["name"], players[id]["inventoryslot"]["slot1"], players[id]["inventoryslot"]["slot2"], players[id]["inventoryslot"]["slot3"], players[id]["inventoryslot"]["slot4"],  players[id]["inventoryslot"]["slot5"], players[id]["inventoryslot"]["slot6"], players[id]["inventoryslot"]["slot7"], players[id]["inventoryslot"]["slot8"], players[id]["head"], players[id]["body"], players[id]["hands"], players[id]["legs"], players[id]["feet"], players[id]["weapon"], players[id]["offhand"], players[id]["ear"], players[id]["neck"], players[id]["waist"], players[id]["ringl"], players[id]["ringr"], players[id]["back"], players[id]["bag"])
        print("Created a new save file for: "+players[id]["name"])
    else:
        # updates save file
        database.update_name(userdata, players[id]["name"], players[id]["room"], players[id]["password"], players[id]["email"], players[id]["user"], players[id]["race"], players[id]["job"], players[id]["coin"],json.dumps(players[id]["ujob"]), players[id]["exp"], json.dumps(players[id]["ujoblevel"]), players[id]["status"])
        invendb.update_name(invdata, players[id]["name"], players[id]["inventoryslot"]["slot1"], players[id]["inventoryslot"]["slot2"], players[id]["inventoryslot"]["slot3"], players[id]["inventoryslot"]["slot4"],  players[id]["inventoryslot"]["slot5"], players[id]["inventoryslot"]["slot6"], players[id]["inventoryslot"]["slot7"], players[id]["inventoryslot"]["slot8"], players[id]["head"], players[id]["body"], players[id]["hands"], players[id]["legs"], players[id]["feet"], players[id]["weapon"], players[id]["offhand"], players[id]["ear"], players[id]["neck"], players[id]["waist"], players[id]["ringl"], players[id]["ringr"], players[id]["back"], players[id]["bag"])
        mud.send_message(id, "Updated your file.")
        print("Updated save file for: "+players[id]["name"])



def ItemsCheckRoom(pr):
    items = []
    for itemsx in allitemslist:
       if itemsx == Items.allitems[itemsx].iid:
           if pr == Items.allitems[itemsx].room:
               items.append(itemsx)
    return items

def ContainersCheckRoom(pr):
    myconts = []
    for conts in containerslist:
        if conts == Containers.containers[conts].cnid:
            if pr == Containers.containers[conts].map:
                myconts.append(conts)
    return myconts
def DoorsCheckRoom(pr):
    mydoors = []
    for doors in doorslist:
        if doors == Doors.doors[doors].did:
            if pr == Doors.doors[doors].map:
                mydoors.append(doors)
    return mydoors
#def OpenCommand():

    #opens objects like doors or closed status
    #containers.  checks object for open, closed
    #switch. which might reveal an exit or a
    #container


#def GetCommand():
    # same as grab but an extra param for the container
    # like the bucket.  maybe we can add this option to grab
    # so grab (item): room
    # grab (item) (bucket): container

#def PutCommand():
    # similar to grab n drop but puts the item into a container
    # obeject like a bucket.  object needs to be checked for
    # type : container in corefunctions, and the object class
    # needs to be written to give inventory to the container

def GrabCommand():
    gotitem = 0 ## needed to check if item was taken
    text = str(params.lower()).split(' ')
    item = ItemsCheckRoom(players[id]["room"]) # takes all items in current room
    cont = ContainersCheckRoom(players[id]["room"])
    mob = CreatureCheckRoom(players[id]["room"])
    x = 1
    for c in cont:
        if gotitem == 0:
            try:
                if text[1] == Containers.containers[c].name:
                    for y in Containers.containers[c].slots:
                        print("got here")
                        for z in allitemslist:
                            if text[0] == Items.allitems[z].name and Containers.containers[c].slots[y] == text[0]:
                                if players[id]["inventoryspace"] > players[id]["inventoryused"]:
                                    for x in players[id]["inventoryslot"]:
                                        for s in [players[id]["inventoryslot"][x]]: ##extra [] for stoping s being char by char
                                            if s == "Empty":
                                                if gotitem == 0:
                                                    orig = z[:4]
                                                    newiid = orig+str(random.randint(100,10000000000))
                                                    while newiid in allitemslist:
                                                        newiid = orig+str(random.randint(100,10000000000))
                                                    allitemslist.append(newiid)
                                                    Items(newiid ,Items.allitems[orig].name, Items.allitems[orig].desc, players[id]["name"], Items.allitems[orig].type, Items.allitems[orig].eqtype, Items.allitems[orig].invdesc,            Items.allitems[orig].bp, Items.allitems[orig].bpsize, Items.allitems[orig].eqstata, Items.allitems[orig].eqstatb, Items.allitems[orig].eqsvala, Items.allitems[orig].eqsvalb,Items.allitems[orig].sellval)
                                                    Containers.containers[c].slots[y] = "Empty"
                                                    mud.send_message(id, "You pick up the "+str(Items.allitems[z].name))
                                                    players[id]["inventoryslot"][x] = str(Items.allitems[z].iid)
                                                    players[id]["inventoryused"] += 1
                                                    gotitem = 1
                                                    break

                                else:
                                    mud.send_message(id, "Your inventory is full.")
                                gotitem = 1
            except:
                pass

    for m in mob:
        if gotitem == 0:
            try:
                if text[1] == Creatures.creatures[m].name and Creatures.creatures[m].corp == "yes":
                    for z in allitemslist:
                        if text[0] == Items.allitems[z].name and Creatures.creatures[m].drops == text[0]:
                            if players[id]["inventoryspace"] > players[id]["inventoryused"]:
                                for x in players[id]["inventoryslot"]:
                                    for s in [players[id]["inventoryslot"][x]]: ##extra [] for stoping s being char by char
                                        if s == "Empty":
                                            if gotitem == 0:
                                                orig = z[:4]
                                                newiid = orig+str(random.randint(100,10000000000))
                                                while newiid in allitemslist:
                                                    newiid = orig+str(random.randint(100,10000000000))
                                                allitemslist.append(newiid)
                                                Items(newiid ,Items.allitems[orig].name, Items.allitems[orig].desc, players[id]["name"], Items.allitems[orig].type, Items.allitems[orig].eqtype, Items.allitems[orig].invdesc, Items.allitems[orig].bp, Items.allitems[orig].bpsize, Items.allitems[orig].eqstata, Items.allitems[orig].eqstatb, Items.allitems[orig].eqsvala, Items.allitems[orig].eqsvalb,Items.allitems[orig].sellval)
                                                Creatures.creatures[m].drops = "Empty"
                                                mud.send_message(id, "You pick up the "+str(Items.allitems[z].name))
                                                players[id]["inventoryslot"][x] = str(Items.allitems[z].iid)
                                                players[id]["inventoryused"] += 1
                                                gotitem = 1
                                                break
            except:
                pass
    for i in item:
        if gotitem == 0:
            if params.lower() == Items.allitems[i].name:
                if players[id]["inventoryspace"] > players[id]["inventoryused"]:
                    for x in players[id]["inventoryslot"]:
                        for s in [players[id]["inventoryslot"][x]]: ##extra [] for stoping s being char by char
                            if s == "Empty":
                                if gotitem == 0:
                                    mud.send_message(id, "You pick up the "+str(Items.allitems[i].name))
                                    Items.allitems[i].room = players[id]["name"]
                                    players[id]["inventoryslot"][x] = str(Items.allitems[i].iid)
                                    players[id]["inventoryused"] += 1
                                    gotitem = 1
                else:
                    mud.send_message(id, "Your inventory is full.")
                    gotitem = 1
            elif gotitem == 1:
                mud.send_message(id, "You think you're grabbing something?\n I think your VR broke.  welcome back to reality.")
    if gotitem == 0:
        mud.send_message(id, "You think you're grabbing something?\n I think your VR broke.  welcome back to reality.")

def GiveCommand():
    text = str(params.lower()).split(' ')  ## we need to seperate the input
    try:
        reciever = text[0] ## players name is the 1st param
        gift = text[1] ### item given is the 2nd param
        gaveitem = 0
        items = ItemsCheckRoom(players[id]["name"]) ## all items in inventory should be in room / player
        for pid, pl in players.items():
            if players[pid]["room"] != players[id]["room"]: #and players[pid]["name"] == reciever:
                if players[pid]["name"] == reciever:
                    mud.send_message(id, "They are not in your room... we are letting them know you cant read 'look'")
                    mud.send_message(pid, players[id]["name"]+" tried to send you an item, but postal service is on strike")
                    gaveitem = 1
                    break
            if players[pid]["room"] == players[id]["room"] and players[pid]["name"] == reciever:
                for item in items:
                    if gift == Items.allitems[item].name:
                        for x in players[id]["inventoryslot"]:
                            for s in [players[id]["inventoryslot"][x]]:
                                if s != "Empty" and s == item:
                                    if players[pid]["inventoryspace"] > 0:
                                        for y in players[pid]["inventoryslot"]:
                                            for z in [players[pid]["inventoryslot"][y]]:
                                                if z == "Empty" and gaveitem == 0:
                                                    players[id]["inventoryslot"][x] = "Empty"
                                                    players[pid]["inventoryspace"] -= 1
                                                    players[id]["inventoryspace"] += 1
                                                    orig = item[:4]
                                                    print("orig: "+orig)
                                                    newiid = orig+str(random.randint(100,10000000000))
                                                    while newiid in allitemslist:
                                                        newiid = orig+str(random.randint(100,10000000000))
                                                    print("newiid: "+newiid)
                                                    allitemslist.append(newiid)
                                                    allitemslist.remove(item)
                                                    Items(newiid ,Items.allitems[orig].name, Items.allitems[orig].desc, players[pid]["name"], Items.allitems[orig].type, Items.allitems[orig].eqtype, Items.allitems[orig].invdesc, Items.allitems[orig].bp, Items.allitems[orig].bpsize, Items.allitems[orig].eqstata, Items.allitems[orig].eqstatb, Items.allitems[orig].eqsvala, Items.allitems[orig].eqsvalb, Items.allitems[orig].sellval)
                                                    players[pid]["inventoryslot"][y] = newiid
                                                    del(Items.allitems[item])
                                                    gaveitem = 1
                                                    if reciever == players[id]["name"]:
                                                        mud.send_message(id, "wow you found the secret command to sort inventory items")
                                                    else:
                                                        mud.send_message(id, "sent: "+ gift)
                                                        mud.send_message(pid, players[id]["name"]+" sent you: "+gift)
        if gaveitem == 0:
            mud.send_message(id, "you two both might wanna check inventory space and or know what you're sending.")
            mud.send_message(id, "ya know, commands only work if you actually use them right... just sayin.")
    except IndexError:
        mud.send_message(id, "Give <person> <item> ... okay back to the basics")


def DropCommand():  ## find item, assign new iid and room, delete old iid
    droppeditem = 0
    for x in players[id]["inventoryslot"]:
        for s in [players[id]["inventoryslot"][x]]:
            if s != "Empty":
                print(Items.allitems[s].name)
                if params.lower() == Items.allitems[s].name and droppeditem == 0:
                    players[id]["inventoryslot"][x] = "Empty"
                    newiid = str(Items.allitems[s].iid)+str(random.randint(100,10000000000))
                    Items(newiid ,Items.allitems[s].name, Items.allitems[s].desc, players[id]["room"], Items.allitems[s].type, Items.allitems[s].eqtype, Items.allitems[s].invdesc, Items.allitems[s].bp, Items.allitems[s].bpsize, Items.allitems[s].eqstata, Items.allitems[s].eqstatb, Items.allitems[s].eqsvala, Items.allitems[s].eqsvalb)
                    allitemslist.append(Items.allitems[str(newiid)].iid)
                    allitemslist.remove(s)
                    droppeditem = 1
                    players[id]["inventoryused"] -= 1
                    mud.send_message(id, "You drop: "+str(Items.allitems[s].name))
                    del(Items.allitems[s])
    if droppeditem == 0:
        mud.send_message(id, "Only thing dropping is your IQ.")


def ExamCommand():
    # sets the ding
    ding = 0
    # store the player's current room
    rm = rooms[players[id]["room"]]
    # store the object name
    oj = params.lower()
    text = str(params.lower()).split(' ')
    # checks for relevant info
    item = ItemsCheckRoom(players[id]["room"])
    cont = ContainersCheckRoom(players[id]["room"])
    try:
        for c in cont:
            if text[1] == "list":
                if text[0] == Containers.containers[c].name:
                    mud.send_message(id, "You peek inside the {} and see the following:".format(Containers.containers[c].name))
                    for y in Containers.containers[c].slots:
                        mud.send_message(id, Containers.containers[c].slots[y])
                        ding=1
    except:
        pass
    #if the object exists in room
    for i in item:
        if ding == 0 and oj == Items.allitems[i].name:
            mud.send_message(id, Items.allitems[i].invdesc)
            ding = 1

    if ding == 0 and oj in rm["objects"]:
        # Show object exam description
        mud.send_message(id, rm["objects"][oj])
        ding = 1
        # Otherwise tell them they are stupid
    if ding == 0:
        mud.send_message(id, "Nothing like that to examine.")


def SheetCommand():
    ## luna # i want to add some math to this as well to structure it based on line length
    # add unlocked jobs (ujobs) spells and skills
    mud.send_message(id, ":"*62)
    mud.send_message(id, ":"*62)
    mud.send_message(id, ":"*62)
    mud.send_message(id, ":"*23+"CHARACTER SHEET"+":"*24)
    mud.send_message(id, ":"*62)
    mud.send_message(id, ":"*62)
    mud.send_message(id, "{}Name: {}  {}Race: {}  {}Level: {}   {}".format(":"*3,players[id]["name"],":"*8,players[id]["race"],":"*8,players[id]["level"],":"*5))
    mud.send_message(id, ":"*62)
    mud.send_message(id, "{}HP: {}   {}MAX HP: {}   {}MP: {}   {}MAX MP: {}   ".format(":"*2,players[id]["hp"],":"*4,players[id]["maxhp"],":"*4,players[id]["mp"],":"*5,players[id]["maxmp"],":"*7))
    mud.send_message(id, ":"*62)
    mud.send_message(id, ":"*22+" Character Stats "+":"*23)
    mud.send_message(id, ":"*62)
    mud.send_message(id, "{}STR:{} {}DEX:{} {}VIT:{} {}INT:{} {}MND:{} {}CHA:{} {}".format(":"*2,players[id]["str"],":"*2,players[id]["dex"],":"*2,players[id]["vit"],":"*2,players[id]["int"],":"*4,players[id]["mnd"],":"*2,players[id]["cha"],":"*6))
    mud.send_message(id, ":"*62)
    #if players[id]["next"] - players[id]["exp"] > 100:
    #    bob = players[id]["next"]-players[id]["exp"]
    #    mud.send_message(id, "{}Crit. Chance{} {}% {}Coin{} {} {}TNL{} {} {}".format(":"*2,":"*3,players[id]["crit"],":"*3,":"*3,players[id]["coin"],":"*5,":"*3,str(bob)[3:]+"K",":"*6))
    #else:
    mud.send_message(id, "{}Crit. Chance{} {}% {}Coin{} {} {}TNL{} {} {}".format(":"*2,":"*3,players[id]["crit"],":"*3,":"*3,players[id]["coin"],":"*5,":"*3,players[id]["next"]-players[id]["exp"],":"*6))
    mud.send_message(id, ":"*62)
    mud.send_message(id, "::Spells"+":"*54)
    mud.send_message(id, ":"*62)

    #mud.send_message(id, "::{}".format([fun["corevalues"]["jobs"][players[id]["job"]]["spells"][str(players[id]["level"]).replace("'spell'"," ")]]))
    mud.send_message(id, "::"+" "*58+"::")
    mud.send_message(id, "::"+" "*58+"::")
    mud.send_message(id, "::"+" "*58+"::")
    mud.send_message(id, "::"+" "*58+"::")
    mud.send_message(id, "::"+" "*58+"::")
    mud.send_message(id, "::"+" "*58+"::")
    mud.send_message(id, ":"*62)
    mud.send_message(id, "::Skills"+":"*54)
    mud.send_message(id, ":"*62)
    #mud.send_message(id, "::{}".format([fun["corevalues"]["jobs"][players[id]["job"]]["skills"][str(players[id]["level"]).replace("'spell'"," ")]]))
    mud.send_message(id, "::"+" "*58+"::")
    mud.send_message(id, "::"+" "*58+"::")
    mud.send_message(id, "::"+" "*58+"::")
    mud.send_message(id, "::"+" "*58+"::")
    mud.send_message(id, "::"+" "*58+"::")
    mud.send_message(id, "::"+" "*58+"::")
    mud.send_message(id, "::"+" "*58+"::")
    mud.send_message(id, ":"*62)
    mud.send_message(id, "::User Rank"+":"*9+"Current Job"+":"*6+"PVP Status"+":"*4+"TP"+":"*9)
    mud.send_message(id, ":: {}".format(players[id]["user"]) + "     :::::::: {} ::::::: {} :::::::: {} :::::::".format(players[id]["job"],players[id]["pvp"],players[id]["tp"]))
    mud.send_message(id, ":"*62)
    mud.send_message(id, "::Unlocked Jobs"+":"*47)
    mud.send_message(id, ":::warrior:{}::whitemage:{}::thief:{}::indecisive:{}::bard:{}::::::".format(players[id]["ujob"]["warrior"],players[id]["ujob"]["whitemage"],players[id]["ujob"]["thief"],players[id]["ujob"]["indecisive"],players[id]["ujob"]["bard"]))
    mud.send_message(id, ":"*62)
    mud.send_message(id, ":::blackmage:{}::samurai:{}::ninja:{}::bartender:{}::mog:{}::::::::".format(players[id]["ujob"]["blackmage"],players[id]["ujob"]["samurai"],players[id]["ujob"]["ninja"],players[id]["ujob"]["bartender"],players[id]["ujob"]["mog"]))
    mud.send_message(id, ":"*62)
    mud.send_message(id, ":::linecook:{}::inventor:{}::landscaper:{}::druid:{}::witch:{}:::::".format(players[id]["ujob"]["linecook"],players[id]["ujob"]["inventor"],players[id]["ujob"]["landscaper"],players[id]["ujob"]["druid"],players[id]["ujob"]["witch"]))
    mud.send_message(id, ":"*62)
    mud.send_message(id, ":"*62)
    mud.send_message(id, ":"*62)

    #help me god need to print out the right format for json files
    #mud.send_message(id, "{}".format([fun["corevalues"]["jobs"][players[id]["job"]]["spells"][str(players[id]["level"]).replace("'spell'"," ")]]))

def EquipmentCommand():
    ###  prints slots available

    mud.send_message(id, "***************************************")
    mud.send_message(id, "******************EQ*******************")
    mud.send_message(id, "***************************************")
    if str(players[id]["head"]) != "Empty":
        mud.send_message(id, "***Head: {}".format(str(Items.allitems[str(players[id]["head"])].name))) ##
    else:
        mud.send_message(id, "***Head: {}".format(players[id]["head"])) ##
    if str(players[id]["body"]) != "Empty":
        mud.send_message(id, "***Body: {}".format(str(Items.allitems[str(players[id]["body"])].name))) ##
    else:
        mud.send_message(id, "***Body: {}".format(players[id]["body"])) ##
    if str(players[id]["hands"]) != "Empty":
        mud.send_message(id, "**Hands: {}".format(str(Items.allitems[str(players[id]["hands"])].name))) ##
    else:
        mud.send_message(id, "**Hands: {}".format(players[id]["hands"])) ##
    if str(players[id]["legs"]) != "Empty":
        mud.send_message(id, "***Legs: {}".format(str(Items.allitems[str(players[id]["legs"])].name))) ##
    else:
        mud.send_message(id, "***Legs: {}".format(players[id]["legs"])) ##
    if str(players[id]["feet"]) != "Empty":
        mud.send_message(id, "***Feet: {}".format(str(Items.allitems[str(players[id]["feet"])].name))) ##
    else:
        mud.send_message(id, "***Feet: {}".format(players[id]["feet"])) ##
    mud.send_message(id, "***************************************")
    mud.send_message(id, "***************************************")
    if str(players[id]["weapon"]) != "Empty":
        mud.send_message(id, "***Weapon: {}".format(str(Items.allitems[str(players[id]["weapon"])].name))) ##
    else:
        mud.send_message(id, "***Weapon: {}".format(players[id]["weapon"])) ##
    if str(players[id]["offhand"]) != "Empty":
        mud.send_message(id, "**Offhand: {}".format(str(Items.allitems[str(players[id]["offhand"])].name))) ##
    else:
        mud.send_message(id, "**Offhand: {}".format(players[id]["offhand"])) ##
    mud.send_message(id, "***************************************")
    mud.send_message(id, "**************ACCESSORIES**************")
    if str(players[id]["ear"]) != "Empty":
        mud.send_message(id, "**Earrings: {}".format(str(Items.allitems[str(players[id]["ear"])].name))) ##
    else:
        mud.send_message(id, "**Earrings: {}".format(players[id]["ear"])) ##
    mud.send_message(id, "***************************************")
    if str(players[id]["neck"]) != "Empty":
        mud.send_message(id, "******Neck: {}".format(str(Items.allitems[str(players[id]["neck"])].name))) ##
    else:
        mud.send_message(id, "******Neck: {}".format(players[id]["neck"])) ##
    if str(players[id]["waist"]) != "Empty":
        mud.send_message(id, "*****Waist: {}".format(str(Items.allitems[str(players[id]["waist"])].name))) ##
    else:
        mud.send_message(id, "*****Waist: {}".format(players[id]["waist"])) ##
    if str(players[id]["ringl"]) != "Empty":
        mud.send_message(id, "*****Ringl: {}".format(str(Items.allitems[str(players[id]["ringl"])].name))) ##
    else:
        mud.send_message(id, "****Ringl: {}".format(players[id]["ringl"])) ##
    if str(players[id]["ringr"]) != "Empty":
        mud.send_message(id, "*****Ringr: {}".format(str(Items.allitems[str(players[id]["ringr"])].name))) ##
    else:
        mud.send_message(id, "*****Ringr: {}".format(players[id]["ringr"])) ##
    if str(players[id]["back"]) != "Empty":
        mud.send_message(id, "******Back: {}".format(str(Items.allitems[str(players[id]["back"])].name))) ##
    else:
        mud.send_message(id, "******Back: {}".format(players[id]["back"])) ##
    mud.send_message(id, "***************************************")
    if str(players[id]["bag"]) != "Empty":
        mud.send_message(id, "**BAG EQUIPPED:{}".format(str(Items.allitems[players[id]["bag"]].name))) ##
    else:
        mud.send_message(id, "***BACKPACK EQUIPPED: {}".format(players[id]["bag"])) ##
    mud.send_message(id, "***************************************")

def EquipCommand():
    iequipped = 0
    item = ItemsCheckRoom(players[id]["name"])
    for i in item:
        if i == Items.allitems[i].iid and params.lower() == Items.allitems[i].name and iequipped == 0:
            for x in players[id]["inventoryslot"]:
                for s in [players[id]["inventoryslot"][x]]: ## now we should only get only one item coming throug
                        if s == Items.allitems[i].iid and iequipped == 0 and params.lower() == Items.allitems[i].name: ## double check it
                            if Items.allitems[i].eqtype == "not":
                                mud.send_message(id, "That's not equipment... wtf are you thinking.")
                                iequipped = 1
                            if Items.allitems[i].eqtype != "not":
                            ### we need to check if eq slot is full otherwise it over writes it (player loses eq item)
                                if players[id][str(Items.allitems[i].eqtype)] == "Empty":
                                    mud.send_message(id, "You equipped up the "+str(Items.allitems[i].name))
                                    players[id][str(Items.allitems[i].eqtype)] = Items.allitems[i].iid
                                    players[id]["inventoryslot"][x] = "Empty"
                                    players[id][str(Items.allitems[i].eqstata)] = int(players[id][str(Items.allitems[i].eqstata)]) + int(Items.allitems[i].eqsvala)
                                    players[id][str(Items.allitems[i].eqstatb)] = int(players[id][str(Items.allitems[i].eqstatb)]) + int(Items.allitems[i].eqsvalb)
                                    iequipped = 1
                                elif iequipped == 0: ## this needs to be on this level to work
                                    mud.send_message(id, "You have equipment in that slot.")
                                    iequipped = 1
                                    mud.send_message(id, "you need to unequip "+str(Items.allitems[i].eqtype)+" to equip "+params.lower())
    if iequipped == 0 and params.lower() != Items.allitems[i].name:
        mud.send_message(id, "what are you trying to equip you fool!!")

def UnequipCommand():
    print("started unequip")
    useableslots = ["head", "body", "hands", "legs", "feet", "weapon", "offhand", "ear", "neck", "waist", "ringl", "ringr", "back", "bag"]
    iequipped = 1
    emptyslots = 8
    for d in useableslots:
        for i in [players[id][d]]:
            if d == params.lower() and iequipped == 1 and i != "Empty":
                for y in players[id]["inventoryslot"]:#####
                    for s in [players[id]["inventoryslot"][y]]:
                            if s == "Empty" and iequipped == 1:
                                players[id]["inventoryslot"][y] = players[id][d]
                                players[id][d] = "Empty"
                                iequipped = 0
                                mud.send_message(id, "I just pulled out!")
                                players[id][str(Items.allitems[i].eqstata)] = int(players[id][str(Items.allitems[i].eqstata)]) - int(Items.allitems[i].eqsvala)
                                players[id][str(Items.allitems[i].eqstatb)] = int(players[id][str(Items.allitems[i].eqstatb)]) - int(Items.allitems[i].eqsvalb)
                            else:
                                emptyslots -= 1
                                if emptyslots == 0:
                                    mud.send_message(id, "Nono emptys")####
            elif d != params.lower() and iequipped == 1 and i != "Empty":
                print(i)
                mud.send_message(id, "Nothing like that to unequip jackass.")
            elif d == params.lower() and iequipped == 1 and i == "Empty":
                mud.send_message(id, "you have nothing to unequip, Lost your meds?")


def SayCommand():
    # go through every player in the game
    for pid, pl in players.items():
        # if they're in the same room as the player
        if players[pid]["room"] == players[id]["room"]:
            # send them a message telling them what the player said
            mud.send_message(pid, "{} says: {}".format(players[id]["name"], params))

def LoginCommand():

    AssignNewPlayersIDs()
    if login[id]["name"] is None:
        mud.send_message(id, "Please enter your character name:")
        login[id]["process"] = "name"
    if login[id]["password"] is None:
        if login[id]["name"] != None:
            mud.send_message(id, "Please enter your password:")
            login[id]["process"] = "password"
    if login[id]["password"] != None:
        if login[id]["name"] != None:
            # check the database
            userlist = database.get_name(userdata, login[id]["name"])
            print("checking database for")
            print(login[id]["name"])
            if not userlist: # if cant find a user save list will come back blank
                mud.send_message(id, "Bad username.")
                Login()
                    # i have the ability to type reset now
                    # which means i built in a work around.
                    # for the issue.  however its easier to
                    # just have it run it.
                login[id]["process"] = None
                login[id]["name"] = None
                login[id]["password"] = None
            for check in userlist:
                if check[0] == login[id]["name"]:
                    if check[2] == login[id]["password"]:
                        players[id]["name"]        = check[0]
                        players[id]["room"]        = check[1]
                        players[id]["password"]    = check[2]
                        players[id]["email"]       = check[3]
                        players[id]["user"]        = check[4]
                        players[id]["race"]        = check[5]
                        players[id]["job"]         = check[6]
                        players[id]["coin"]        = check[7]
                        players[id]["ujob"]        = json.loads(check[8])
                        players[id]["exp"]         = check[9]
                        players[id]["ujoblevel"]   = json.loads(check[10])
                        players[id]["status"]      = check[11]
                      # populate players with race and class info
                        ChangeJob(players[id]["race"], players[id]["job"])
                        players[id]["level"] = 0
                        players[id]["maxhp"] = players[id]["maxhp"]+((players[id]["maxhp"]*.5)*players[id]["level"])
                        players[id]["maxmp"] = players[id]["maxmp"]+((players[id]["maxmp"]*.5)*players[id]["level"])
                        players[id]["hp"] = players[id]["maxhp"]
                        players[id]["mp"] = players[id]["maxmp"]
                        players[id]["pvp"] = "no"
                        players[id]["statustimer"] = 0
                        players[id]["fightstarted"] = 0
                        players[id]["timer"] = 0
                        players[id]["fighttimer"] = 10
                        players[id]["target"] = ''
                        players[id]["outcome"] = ''
                        players[id]["firstround"] = ''
                        players[id]["goesfirst"] = ''
                        players[id]["monster"] = ''
                        players[id]["tp"] = 0
                        players[id]["level"] = 0
                        players[id]["next"] = 3000*players[id]["level"]
                        if players[id]["next"] == 0:
                            players[id]["next"] = 3000
                        mud.send_message(id, "Successfully loaded: {}.\n".format(players[id]["name"]))
                        # print serverside a player logged in
                        print("New login")
                        print(players[id]["name"])
                        mud.send_message(id, motd.read())
                        mud.send_message(id, "You are being pulled through a dimensional gateway.")
                        mud.send_message(id, "Welcome back to NixMud, {}.".format(players[id]["name"]))
                        #mud.send_message(id, "Have a 'look' around...")
                        mud.send_message(id, "A lot changes here and interdimensional travel")
                        mud.send_message(id, "is always a pain in the ass.")
                        LookCommand()
                        ###   This makes your unique iid work on login
                        ###
                        ###   WHAT THE ACTUAL FUCK!!!??? I KNOW IT WORKS BUT WTF
                        ### if you fork our code never change this
                        ###  you will never recover (6:44AM Dec 29 2018)
                        ###      ........    seriously   ....  dont do it
                        ###
                        invlist = invendb.get_name(invdata, login[id]["name"])
                        slotlist = []
                        invitems = 8
                        equiplist = []
                        if invlist:
                            for checkinv in invlist:
                                for item in checkinv:
                                    if item != players[id]["name"] and item == "Empty":
                                        invitems -= 1
                                    if item != players[id]["name"] and item != "Empty":
                                        invitems -= 1
                                        orig = item[:4]
                                        newiid = str(orig)+str(random.randint(100,10000000000))
                                        while newiid in allitemslist:
                                            newiid = str(orig)+str(random.randint(100,10000000000))
                                        Items(newiid ,Items.allitems[orig].name, Items.allitems[orig].desc, players[id]["name"], Items.allitems[orig].type, Items.allitems[orig].eqtype, Items.allitems[orig].invdesc, Items.allitems[orig].bp, Items.allitems[orig].bpsize, Items.allitems[orig].eqstata, Items.allitems[orig].eqstatb, Items.allitems[orig].eqsvala, Items.allitems[orig].eqsvalb, Items.allitems[orig].sellval)
                                        allitemslist.append(Items.allitems[str(newiid)].iid)
                                        if invitems >0:
                                            slotlist.append(Items.allitems[str(newiid)].iid)
                                        else:
                                            equiplist.append(Items.allitems[str(newiid)].iid)
                        slotsfilled = int(0)-int(len(slotlist))
                        totalslots = int(8)+int(slotsfilled)
                        fillslots = 1
                        while fillslots == 1:
                            iteminlist = str(int(slotsfilled)+int(len(slotlist))+int(1))
                            if len(slotlist) != int(iteminlist)-int(1):
                                print("yay i filled slot"+iteminlist+" your majesty")
                                players[id]["inventoryslot"]["slot"+iteminlist] = slotlist[int(int(iteminlist)-int(1))]
                            if len(slotlist) == int(iteminlist)-int(1):
                                while totalslots != 0:
                                    players[id]["inventoryslot"]["slot"+iteminlist  ] = "Empty"
                                    totalslots -= 1
                            if slotsfilled == 0:
                                fillslots = 0
                            slotsfilled += 1
                        players[id]["inventoryused"] = len(slotlist)
                        for equipitem in equiplist:
                            players[id][str(Items.allitems[str(equipitem)].eqtype)] = equipitem
                        login[id]["process"] = "done"
                if check[0] != login[id]["name"]:
                    login[id]["name"] = None
                    login[id]["password"] = None
                    login[id]["process"] = None
                if check[2] != login[id]["password"]:
                    mud.send_message(id, "Bad password.")
                    Login()
                    login[id]["name"] = None
                    login[id]["password"] = None
                    login[id]["process"] = None
                    ### end of dont touch this section
def SetjobCommand():
#prints available jobs
    #change to ujobs
    jobpick = 0
    job = params
    ulock = "X"
    if job in players[id]["ujob"]:
        if ulock in players[id]["ujob"][job]:
            if ulock == "X":
                players[id]["ujoblevel"][players[id]["job"]] = players[id]["level"]
                players[id]["job"] = params
                level = players[id]["ujoblevel"][params]
                print(players[id]["ujoblevel"][players[id]["job"]])
                ChangeJob(players[id]["race"], players[id]["job"])
                players[id]["exp"] = 0
                players[id]["level"] = players[id]["ujoblevel"][players[id]["job"]]
                players[id]["next"] =  players[id]["level"]+1 * 3000
                players[id]["maxhp"] = players[id]["maxhp"]+((players[id]["maxhp"]*.5)*players[id]["level"])
                players[id]["maxmp"] = players[id]["maxmp"]+((players[id]["maxmp"]*.5)*players[id]["level"])
                if players[id]["hp"] > players[id]["maxhp"]:
                    players[id]["hp"] = players[id]["maxhp"]
                if players[id]["mp"] > players[id]["maxmp"]:
                    players[id]["mp"] = players[id]["maxmp"]
                mud.send_message(id, "Job Changed to {}".format(params))
                jobpick = 1
        else:
            mud.send_message(id, "Not an unlocked job")
            mud.send_message(id, "Your unlocked jobs are marked with an X in 'sheet'.")
            jobpick = 1
    elif job not in players[id]["ujob"]:
        mud.send_message(id, "Not a valid job...")
        jobpick = 1
    if jobpick == 0:
        mud.send_message(id, "What ya doin... just sayin hi?")

def StartDoorTimers():
    for door in doorslist:
        if Doors.doors[door].dtimer <= Doors.doors[door].gotopened:
            if Doors.doors[door].status == "open":
                Doors.doors[door].status = "closed"
                for pid, pl in players.items():
                    if players[pid]["room"] == Doors.doors[door].map:
                        mud.send_message(pid, "A clown pokes his head into the room , then slams the door")
        Doors.doors[door].gotopened += 1

def NewjobCommand():
    if playerprocess[id]["selection"] == None:
        for job in players[id]["ujob"]:
            for ulock in players[id]["ujob"][job]:
                if ulock == "X":
                    mud.send_message(id, "{}: {}".format(fun["corevalues"]["jobs"][job]["name"],fun["corevalues"]["jobs"][job]["description"]))
                    playerprocess[id]["selection"] = "job"
                    # moves to player process function
                    playerprocess[id]["process"] = "pickjob"
    if playerprocess[id]["selection"] == "job":
        mud.send_message(id, "What job you gonna go with?")

def NewCommand():
    #   The 'new' command gets input for a new player from the user
    # without getting all lost n broken amidst updates of server.
    # After it has collected all the data, it stores the setup[id]
    # as a new player in players[id].
    if setups[id]["name"] is None:
    # Prompt for a Name and set the new player task
        mud.send_message(id, "Enter a Name:")
        setups[id]["setup"] = "name"
    # Check to see if we set up an email yet
    if setups[id]["email"] is None:
    # Oh look we got a name from the user
        if setups[id]["name"] != None:
    # Make sure that silly player learns their name
            mud.send_message(id, "Your Name is: {}".format(setups[id]["name"]))
    # Ask for an email and set the new player task
            mud.send_message(id, "Enter an Email Address:")
            setups[id]["setup"] = "email"
            # Check to see if we have set a password
    if setups[id]["password"] is None:
    # We have input for an email.
        if setups[id]["email"] != None:
            mud.send_message(id, "Your Email is: {}".format(setups[id]["email"]))
    # Please set up a email change command
            mud.send_message(id, "WARNING!")
            mud.send_message(id, "If this email is not valid, you will not")
            mud.send_message(id, "recieve a new password should you lose")
            mud.send_message(id, "yours.")
    # Ask for a password
            mud.send_message(id, "Enter a password:")
            setups[id]["setup"] = "password"
    # Check if we have input for password confirmation
    if setups[id]["confirm"] is None:
    # We have input of password.  Store it and move on.
        if setups[id]["password"] != None:
            mud.send_message(id, "Confirm password:")
            setups[id]["setup"] = "confirm"
            # We have input for a confirmation of password
    if setups[id]["confirm"] != None:
    # Our paswords match so move on to race
        if setups[id]["password"] == setups[id]["confirm"]:
            setups[id]["match"] = "yes"
            setups[id]["setup"] = "pickrace"
        else:
    # Prompt for a new password and wait for input
            mud.send_message(id, "Passwords do not match.")
            mud.send_message(id, "Please enter a password:")
            setups[id]["password"] = None
            setups[id]["confirm"] = None
            setups[id]["setup"] = "password"
    # If there is no choice for class prompt for one
    if setups[id]["pickrace"] is None:
        if setups[id]["match"] == "yes":
            mud.send_message(id, "Here's a list of races:")
            for newraces in fun["corevalues"]["races"]:
                mud.send_message(id, newraces+" :  "+fun["corevalues"]["races"][newraces]["description"])
            mud.send_message(id, "pick a race:")
    if setups[id]["setup"] == "pickrace":
            # Now we have input for our choice of race
        if setups[id]["pickrace"] != None:
            # Check if input for race is valid
            if setups[id]["pickrace"] not in  fun["corevalues"]["races"]:
                mud.send_message(id, "Pick a valid race:")
                setups[id]["pickrace"] = None
            else:
                if setups[id]["job"] == None:
                    setups[id]["race"] = setups[id]["pickrace"]
                    setups[id]["setup"] = "pickjob"
                    NewjobCommand()

    # Now we have input for our choice of class
    if setups[id]["job"] != None:
    # Merge with players
        players[id]["name"] = setups[id]["name"]
        players[id]["email"] = setups[id]["email"]
        players[id]["password"] = setups[id]["password"]
        players[id]["race"] = setups[id]["race"]
        players[id]["job"] = setups[id]["job"]
        players[id]["user"] = "normal"
        players[id]["room"] = "Dungeon1"
        setups[id]["setup"] = None
        # populate players with race and class info
        #print serverside a new player was added
        print("New Player Added to server")
        print(players[id]["name"])
        ChangeJob(players[id]["race"], players[id]["job"])
        print("new player id for")
        print(players[id]["name"])
        players[id]["level"] = 0
        players[id]["maxhp"] = players[id]["maxhp"]+((players[id]["maxhp"]*.5)*players[id]["level"])
        players[id]["maxmp"] = players[id]["maxmp"]+((players[id]["maxmp"]*.5)*players[id]["level"])
        players[id]["hp"] = players[id]["maxhp"]
        players[id]["mp"] = players[id]["maxmp"]
        players[id]["fightstarted"] = 0
        players[id]["fighttimer"] = 10
        players[id]["timer"] = 0
        players[id]["status"] = 0
        players[id]["statustimer"] = 0
        players[id]["target"] = ''
        players[id]["outcome"] = ''
        players[id]["firstround"] = ''
        players[id]["goesfirst"] = ''
        players[id]["monster"] = ''
        players[id]["pvp"] = "no"
        players[id]["tp"] = 0
        players[id]["exp"] = 0
        players[id]["next"] = 3000
        players[id]["ujoblevel"] = {
                "warrior": 0,
                "whitemage": 0,
                "thief": 0,
                "indecisive": 0,
                "bard": 0,
                "blackmage": 0,
                "samurai": 0,
                "ninja": 0,
                "bartender": 0,
                "mog": 0,
                "linecook": 0,
                "inventor": 0,
                "landscaper": 0,
                "druid": 0,
                "witch": 0
                }
        players[id]["ujob"] = {
                "warrior": "X",
                "whitemage": "X",
                "thief": "X",
                "indecisive": " ",
                "bard": " ",
                "blackmage": "X",
                "samurai": " ",
                "ninja": " ",
                "bartender": " ",
                "mog": " ",
                "linecook": " ",
                "inventor": " ",
                "landscaper": " ",
                "druid": " ",
                "witch": " "
                }

        mud.send_message(id, "Thank you. Creation successful.")
         # can we send player straight to 'look'?
        mud.send_message(id, motd.read())
        mud.send_message(id, "Welcome to the Nixheads-Mud, {}.\n".format(players[id]["name"]))
        mud.send_message(id, "Type 'help' for a list of commands.")
        #mud.send_message(id, "Type 'look' to get your bearings in this new world")
        LookCommand()

def KickCommand():
    #### test command
    items = ItemsCheckRoom(players[id]["room"])
    creatures = CreatureCheckRoom(players[id]["room"])
    for i in items:
        if params.lower() == Items.allitems[i].name:
            mud.send_message(id, "you kicked a "+Items.allitems[i].name+"   :  "+Items.allitems[i].iid)
        else:
            for c in creatures:
                if params.lower() == Creatures.creatures[c].name:
                    mud.send_message(id, "you kicked a "+Creatures.creatures[c].name+"  :  "+Creatures.creatures[c].cid)

def OpenCommand():
    ex = params.lower()
    rm = rooms[players[id]["room"]]
    opened = 0
    doors = DoorsCheckRoom(players[id]["room"])
    block = ''
    blockx = ""
    for ob in rm["exits"]:
        if ob == "":
            for thedoor in doors:
                block = thedoor
                if Doors.doors[block].status == "closed":
                    if ex in Doors.doors[block].exits or ex == Doors.doors[block].name:
                        if Doors.doors[block].elock == "yes":
                            mud.send_message(id, "Locked doors don't open... they need keys.")
                        if Doors.doors[block].elock == "no":
                            Doors.doors[block].status = "open"
                            mud.send_message(id, "You opened the door... congrats.")
                            Doors.doors[block].gotopened = 0
                            for pid, pl in players.items():
                                if players[pid]["room"] == players[id]["room"]:
                                    mud.send_message(pid, "A door was opened.")
                                    opened = 1
    if opened == 0:
        mud.send_message(id, "Exactly what are you trying to open?....")

def CloseCommand():
    ex = params.lower()
    rm = rooms[players[id]["room"]]
    closed = 0
    doors = DoorsCheckRoom(players[id]["room"])
    block = ''
    blockx = ""
    for ob in rm["exits"]:
        if ob == "":
            for thedoor in doors:
                block = thedoor
                if Doors.doors[block].status == "open":
                    if ex in Doors.doors[block].exits or ex == Doors.doors[block].name:
                        Doors.doors[block].status = "closed"
                        mud.send_message(id, "You closed the door... congrats.")
                        for pid, pl in players.items():
                            if players[id]["room"] == players[pid]["room"]:
                                mud.send_message(pid, "A door was closed.")
                                closed = 1
    if closed == 0:
        mud.send_message(id, "Exactly what are you trying to close?....")



def GoCommand():

    # store the player's current room
    ex = params.lower()
    rm = rooms[players[id]["room"]]
    #store object Status
    doors = DoorsCheckRoom(players[id]["room"])
    block = ''
    blockx = ""
    for ob in rm["exits"]: # door43536457474
        if ob == "":
            for thedoor in doors:
                block = thedoor
                #block = rm["exits"][""] ## block = Doors.doors[].status
            if Doors.doors[block].status == "open": # Doors.doors.
                blockx = Doors.doors[block].exits
            if ex == Doors.doors[block].name:
                mud.send_message(id, "Idiot... you ran into a {}?".format(Doors.doors[block].name))
                playerprocess[id]["process"] = "ding"
                players[id]["hp"] -= 3
            # if the specified exit is found in the room's exits list
            if ex in Doors.doors[block].exits:
                playerprocess[id]["process"] = "ding"
                if Doors.doors[block].status == "closed":
                    mud.send_message(id, "{} is blocking your path.".format(Doors.doors[block].name))
                if Doors.doors[block].status == "open":
                # go through all the players in the game
                    for pid, pl in players.items():
                    # if player is in the same room and isn't the player
                    # sending the command
                        if players[pid]["room"] == players[id]["room"] and pid != id:
                         # send them a message telling them that the player
                         # left the room
                            mud.send_message(pid, "{} left via the {}.".format(players[id]["name"], Doors.doors[block].name))
                                    # update the player's current room to the one the exit leads to
                    players[id]["room"] = Doors.doors[block].mapto
                                    # possible place for description after moving
                    LookCommand()
                            # go through all the players in the game
                    for pid, pl in players.items():
                            # if player is in the same (new) room and isn't the player sending the command
                        if players[pid]["room"] == players[id]["room"] and pid != id:
                            # send them a message telling them that the player entered the room
                            mud.send_message(pid,"{} arrived via the {}.".format(players[id]["name"], Doors.doors[block].name))
    if ex != "":
        if ex in rm["exits"]:
        # go through all the players in the game
            for pid, pl in players.items():
        # if player is in the same room and isn't the player
                if players[pid]["room"] == players[id]["room"] and pid != id:
               # send them a message telling them that the player
               # left the room
                    mud.send_message(pid, "{} left via the {}.".format(players[id]["name"], ex))
                # update the player's current room to the one the exit leads to
            players[id]["room"] = rm["exits"][ex]
                # possible place for description after moving
            LookCommand()
        # go through all the players in the game
            for pid, pl in players.items():
        # if player is in the same (new) room and isn't the player sending the command
                if players[pid]["room"] == players[id]["room"] and pid != id:
        # send them a message telling them that the player entered the room
                    mud.send_message(pid,"{} arrived via the {}.".format(players[id]["name"], ex))
        else:
            # send back an 'unknown exit' message
            if playerprocess[id]["process"] != "ding":
                mud.send_message(id, "Unknown exit '{}'".format(ex))
                playerprocess[id] == None
    else:
            mud.send_message(id, "Unknown exit '{}'".format(ex))

def LookCommand():
    # send the player back the description of their current room
    rm = rooms[players[id]["room"]]
    mud.send_message(id, "*"*62)
    mud.send_message(id, rm["name"])
    mud.send_message(id, "*"*62)
    mud.send_message(id, rm["description"])
    mud.send_message(id, "*"*62)
    mud.send_message(id, "**** HP: {} **** MP: {} **** NEXT: {} **** PVP: {} ****".format(players[id]["hp"],players[id]["mp"],players[id]["next"]-players[id]["exp"],players[id]["pvp"]))
    mud.send_message(id, "*"*62)
## add bit to append exits if door opens
## the exit should have 2 values not just
## an exit.  if closed so retrun back ""
## if open "w" or "e" "or w/e"
## go command must be adjusted to not allow blanks
## as parameters.
    doors = DoorsCheckRoom(players[id]["room"])
    blockx = ""
    for ex in rm["exits"]:
        if ex == "":
            for thedoor in doors:
                block = thedoor
                print("block")
                if Doors.doors[block].status == "open":
                    blockx = Doors.doors[block].exits
                if Doors.doors[block].status == "closed":
                    blockx = Doors.doors[block].name
    mud.send_message(id, "Exits are: {} {}".format(" ".join(rm["exits"]),"".join(blockx)))
    print(blockx)
    mud.send_message(id, "*"*62)
    # list of players in room
    playershere = []
    # go through every player in the game
    for pid, pl in players.items():
    # if they're in the same room as the player
        if players[pid]["room"] == players[id]["room"]:
    # ... and they have a name to be shown
            if players[pid]["name"] is not None:
    # add their name to the list
                playershere.append(players[pid]["name"])
            ### send player a message containing the list of players in the room
    mud.send_message(id, "Players here: {}".format(", ".join(playershere)))
            # send player a message containing the list of creatures in the room
    for cre in CreatureCheckRoom(players[id]["room"]):
        mud.send_message(id, Creatures.creatures[cre].desc)
            # send player a message containing items on the floor
    for i in ItemsCheckRoom(players[id]["room"]):
        mud.send_message(id, Items.allitems[i].desc)

def CreatureCheckRoom(pr):
    creatures = []
    for items in creaturelist:
       if items == Creatures.creatures[items].cid:
           if pr == Creatures.creatures[items].room:
               creatures.append(items)
    return creatures

def GetDammage(attacker, prey):
    if attacker == players[id]["name"]:
        defence = int(players[id]["dex"]) + int(players[id]["vit"])
        attack = int(players[id]["dex"]) + int(players[id]["str"])
        miss = str(random.randint(int(players[id]["level"]), int(int(players[id]["level"])+attack)))
        damage = int(players[id]["str"])/2-int(Creatures.creatures[prey].cdef)/4
        if damage <= 0:
            return 0
        else:
            if int(miss) >= int(Creatures.creatures[prey].cdef):
                return damage
            else:
                return "miss"
    else:
        defence = int(Creatures.creatures[attacker].cdef)
        attack = int(Creatures.creatures[attacker].cstr)
        miss = str(random.randint(int(Creatures.creatures[attacker].clvl), int(int(Creatures.creatures[attacker].clvl)+attack)*2))
        damage = int(attack)/2 - int(defence)/4
        playerdef = int(players[id]["dex"]) + int(players[id]["vit"])
        if damage <= 0:
            return 0
        else:
            if int(miss) >= int(playerdef)-attack:
                return damage
            else:
                return "miss"
def RestCommand():
    players[id]["hp"] = players[id]["maxhp"]
    players[id]["mp"] = players[id]["maxmp"]
def IsDead(character):
    if character == players[id]["name"]:
        if players[id]["hp"] <= 0:
            return 1
    else:
        if int(Creatures.creatures[character].life) <= 0:
            return 1

def CheckSkill(sk):
    skillinfo=[]
    for skill in fun["corevalues"]["skills"]:
        if skill == sk:
            for stat in fun["corevalues"]["skills"][skill]:
                statie = str(json.dumps(fun["corevalues"]["skills"][skill][stat])).replace('"', '')
                skillinfo.append(statie)
    return skillinfo

def SkillCommand():
    text = str(params).split(' ')
    skkll = CheckSkill(text[0])
    didskill = 0
    if not skkll:
        mud.send_message(id, "Use wtf? Huh?")
        didskill = 1
    if skkll:
        if didskill == 0:
            if players[id]["job"] != skkll[4]:
                mud.send_message(id, "Oh you think you suddenly can act like a {}?".format(skkll[4]))
                didskill = 1
            elif players[id]["tp"] < int(skkll[3]):
                mud.send_message(id, "Things cost TP ya know... TP you dont have.")
                didskill = 1
            elif players[id]["level"] < int(skkll[0]):
                mud.send_message(id, "You just dont have what it takes to use this... git gud!!")
            elif players[id]["level"] >= int(skkll[0]):
                if skkll[2] == "quiet":
                    if players[id]["name"] != text[1]:
                        mud.send_message(id, "You can't just make someone else sneaky...")
                        mud.send_message(id, "Nice try though.")
                        didskill = 1
                    else:
                        players[id]["status"] = "quiet"
                        players[id]["statustimer"] = players[id]["level"] * 1 + 1
                        mud.send_message(id, "You are sneakin around.  ya got {} Minute(s)".format(players[id]["statustimer"]))
                        didskill = 1
    if didskill == 0:
        mud.send_message(id, "Just spamming skills for giggles n tits?")


def CheckCast(sc):
    spellinfo=[]
    for spell in fun["corevalues"]["spells"]:
        if spell == sc:
            for stat in fun["corevalues"]["spells"][spell]:
                statie = str(json.dumps(fun["corevalues"]["spells"][spell][stat])).replace('"', '')
                spellinfo.append(statie)
    return spellinfo


def CastCommand():
    text = str(params).split(' ')
    cast = CheckCast(text[0])
    didcast = 0
    if not cast:
        mud.send_message(id, "Cast wtf now?")
        didcast =1
    if cast:
        if didcast == 0:
            if players[id]["job"] != cast[4]:
                mud.send_message(id, "Oh you think you're a {} do you?".format(cast[4]))
                didcast = 1
            elif players[id]["mp"] < int(cast[3]):
                mud.send_message(id, "You are not made of mp ya know...")
                didcast = 1
            elif players[id]["level"] < int(cast[0]):
                mud.send_message(id, "Only the big kids get this spell...")
                didcast =1
            elif players[id]["level"] >= int(cast[0]):
                if cast[2] == "damage":
                    creatures = CreatureCheckRoom(players[id]["room"])
                    for creature in creatures:
                        if Creatures.creatures[creature].name == text[1]:
                            mud.send_message(id, "You cast {} on {}".format(text[0],text[1]))
                            players[id]["mp"] -= int(cast[3])
                            dmgval = random.randint(int(cast[1])-3, int(cast[1])+3)
                            mud.send_message(id, "You did: {} damage!".format(dmgval))
                            players[id]["monster"] = creature
                            Creatures.creatures[creature].life = int(Creatures.creatures[creature].life) - int(dmgval)
                            FightCommand()
                            didcast = 1
                            break

                if cast[2] == "heal":
                    for pid, pl in players.items():
                        if players[pid]["name"] == text[1]:
                            if players[pid]["room"] == players[id]["room"]:
                                mud.send_message(id, "You cast: {} on {}".format(text[0],text[1]))
                                players[id]["mp"] -= int(cast[3])
                                healval = random.randint(int(cast[1])-3, int(cast[1])+3)
                                mud.send_message(id, "Healed for: {}".format(healval))
                                if players[pid]["name"] != players[id]["name"]:
                                    mud.send_message(pid, "{} healed you for: {}.".format(players[id]["name"],healval))
                                players[pid]["hp"] = players[pid]["hp"]+healval
                                if players[pid]["hp"] > players[pid]["maxhp"]:
                                    players[pid]["hp"] = players[pid]["maxhp"]
                                didcast = 1
    if didcast == 0:
        mud.send_message(id, "Did you put the right name in or just casting for lulz?")

def StartFightTimer():
    if players[id]["fighttimer"] <= players[id]["timer"]:
        players[id]["timer"] = 0
        FightCommand()
    if players[id]["fighttimer"] >= players[id]["timer"]:
        players[id]["timer"] += 1


movepool = []
def FightCommand():
    if players[id]["fightstarted"] == 0:
        creatures = CreatureCheckRoom(players[id]["room"])
        for creature in creatures:
            if Creatures.creatures[creature].name == str(params.lower()):
                players[id]["monster"] = creature
                break
        if players[id]["monster"] == '':
            mud.send_message(id, "there is no creature here called "+params.lower())
        else:
            mud.send_message(id, "You try starting a fight with "+params.lower())
            if int(Creatures.creatures[players[id]["monster"]].clvl) >= int(players[id]["level"])+15:
                mud.send_message(id, Creatures.creatures[players[id]["monster"]].name+" flicks you away like a bug, you sore through the air and land as a bloody mess on the floor")
                players[id]["hp"] = players[id]["hp"] - players[id]["hp"]
            else:
                if int(Creatures.creatures[players[id]["monster"]].cdef) >= int(players[id]["dex"]):
                    players[id]["goesfirst"] = players[id]["monster"]
                if int(Creatures.creatures[players[id]["monster"]].cdef) < int(players[id]["dex"]):
                    players[id]["goesfirst"] = players[id]["name"]
                players[id]["fightstarted"] = 1
                players[id]["outcome"] = kung_fu_fighting(players[id]["monster"])
    if players[id]["fightstarted"] == 1:
        if players[id]["outcome"] == players[id]["name"]:
            players[id]["hp"] = 1
            mud.send_message(id, "you died")
            players[id]["exp"] = players[id]["exp"]-(players[id]["exp"] * .6)
            if players[id]["exp"] < 0:
                Leveldown()
                ## add here if drop all items
            players[id]["room"] = "TownCenter"
            players[id]["fightstarted"] = 0
            LookCommand()
            return
            ## Dead()
        elif players[id]["outcome"] == players[id]["monster"]:
            return
        elif players[id]["outcome"] == 0:
            players[id]["outcome"] = kung_fu_fighting(players[id]["monster"])


def kung_fu_fighting(monster):
    if monster != players[id]["target"] and players[id]["firstround"] == 1:
        mud.send_message(id, "you are now fighting "+Creatures.creatures[monster].name)
        players[id]["target"] = monster
        players[id]["firstround"] = 1
    else:
        players[id]["target"] = monster
    if players[id]["firstround"] == 1:
        movepool = []
        basemoveamount = 5 ## might add this to the creature so its a dynamic percentage
        count = 0
        if Creatures.creatures[monster].basemove != "no":
            while basemoveamount >= count:
                movepool.append(Creatures.creatures[monster].basemove)
                count += 1
        if Creatures.creatures[monster].csnm != "no":
            movepool.append(Creatures.creatures[monster].csnm)
        players[id]["firstround"] = 0
    if players[id]["goesfirst"] == monster:
        movetouse = movepool[int(str(random.randint(1, len(movepool))))]
        if movetouse == Creatures.creatures[monster].csnm:
            pass #CastCommand(monster, movetouse)
        else:
            dmg = GetDammage(monster, players[id]["name"])
            if dmg == 0:
                dmg = 1
                mud.send_message(id, str(Creatures.creatures[monster].name)+" is powerless against you, dealing "+str(dmg)+" damage")
            elif dmg == "miss":
                dmg = 0
                mud.send_message(id, str(Creatures.creatures[monster].name)+" has pathetic aim and misses you")
            else:
                mud.send_message(id, str(Creatures.creatures[monster].name)+" attacks you, dealing "+str(dmg)+" damage")
            players[id]["hp"] = int(players[id]["hp"]) - int(dmg)

        players[id]["goesfirst"] = ''
    else:
        dead = IsDead(players[id]["name"])
        if dead == 1:
            return players[id]["name"]
        dead = IsDead(monster)
        if dead == 1:
            return monster
        ####
        dmg = GetDammage(players[id]["name"], monster)
        if dmg == 0:
            dmg = 1
            mud.send_message(id, "You are powerless against "+str(Creatures.creatures[monster].name)+", dealing "+str(dmg)+" damage")
        elif dmg == "miss":
            dmg = 0
            mud.send_message(id, "You suck, you need to train more, you missed the "+str(Creatures.creatures[monster].name))
        else:
            mud.send_message(id, "You hit the "+str(monster)+", dealing "+str(dmg)+" damage")
            players[id]["exp"] += 3*int(Creatures.creatures[monster].life)
        Creatures.creatures[monster].life = int(Creatures.creatures[monster].life) - int(dmg)

        dmg = GetDammage(monster, players[id]["name"])
        if dmg == 0:
            dmg = 1
            mud.send_message(id, str(Creatures.creatures[monster].name)+" is powerless against you, dealing "+str(dmg)+" damage")
        elif dmg == "miss":
            dmg = 0
            mud.send_message(id, str(Creatures.creatures[monster].name)+" has pathetic aim and misses you")
        else:
            mud.send_message(id, str(Creatures.creatures[monster].name)+" attacks you, dealing "+str(dmg)+" damage")
        players[id]["hp"] = players[id]["hp"] - dmg
        mud.send_message(id, "**** HP: {} **** MP: {} **** NEXT: {} **** PVP: {} ****".format(players[id]["hp"],players[id]["mp"],players[id]["next"]-players[id]["exp"],players[id]["pvp"]))
        return 0

#cid name room desc clvl cstr
#cdmg cdef clfe life moves
#drops cspc csnm ctmr corp turn

def Levelup():
    players[id]["level"] = players[id]["level"] + 1
    players[id]["next"] =  players[id]["level"] * 3000
    players[id]["exp"] = 0
    players[id]["maxmp"] = players[id]["maxmp"]+((players[id]["maxmp"]*.5)*players[id]["level"])
    players[id]["maxhp"] = players[id]["maxhp"]+((players[id]["maxhp"]*.5)*players[id]["level"])
    players[id]["mp"] = players[id]["maxmp"]
    players[id]["hp"] = players[id]["maxhp"]
    mud.send_message(id, "You have leveled up!!!")
    mud.send_message(id, "You get some bonuses")

def Leveldown():
    players[id]["level"] = players[id]["level"] - 1
    if players[id]["level"] < 0:
        players[id]["level"] = 0
    players[id]["next"] = players[id]["level"] *3000
    if players[id]["next"] == 0:
        players[id]["next"] = 3000
    players[id]["maxhp"] = players[id]["maxhp"]+ ((players[id]["maxhp"]*.5)*players[id]["level"])
    players[id]["maxmp"] = players[id]["maxmp"]+ ((players[id]["maxmp"]*.5)*players[id]["level"])
    players[id]["hp"] = 1
    players[id]["mp"] = 0
    mud.send_message(id, "You leveled down...")
    mud.send_message(id, "You just got nerfed.  Not my problem.")

def CheckCommand():
    creatures = CreatureCheckRoom(players[id]["room"])
    for creature in creatures:
        if Creatures.creatures[creature].name == str(params.lower()):
            if int(Creatures.creatures[creature].clvl) >= int(players[id]["level"])+15:
                mud.send_message(id, "Do you want your grave dug now or later?")
                break
            if int(Creatures.creatures[creature].clvl) >= int(players[id]["level"])+7:
                mud.send_message(id, "You're gonna need a lot of help...")
                break
            if int(Creatures.creatures[creature].clvl) >= int(players[id]["level"])+4:
                mud.send_message(id, "This won't be easy...")
                break
            if int(Creatures.creatures[creature].clvl) >= int(players[id]["level"]):
                mud.send_message(id, "This could be doable...")
                break
            if int(Creatures.creatures[creature].clvl) >= int(players[id]["level"])-4:
                mud.send_message(id, "I'll be dissapointed if you die.")
                break
            if int(Creatures.creatures[creature].clvl) >= int(players[id]["level"])-10:
                mud.send_message(id, "It's just a baby... why would you kill this?")
                break
    else:
        mud.send_message(id, "Exactly what are you trying to check here?")
## get date
#timeatstart = datetime.datetime.now()
# main game loop. We loop forever (i.e. until the program is terminated)
while True:
    # pause for 1/5 of a second on each loop, so that we don't constantly
    # use 100% CPU time
    time.sleep(0.2)
    # 'update' must be called in the loop to keep the game running and give
    # us up-to-date information
    mud.update()

    ## check timers
#    currenttime = datetime.datetime.now()
#    uptime = currenttime - timeatstart
#    uptime = int(''.join(str(divmod(uptime.total_seconds(), 1)).replace('(', '').split('.')[:1]))
    #print(uptime)

    # go through any newly connected players
    for id in mud.get_new_players():
        AssignNewPlayersIDsP()
        AssignNewPlayersIDs()
        mud.send_message(id, logascii.read())
        Login()

    # go through any recently disconnected players
    for id in mud.get_disconnected_players():
        # if for any reason the player
        #isn't in the player map, skip
        #them and move on to the next one
        if id not in players:
            continue
        # go through all the players in the game
        for pid, pl in players.items():
            # send each player a message to tell
            # them about the diconnected player
            mud.send_message(pid, "{} quit the game".format(players[id]["name"]))
        # remove the player's entry in the player dictionary
        del(players[id])

    commandflag = 0
    try:
        if players[id]["fightstarted"] == 1:
            StartFightTimer()
            if players[id]["outcome"] == players[id]["monster"]:
                mud.send_message(id, "you killed "+Creatures.creatures[players[id]["monster"]].name)
                newcnid = str("corp")+str(random.randint(100,10000000000))
                monmon = Creatures.creatures[players[id]["monster"]].name
                Creatures.creatures[players[id]["monster"]].corp = "yes"
                mud.send_message(id, "The monster drops a: "+Creatures.creatures[players[id]["monster"]].drops)
                Creatures.creatures[players[id]["monster"]].desc = "The corpse of a "+Creatures.creatures[players[id]["monster"]].name+" is laying here"
                Creatures.creatures[players[id]["monster"]].moves = "no"
                players[id]["fightstarted"] = 0
                players[id]["outcome"] = ''
                players[id]["monster"] = ''
                players[id]["goesfirst"] = ''
                players[id]["target"] = ''
                players[id]["firstround"] = ''
                pass
    except:
        pass
    StartDoorTimers()
    # go through any new commands sent from players
    for id, command, params in mud.get_commands():
        if players[id]["exp"] >= players[id]["next"]:
            Levelup()

# if for any reason the player isn't in the player map, skip them and
# move on to the next one
# move the above comments down
# Job change command process
        if playerprocess[id]["process"] == "jobchange":
            command = "setjob"
            player[process][id]["selection"] = None
        if playerprocess[id]["process"] == "pickjob":
            commandflag = 1
            if command in fun["corevalues"]["jobs"]:
                if setups[id]["setup"] == "pickjob":
                    playerprocess[id]["process"] = None
                    setups[id]["job"] = command
                    setups[id]["setup"] = "merge"
                    playerprocess[id]["selection"] = None
                else:
                    players[id]["job"] = command
                    ChangeJob(players[id]["race"], players[id]["job"])
                    if players[id]["hp"] > players[id]["maxhp"]:
                        players[id]["hp"] = players[id]["maxhp"]
                    if players[id]["mp"] > players[id]["maxmp"]:
                        players[id]["mp"] = players[id]["maxmp"]
                    mud.send_message(id, "Job Changed to {}".format(command))
                    playerprocess[id]["selection"] = None
                    commandflag = 1
            else:
                mud.send_message(id, "Thats not a valid job.")
                commandflag = 1
                if setups[id]["job"] != None:
                        playerprocess[id]["selection"] = None
        playerprocess[id]["process"] = None

        # login command process
        if login[id]["process"] != None:
            if command == 'reset':
                login[id]["process"] = None
            if login[id]["process"] == "name":
                login[id]["name"] = command
                command = "login"
            if login[id]["process"] == "password":
                login[id]["password"] = command
                command = "login"
            if login[id]["process"] == "done":
                login[id]["process"] = None
            if login[id]["process"] == "reset":
                login[id]["process"] = None
                command = "reset"

        # new command process
        if setups[id]["setup"] != None:
            if setups[id]["setup"] == "name":
                setups[id]["name"] = command
                #checks for name in database
                userlist = database.get_name(userdata, setups[id]["name"])
                for user in userlist:
                    if setups[id]["name"] == user[0]:
                        mud.send_message(id, "That name is taken, Enter a new name:")
                        setups[id]["name"] = None
            if setups[id]["setup"] == "email":
                setups[id]["email"] = command
            if setups[id]["setup"] == "password":
                setups[id]["password"] = command
            if setups[id]["setup"] == "confirm":
                setups[id]["confirm"] = command
            if setups[id]["setup"] == "pickrace":
                setups[id]["pickrace"]  = command
            if setups[id]["setup"] == "pickjob":
                pickjob = command
                SetjobCommand()
                playerprocess[id]["process"] = "pickjob"
            if setups[id]["setup"] != "pickjob":
                command = "new"

        # does this work?
        if id not in players:
            continue
            # go through all the players in the game
            for pid, pl in players.items():
                # send each player a message to tell them about the new player
                mud.send_message(pid, "{} entered the game".format(players[id]["name"]))

        # Commands
        # add gm commands later please

        # login command
        # this function is faulty
        # so it is backed up
        # by the 'reset' command
        # better documentation
        # for this will come as
        # it becomes refined
        elif command == "login":
            LoginCommand()

        elif command == "rest":
            RestCommand()

        elif command == "new":
            NewCommand()
         # setjobs command
         # used to change jobs

        elif command == "setjob":
             SetjobCommand()

        # save command
        elif command == 'save':
            SaveCommand()

        # emergency reset
        # also logout command
        elif command == "reset":
            ResetCommand()

        # character sheet
        elif command == "sheet":
            SheetCommand()
        # help file command
        # rewrite all this

        elif command == "help":
            mud.send_message(id, helpo.read())
        elif command == "help2":
            mud.send_message(id, helpt.read())

        # 'system' command
        # Make GM command
        # outputs a message to all users in game
        # useful during server maintenace to warn players to save.
        elif command == "gm":
            mud.send_message(id, "Your user is set to GM mode")
            players[id]["user"] = "GM"

        elif command == "global":
            for pid, pl in players.items():
                mud.send_message(pid, "{}: Global Chat: {}".format(players[id]["name"], params))

        elif players[id]["user"] == "GM" and command == "system":
            for pid, pl in players.items():
                mud.send_message(pid, "SYSTEM MESSAGE!!: {}".format(params))

        elif command == "tell":
            online = "offline"
            for pid, pl in players.items():
                text = str(params).split(' ')
                if players[id]["name"] != text[0]:
                    if players[pid]["name"] == text[0]:
                        msgto = " ".join(str(x) for x in text[1:])
                        mud.send_message(pid, "{} whispers: {}".format(players[id]["name"],msgto))
                        online = "online"
                else:
                     online = "online"
                     mud.send_message(id, "you love to hear yourself talk huh.....")
            if online != "online":
                mud.send_message(id, "That character is not logged in at this time.")

        # 'say' command
        elif command == "say":
            SayCommand()

        # 'shutdown' command
        # shutdowns server
        # saves character data to database and prints
        # serverside for each character saved
        # make this a gm command later
        elif players[id]["user"] == "GM" and command == "shutdown":
            ShutdownCommand()

        elif command == "drop":
            DropCommand()

        elif command == "grab":
            GrabCommand()
        elif command == "give":
            GiveCommand()

        # 'look' command
        elif command == "look":
            LookCommand()

        elif command == "kick":
            KickCommand()

        elif command == "exam":
            ExamCommand()
        elif command == "check":
            CheckCommand()

        elif command == "fight":
            if players[id]["fightstarted"] != 1:
                FightCommand()
            else:
                mud.send_message(id, "You are already fighting...")

        elif command == "eq":
            EquipmentCommand()

        elif command == "cast":
            CastCommand()

        elif command == "skill":
            SkillCommand()

        elif command == "equip":
            EquipCommand()
        #elif command == "unequip":
         #   UnequipCommand()

        elif command == "uptime":
            mud.send_message(id, str(uptime))
        elif command == "open":
            OpenCommand()

        elif command == "close":
            CloseCommand()
        # 'go' command
        elif command == "go":
            GoCommand()

        elif command == "inv":
            InventoryCommand()
        #Random text entered
        #elif command == 'blank':
        #    continue
        # some other, unrecognised command
        elif commandflag == 0:
            #if command == '':
            mud.send_message(id, "This is not a valid command '{}', silly dumb dumb.".format(command))
