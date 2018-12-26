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

"""

import time
import db as database
import json

# import the MUD server class

from mudserver import MudServer

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
with open("Maps/gm.json") as room:
    map7 = json.load(room)

# put all the map files together

rooms = {**map1, **map2, **map3, **map4, **map5, **map6, **map7}


# import ascii files

motd = open("Art/MOTD")
todo = open("Art/todo")

# import help files
with open("Help/help1.json") as helpfile:

    helpfiles = json.load(helpfile)

with open("Races/races.json") as raceoptions:

    races = json.load(raceoptions)

with open("Classes/classes.json") as joboptions:

    jobs = json.load(joboptions)

# stores the players in the game

setups = {}
players = {}

# start the server

mud = MudServer()

##connect to db for player saves
userdata = database.connect()

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

        # add the new player to the dictionary, noting that they've not been

        # named yet.

        # The dictionary key is the player's id number. We set their room to

        # None initially until they have entered a name

        # Try adding more player stats - level, gold, inventory, etc

        setups[id] = {

                "setup": None,
                "confirm": None,
                "match": None,
                "name": None,
                "pickrace" : None,
                "race": None,
                "class": None,
                "pickclass": None,
                "user" : None,
                "email": None,
                "password": None,
                }

        players[id] = {

            "name": None,

            "email": None,

            "password": None,

            "room": None,

            "user": None,

            "race": None,

            "class": None,

            "coin": 0,

            "waitingsave": None,


        }


        # send the new player a prompt for their name

        mud.send_message(id, "Are you a 'new' player or would you like to 'login'? ")



    # go through any recently disconnected players

    for id in mud.get_disconnected_players():

        # if for any reason the player isn't in the player map, skip them and

        # move on to the next one

        if id not in players:

            continue

        # go through all the players in the game

        for pid, pl in players.items():

            # send each player a message to tell them about the diconnected

            # player

            mud.send_message(pid, "{} quit the game".format(

                                                        players[id]["name"]))

        # remove the player's entry in the player dictionary

        del(players[id])

    # go through any new commands sent from players


    for id, command, params in mud.get_commands():

        # if for any reason the player isn't in the player map, skip them and

        # move on to the next one

        if setups[id]["setup"] != None:
            if setups[id]["setup"] == "name":
                setups[id]["name"] = command
            if setups[id]["setup"] == "email":
                setups[id]["email"] = command
            if setups[id]["setup"] == "password":
                setups[id]["password"] = command
            if setups[id]["setup"] == "confirm":
                setups[id]["confirm"] = command
            if setups[id]["setup"] == "race":
                setups[id]["race"] = command
            if setups[id]["setup"] == "pickrace":
                setups[id]["pickrace"]  = command
            if setups[id]["setup"] == "class":
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


        # each of the possible commands is handled below. Try adding new

        # commands to the game!

        # 'help' command

        elif command == "login":
            mud.send_message(id, "Pending...")

        elif command == "new":

            # Setup a setups[id] section with info and pipe it into players

            if setups[id]["name"] is None:

                mud.send_message(id, "Enter a Name:")

                setups[id]["setup"] = "name"

            if setups[id]["email"] is None:

                if setups[id]["name"] != None:

                    mud.send_message(id, "Your Name is: {}".format(

                                                          setups[id]["name"]))

                    mud.send_message(id, "Enter an Email Address:")

                    setups[id]["setup"] = "email"

            if setups[id]["password"] is None:

                if setups[id]["email"] != None:

                    mud.send_message(id, "Your Email is: {}".format(

                                                          setups[id]["email"]))

                    mud.send_message(id, "Enter a password:")

                    setups[id]["setup"] = "password"

            if setups[id]["confirm"] is None:

                if setups[id]["password"] != None:

                    mud.send_message(id, "Confirm password:")

                    setups[id]["setup"] = "confirm"

            if setups[id]["confirm"] != None:


                if setups[id]["password"] == setups[id]["confirm"]:

                   # setups[id]["confirm"] = None

                    setups[id]["match"] = "yes"

                    setups[id]["setup"] = "pickrace"

                else:

                    mud.send_message(id, "Passwords do not match.")
                    mud.send_message(id, "Please enter a password:")

                    setups[id]["password"] = None

                    setups[id]["confirm"] = None

                    setups[id]["setup"] = "password"

            if setups[id]["pickrace"] is None:

                if setups[id]["match"] == "yes":

                    mud.send_message(id, "Now lets take a second to pick a race.\n'elvari' hail from Kelfram, they are very good with magic.\nThey tend to be tall thing characters.\n'humani' are descendents of the children of earth.\nThey are balanced in both strengths and weaknesses\n'dragani' are hybrid dragonic humanoids from the Mistlands.\n  They have wings to fly short distances and can see in the dark.\n'krei' are an ancient mystical race of catlike humanoids from The Villa")

                    mud.send_message(id, "of Neff.  They are ferocious and agile.")


                if setups[id]["setup"] == "pickrace":

                    mud.send_message(id, "Pick a race:")

            if setups[id]["pickrace"] != None:

                if setups[id]["pickrace"] not in races:

                    mud.send_message(id, "Not a valid race.\nPick a race:")

                    setups[id]["pickrace"] = None

                else:

                    if setups[id]["race"] is None:

                        setups[id]["race"] = setups[id]["pickrace"]

                        setups[id]["setup"] = "class"

                        mud.send_message(id, "warrior, blackmage, whitemage, thief.\n#write up descriptions.\nFor now pick one:")

            if setups[id]["pickclass"] != None:

                if setups[id]["pickclass"] not in jobs:

                    mud.send_message(id, "Not a valid class.\nPick a class:")

                    setups[id]["pickclass"] = None

                else:

                    setups[id]["class"] = setups[id]["pickclass"]
                    setups[id]["setup"] = "merge"

            if setups[id]["setup"] == "merge":

                players[id]["name"] = setups[id]["name"]
                players[id]["email"] = setups[id]["email"]
                players[id]["password"] = setups[id]["password"]
                players[id]["race"] = setups[id]["race"]
                players[id]["class"] = setups[id]["class"]
                players[id]["user"] = "normal"
                players[id]["room"] = "Lounge"
                setups[id]["setup"] = None
                mud.send_message(id, "Thank you. Creation successful.")
                mud.send_message(id, motd.read())
                mud.send_message(id, "Welcome to the Nixheads-Mud, {}.\n".format(

                                                                players[id]["name"]))
                mud.send_message(id, "Type 'help' for a list of commands.")
                mud.send_message(id, rooms[players[id]["room"]]["description"])



        # save command
        elif players[id]["waitingsave"] is 1:
            if players[id]["password"] is None:
                players[id]["password"] = command

            mud.send_message(id, "saving")
            userlist = database.get_name(userdata, players[id]["name"])
            print(userlist)

            if not userlist:
               ## create new save
                mud.send_message(id, "Creating new save")
                database.save_name(userdata, players[id]["name"], players[id]["room"], players[id]["password"])
                for users in database.get_name(userdata, players[id]["name"]):
                    if user[0] is players[id]["name"]:
                        mud.send_message(id, "New Save Created")
            else:
                for user in userlist:
                     if user[0] == players[id]["name"]:
                         mud.send_message(id, "found current user")
                         if players[id]["password"] == user[2]:
                             mud.send_message(id, "password match")
                             database.update_name(userdata, players[id]["name"], players[id]["room"], players[id]["password"])
                             for users in database.get_name(userdata, players[id]["name"]):
                                 if user[1] is players[id]["room"]:
                                     mud.send_message(id, "Save Completed")
                                 else:
                                     mud.send_message(id, "Save Failed")
                         else:
                             mud.send_message(id, "Passwords do not match")
            players[id]["waitingsave"] = 0

        elif command == "save":
            if players[id]["name"] is not None:
                players[id]["waitingsave"] = 1
                if players[id]["password"] is None:
                    mud.send_message(id, "Type a password for " + players[id]["name"])
                else:
                    mud.send_message(id, "ready to save")
            else:
                mud.send_message(id, "Your name is invalid. please set a username")


        elif command == "help":

            # send the player back the list of possible commands

            mud.send_message(id, "Commands:")

            mud.send_message(id, "  say <message>  - Says something out loud, "

                                 + "e.g. 'say Hello'")

            mud.send_message(id, "  look           - Examines the "

                                 + "surroundings, e.g. 'look'")

            mud.send_message(id, "  go <exit>      - Moves through the exit "

                                 + "specified, e.g. 'go outside'")
            mud.send_message(id, "  exam           - Give a closer look at an object "
                                 + "e.g 'exam chair'")




        # 'say' command

        elif command == "say":

            # go through every player in the game

            for pid, pl in players.items():

                # if they're in the same room as the player

                if players[pid]["room"] == players[id]["room"]:

                    # send them a message telling them what the player said

                    mud.send_message(pid, "{} says: {}".format(

                                                players[id]["name"], params))

        # 'look' command

        elif command == "look":

            # store the player's current room

            rm = rooms[players[id]["room"]]

            # send the player back the description of their current room

            mud.send_message(id, rm["description"])

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

            # send player a message containing the list of players in the room

            mud.send_message(id, "Players here: {}".format(

                                                    ", ".join(playershere)))


            # send player a message containing the list of creatures in the room

            # check to see if any exist

            if rm["creaturecheck"]["number"] != "none":

                mud.send_message(id, "{}".format(

                                          "\n".join(rm["creaturedesc"])))

                # mud.send_message(id, "Creatures here: {}".format(

                #                                      ", ".join(rm["creatures"])))

            # send player a message containing the list of exits from this room

            mud.send_message(id, "Exits are: {}".format(

                                                    ", ".join(rm["exits"])))
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

            ck = params.lower()

            # store the player's current room

            rm = rooms[players[id]["room"]]

            # check if target is the target in room

            if ck in rm["creaturecheck"]:

                # insert combat code here and remove the test

                mud.send_message(id, "You squish the " + rm["creaturecheck"][ck])

                # set a timer to make the spider disapeer



            # Call the player stupid

            else:

                mud.send_message(id, "There is nothing like that to fight.")


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

                mud.send_message(id, rm["description"])


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

                # send the player a message telling them where they are now

                mud.send_message(id, "You arrive at '{}'".format(

                                                          players[id]["room"]))

            # the specified exit wasn't found in the current room

            else:

                # send back an 'unknown exit' message

                mud.send_message(id, "Unknown exit '{}'".format(ex))

        elif command == 'blank':
            continue
        # some other, unrecognised command

        else:

            # send back an 'unknown command' message

                mud.send_message(id, "Unknown command '{}'".format(command))

