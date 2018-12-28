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

"""""""""""

# basic files to import
# including the json
# library

import time
import db as database
import json
import credb as creaturedb
# import the MUD server class

from mudserver import MudServer

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
        Creatures.creatures[name] = self

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

# import help files
# this will be implemented
# in the near future.
# currently still using
# 'help' command

with open("Help/help1.json") as helpfile:

    helpfiles = json.load(helpfile)

# import race files

with open("Races/races.json") as raceoptions:

    races = json.load(raceoptions)

# import jobs (currently classes)

with open("Classes/classes.json") as joboptions:

    startjobs = json.load(joboptions)

# stores the players in the game
# setups is the newly created characters during generation process
# players is the players found in game.  A player will not be seen
# by anyone while in the setups group.

class creatures(object):
    def init(self, name, room, desc):
        self.name = name
        self.room = room
        self.desc = desc

login = {}
setups = {}
players = {}

# start the server

mud = MudServer()

##connect to db for player saves
userdata = database.connect()
creaturedata = creaturedb.connect()

########### this grabs from the json for creatures
for cid in credb.keys():
    for stat in credb[cid]:
# pulls needed data as normal and removes any " " from results
        value = str(json.dumps(credb[cid][stat])).replace('"', '')
### quick ifs to check if values match what need and stores them to be imported after
        if stat == "name":
            name = value
        if stat == "room":
            room = value
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

############ loads every creature into class
    Creatures(cid, name, room, desc, clvl, cstr, cdmg, cdef, clfe, life, moves, drops, cspc, csnm, ctmr, corp)
          #### dumps to database

    # Dumps to database if creature is not already there
    result = creaturedb.cspawn(creaturedata, name)
    if not result:
        print("added "+name+" to db")
        creaturedb.cload(creaturedata, Creatures.creatures[cid].name, Creatures.creatures[cid].room, Creatures.creatures[cid].desc, Creatures.creatures[cid].clvl, Creatures.creatures[cid].cstr, Creatures.creatures[cid].cdmg, Creatures.creatures[cid].cdef, Creatures.creatures[cid].clfe, Creatures.creatures[cid].life, Creatures.creatures[cid].moves, Creatures.creatures[cid].drops, Creatures.creatures[cid].cspc, Creatures.creatures[cid].csnm, Creatures.creatures[cid].ctmr, Creatures.creatures[cid].corp)


# main game loop. We loop forever (i.e. until the program is terminated)

while True:

    # pause for 1/5 of a second on each loop, so that we don't constantly

    # use 100% CPU time

    time.sleep(0.2)

    # 'update' must be called in the loop to keep the game running and give

    # us up-to-date information

    mud.update()

    # go through any newly connected players

    for id in mud.get_new_players():

        # The attributes for login credentials
        # just a character name and password
        # and where it is in its process

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
                "pickclass": None,
                "user" : None,
                "email": None,
                "password": None,
                }

        players[id] = {

            "name": None,
            "email": None,
            "password": None,
            "level":None,
            "exp": None,
            "next": None,
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
            "pvp": None,
            "coin": 0,
            "waitingsave": None,


        }


        # send the new player a login screen
        # identical to the 'reset' command.

        mud.send_message(id, logascii.read())
        mud.send_message(id, "Are you a 'new' player or would you like to 'login'?")



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

            mud.send_message(pid, "{} quit the game".format(

                                                        players[id]["name"]))

        # remove the player's entry in the player dictionary

        del(players[id])

    # go through any new commands sent from players


    for id, command, params in mud.get_commands():

        # if for any reason the player isn't in the player map, skip them and
        # move on to the next one
        # move the above comments down

        # Check the login process
        # currently making use of 'reset'
        # command until a fix is made

        if login[id]["process"] != None:

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

        # Check the process of setting up new character

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
            if setups[id]["setup"] == "pickclass":
                setups[id]["pickclass"] = command
            if setups[id]["setup"] == "merge":
                mud.send_message(id, "success")

            command = "new"

        if id not in players:

            continue


            # go through all the players in the game

            for pid, pl in players.items():

                # send each player a message to tell them about the new player

                mud.send_message(pid, "{} entered the game".format(

                                                        players[id]["name"]))



        # commands section
        # soon to come
        # GM commands

        # login command
        # this function is faulty
        # so it is backed up
        # by the 'reset' command
        # better documentation
        # for this will come as
        # it becomes refined

        elif command == "login":

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
                        login[id]["process"] = "reset"

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

                                # populate players with race and class info

                                pr = players[id]["race"]
                                pj = players[id]["job"]
                                for stat in races[pr]:
                                    attribs = json.dumps(races[pr][stat])
                                    if stat != "description":
                                        for jobs in startjobs[pj]:
                                            if stat == jobs:
                                                value = json.dumps(startjobs[pj][stat])
                                                players[id][stat] = int(attribs) + int(value)
                                            else:
                                                players[id][stat] = int(attribs)

                                players[id]["maxhp"] = players[id]["hp"]
                                players[id]["maxmp"] = players[id]["mp"]
                                players[id]["pvp"] = "no"
                                players[id]["tp"] = 0
                                players[id]["exp"] = 0
                                players[id]["level"] = 0
                                players[id]["next"] = 3000
                                players[id]["ujob"] = {
                                                        "warrior",
                                                        "blackmage",
                                                        "whitemage",
                                                        "thief"
                                                     }
                                players[id]["waitingsave"] = 0


                                mud.send_message(id, "Successfully loaded: {}.\n".format(
                                                                                    players[id]["name"]))

                                # print serverside a player logged in
                                print("New login")
                                print(players[id]["name"])

                                # possible fix for the reset loop issue.
                                #login[id]["process"] is None

                                mud.send_message(id, motd.read())
                                mud.send_message(id, "You are being pulled through a dimensional gateway.")
                                mud.send_message(id, "Welcome back to NixMud, {}.".format(
                                                                                    players[id]["name"]))
                                mud.send_message(id, "Have a 'look' around...")
                                mud.send_message(id, "A lot changes here and interdimensional travel")
                                mud.send_message(id, "is always a pain in the ass.")

                                login[id]["process"] = "done"

                        if check[0] != login[id]["name"]:

                            mud.send_message(id, "Failed to find that character name.")

                            login[id]["name"] = None
                            login[id]["password"] = None
                            login[id]["process"] = None


                        if check[2] != login[id]["password"]:
                            mud.send_message(id, "Bad password.")
                            mud.send_message(id, "Are you a 'new' player or would you like to 'login'?")

                            login[id]["name"] = None
                            login[id]["password"] = None
                            login[id]["process"] = None



        elif command == "new":

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

                    mud.send_message(id, "Your Name is: {}".format(

                                                          setups[id]["name"]))

                    # Ask for an email and set the new player task

                    mud.send_message(id, "Enter an Email Address:")

                    setups[id]["setup"] = "email"

            # Check to see if we have set a password

            if setups[id]["password"] is None:

                # We have input for an email.

                if setups[id]["email"] != None:

                    mud.send_message(id, "Your Email is: {}".format(

                                                          setups[id]["email"]))

                    # Warn player

                    mud.send_message(id, "WARNING!")

                    mud.send_message(id, "If this email is not valid, you will not")

                    mud.send_message(id, "recieve a new password should you lose")

                    mud.send_message(id, "yours.")

                    # Ask for a password

                    mud.send_message(id, "Enter a password:")

                    setups[id]["setup"] = "password"

            # Check if we have input for password confirmation

            if setups[id]["confirm"] is None:

                # We have input of password.  Store it and move on
                # To confirm it.

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
                    mud.send_message(id, "elavari: {}".format("".join(races["elvari"]["description"])))
                    mud.send_message(id, "humani: {}".format("".join(races["humani"]["description"])))
                    mud.send_message(id, "dragani: {}".format("".join(races["dragani"]["description"])))
                    mud.send_message(id, "krei: {}".format("".join(races["krei"]["description"])))

                if setups[id]["setup"] == "pickrace":

                    mud.send_message(id, "Pick a race:")

            # Now we have input for our choice of race

            if setups[id]["pickrace"] != None:

                # Check if input for race is valid

                if setups[id]["pickrace"] not in races:

                    mud.send_message(id, "Not a valid race.\nPick a race:")

                    setups[id]["pickrace"] = None

                else:

                        # Insert race in setups[id]

                        setups[id]["race"] = setups[id]["pickrace"]

                        setups[id]["setup"] = "pickclass"


            # If there is no choice for class prompt for one

            if setups[id]["pickclass"] is None:

                if setups[id]["setup"] == "pickclass":

                    mud.send_message(id, "Jobs you would hope to see:")

            if setups[id]["setup"] == "pickclass":

                mud.send_message(id, "warrior: {}".format("".join(startjobs["warrior"]["description"])))
                mud.send_message(id, "blackmage: {}".format("".join(startjobs["blackmage"]["description"])))
                mud.send_message(id, "whitemage: {}".format("".join(startjobs["whitemage"]["description"])))
                mud.send_message(id, "thief: {}".format("".join(startjobs["thief"]["description"])))
                mud.send_message(id, "What job you gonna start with?")

            # Now we have input for our choice of class

            if setups[id]["pickclass"] != None:

                # check if input for class is valid

                if setups[id]["pickclass"] not in startjobs:

                    mud.send_message(id, "Not a valid class.\nPick a class:")

                    setups[id]["pickclass"] = None

                else:

                        # Insert class in setups[id]

                        setups[id]["job"] = setups[id]["pickclass"]

                        mud.send_message(id, "got it.")

                        setups[id]["setup"] = "merge"

                # check if ready to merge with players

                if setups[id]["setup"] == "merge":

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

                    pr = players[id]["race"]
                    pj = players[id]["job"]
                    for stat in races[pr]:
                        attribs = json.dumps(races[pr][stat])
                        if stat != "description":
                            for jobs in startjobs[pj]:
                                if stat == jobs:
                                    value = json.dumps(startjobs[pj][stat])
                                    players[id][stat] = int(attribs) + int(value)
                                else:
                                    players[id][stat] = int(attribs)

                    print("new player id for")
                    print(players[id]["name"])
                    players[id]["maxhp"] = players[id]["hp"]
                    players[id]["maxmp"] = players[id]["mp"]
                    players[id]["pvp"] = "no"
                    players[id]["tp"] = 0
                    players[id]["exp"] = 0
                    players[id]["level"] = 0
                    players[id]["next"] = 3000
                    players[id]["ujob"] = {
                                            "warrior",
                                            "blackmage",
                                            "whitemage",
                                            "thief"
                                         }


                    # acknowladge the foolish user.

                    mud.send_message(id, "Thank you. Creation successful.")

                    # Show the first look window
                    # though not via 'look' command
                    # i need to make them the same

                    rm = rooms[players[id]["room"]]
                    mud.send_message(id, motd.read())
                    mud.send_message(id, "Welcome to the Nixheads-Mud, {}.\n".format(

                                                                players[id]["name"]))
                    mud.send_message(id, "Type 'help' for a list of commands.")
                    mud.send_message(id, "***************************************************************")
                    mud.send_message(id, rm["name"])
                    mud.send_message(id, "***************************************************************")
                    mud.send_message(id, rm["description"])
                    mud.send_message(id, "***************************************************************")
                    mud.send_message(id, "**** HP: {} **** MP: {} **** NEXT: {} **** PVP: {} ****".format(players[id]["hp"],players[id]["mp"],players[id]["next"],players[id]["pvp"]))
                    mud.send_message(id, "***************************************************************")
                    mud.send_message(id, "Exits are: {}".format(", ".join(rm["exits"])))
                    mud.send_message(id, "***************************************************************")

        # This section initilizes a database
        # for storing players allowing
        # login function to load
        # from the database

        # save command
        elif command == 'save': #players[id]["waitingsave"] is 1:


            # checks database

            userlist = database.get_name(userdata, players[id]["name"])

            if not userlist:

                # function for when a userlist does not exists

                mud.send_message(id, "Creating new save")
                database.save_name(userdata, players[id]["name"], players[id]["room"], players[id]["password"], players[id]["email"], players[id]["user"], players[id]["race"], players[id]["job"], players[id]["coin"])
                print("Created a new save file for:")
                print(players[id]["name"])

            else:

                database.update_name(userdata, players[id]["name"], players[id]["room"], players[id]["password"], players[id]["email"], players[id]["user"], players[id]["race"], players[id]["job"], players[id]["coin"])
                mud.send_message(id, "Updated your file.")
                print("Updated save file for:")
                print(players[id]["name"])

        # emergency reset

        elif command == "reset":

            login[id] = {x: None for x in login[id]}
            players[id] = {x: None for x in players[id]}
            setups[id] = {x: None for x in setups[id]}

            mud.send_message(id, logascii.read())
            mud.send_message(id, "Are you a 'new' player or would you like to 'login'?")

        # character sheet

        elif command == "sheet":
            # very basic character sheet
            mud.send_message(id, "::Basic Stats::")
            mud.send_message(id, "Name: {}".format(players[id]["name"]))
            mud.send_message(id, "Race: {}".format(players[id]["race"]))
            mud.send_message(id, "PvP Status: {}".format(players[id]["pvp"]))
            mud.send_message(id, "Coin: {}".format(players[id]["coin"]))
            mud.send_message(id, "Level: {}".format(players[id]["level"]))
            mud.send_message(id, "Exp/Next: "+ str(players[id]["exp"]) +"/" + str(players[id]["next"]))
            mud.send_message(id, "HP/Max: {}/{}".format(players[id]["hp"], players[id]["maxhp"]))
            mud.send_message(id, "Mp/Max: {}/{}".format(players[id]["mp"], players[id]["maxmp"]))
            mud.send_message(id, "Tech Points: {}".format(players[id]["tp"]))
            mud.send_message(id, "::Character Stats::")
            mud.send_message(id, "Strength: {}".format(players[id]["str"]))
            mud.send_message(id, "Dexterity: {}".format(players[id]["dex"]))
            mud.send_message(id, "Vitality: {}".format(players[id]["vit"]))
            mud.send_message(id, "Intelligence: {}".format(players[id]["int"]))
            mud.send_message(id, "Mind: {}".format(players[id]["mnd"]))
            mud.send_message(id, "Charisma: {}".format(players[id]["cha"]))
            mud.send_message(id, "Crit. Modifer: {}".format(players[id]["crit"]))
            mud.send_message(id, "::Spells::")
            mud.send_message(id, " ")
            mud.send_message(id, "::Skills::")
            mud.send_message(id, " ")
            mud.send_message(id, "::User Rank:::::::::Current Job::")
            mud.send_message(id, ":: {}".format(players[id]["user"]) + "      ::  {}".format(players[id]["job"]))
            mud.send_message(id, "::Unlocked Jobs::")
            mud.send_message(id, " ")

        # help file command

        elif command == "help":

            # send the player back the list of possible commands
            # this will be overhauled to allow lower param

            mud.send_message(id, "Commands:")

            mud.send_message(id, "  say <message>  - Says something out loud, "

                                 + "e.g. 'say Hello'")

            mud.send_message(id, "  look           - Examines the "

                                 + "surroundings, e.g. 'look'")

            mud.send_message(id, "  go <exit>      - Moves through the exit "

                                 + "specified, e.g. 'go outside'")
            mud.send_message(id, "  exam           - Give a closer look at an object "
                                 + "e.g 'exam chair'")

        # 'system' command
        # outputs a message to all users in game
        # useful during server maintenace to warn players to save.
        elif command == "system":

            for pid, pl in players.items():

                mud.send_message(pid, "{}: SYSTEM MESSAGE!!: {}".format(
                                                                players[id]["name"], params))
        # 'tell' command

        elif command == "tell":

            st = params.lower()
            mud.send_message(id, "You tell {}: {}".format(st, params))
            # go through every player in the game

            for pid, pl in players.items():

                # if name matches

                if st == players[pid]["name"]:

                    mud.send_message(pid, "{} whispers: {}".format(players[id]["name"], params))


                if st != players[pid]["name"]:

                    mud.send_message(id, "That use cannot be found...")

        # 'say' command

        elif command == "say":

            # go through every player in the game


            for pid, pl in players.items():

                # if they're in the same room as the player

                if players[pid]["name"] == players[id]["room"]:

                    # send them a message telling them what the player said

                    mud.send_message(pid, "{} says: {}".format(

                                                players[id]["name"], params))

        # 'shutdown' command
        # shutdowns server
        # make this a gm command later

        elif command == 'shutdown':
            print("Mud shutdown")
            print("Reason: ", params)
            for pid, pl in players.items():
                mud.send_message(pid, "Saving your data because server is shutting down.")
                userlist = database.get_name(userdata, players[id]["name"])
                print(players[pid]["name"])
                if not userlist:
                    mud.send_message(pid, "Creating new save.")
                    database.save_name(userdata, players[pid]["name"], players[pid]["room"], players[pid]["password"],        players[pid]["email"], players[pid]["user"], players[pid]["race"], players[pid]["job"], players[pid]["coin"])
                    print("Saved")
                else:

                    for user in userlist:
                        if user[0] == players[pid]["name"]:
                                database.update_name(userdata, players[pid]["name"], players[pid]["room"], players[pid]["password"], players[pid]["email"], players[pid]["user"], players[pid]["race"], players[pid]["job"], players[pid]["coin"])
                                print("saved")

            mud.shutdown()


        # 'look' command

        elif command == "look":

            # store the player's current room

            rm = rooms[players[id]["room"]]

            # send the player back the description of their current room

            #mud.send_message(id, rm["description"])
            mud.send_message(id, "***************************************************************")
            mud.send_message(id, rm["name"])
            mud.send_message(id, "***************************************************************")
            mud.send_message(id, rm["description"])
            mud.send_message(id, "***************************************************************")
            mud.send_message(id, "**** HP: {} **** MP: {} **** NEXT: {} **** PVP: {} ****".format(players[id]["hp"],players[id]["mp"],players[id]["next"],players[id]["pvp"]))
            mud.send_message(id, "***************************************************************")
            mud.send_message(id, "Exits are: {}".format(", ".join(rm["exits"])))
            mud.send_message(id, "***************************************************************")


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

            # Dragonkeeper:
            # not sure how to get this info from the live database
            # we cannot explicitly check for each individual monster
            # whatever room we are in.  there will be thousands.

            for cid in credb.keys():
                #for stat in credb[cid]:
                if credb[cid]["room"] == players[id]["room"]:
                    cx = credb[cid]["desc"]
                    mud.send_message(id, "{}".format("".join(cx)))


        # 'exam' command

        elif command == "exam":

            # store the object name

            oj = params.lower()

            # store the player's current room

            rm = rooms[players[id]["room"]]

            #if the object exists in room

            if oj in rm["objects"]:

            # Show object exam description

                mud.send_message(id, rm["objects"][oj])

            # Otherwise tell them they are stupid

            else:

                mud.send_message(id, "Nothing like that to examine.")

        # 'fight' command

        elif command == "fight":

            # store the target

            #ck = params.lower()

            # store the player's current room

            #rm = rooms[players[id]["room"]]

            # check if target is the target in room

            mud.send_message(id, "not setup yet")
            #if ck in rm["creaturecheck"]:

                # insert combat code here and remove the test

                #mud.send_message(id, "You squish the " + rm["creaturecheck"][ck])

                # set a timer to make the spider disapeer



            # Call the player stupid

            #else:

               # mud.send_message(id, "There is nothing like that to fight.")


        # 'go' command

        elif command == "go":

            # store the exit name

            ex = params.lower()

            # store the player's current room

            rm = rooms[players[id]["room"]]

            # if the specified exit is found in the room's exits list

            if ex in rm["exits"]:

                # go through all the players in the game

                for pid, pl in players.items():

                    # if player is in the same room and isn't the player

                    # sending the command

                    if players[pid]["room"] == players[id]["room"]\
                            and pid != id:

                        # send them a message telling them that the player

                        # left the room

                        mud.send_message(pid, "{} left via exit '{}'".format(

                                                      players[id]["name"], ex))

                # update the player's current room to the one the exit leads to

                players[id]["room"] = rm["exits"][ex]

                # possible place for description after moving
                rm = rooms[players[id]["room"]]

                mud.send_message(id, "***************************************************************")
                mud.send_message(id, rm["name"])
                mud.send_message(id, "***************************************************************")
                mud.send_message(id, rm["description"])
                mud.send_message(id, "***************************************************************")
                mud.send_message(id, "**** HP: {} **** MP: {} **** NEXT: {} **** PVP: {} ****".format(players[id]["hp"],players[id]["mp"],players[id]["next"],players[id]["pvp"]))
                mud.send_message(id, "***************************************************************")
                mud.send_message(id, "Exits are: {}".format(", ".join(rm["exits"])))
                mud.send_message(id, "***************************************************************")


                rm = rooms[players[id]["room"]]
                # go through all the players in the game

                for pid, pl in players.items():

                    # if player is in the same (new) room and isn't the player

                    # sending the command

                    if players[pid]["room"] == players[id]["room"] \
                            and pid != id:

                        # send them a message telling them that the player

                        # entered the room

                        mud.send_message(pid,

                                         "{} arrived via exit '{}'".format(

                                                      players[id]["name"], ex))


            # the specified exit wasn't found in the current room

            else:

                # send back an 'unknown exit' message

                mud.send_message(id, "Unknown exit '{}'".format(ex))

        elif command == 'blank':
            continue
        # some other, unrecognised command

        else:

            # send back an 'unknown command' message

                mud.send_message(id, "This is not a valid command '{}', silly dumb dumb.".format(command))


