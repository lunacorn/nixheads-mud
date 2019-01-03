# nixheads-mud

=^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=

-----------------------------------------------------------

Thank you for visiting https://nixheads.co.uk

-----------------------------------------------------------

This Mud runs the nixheads-mud codebase.  

A heavily modified version of its former

simplemud.  Written with python and json

this overhauled codebase aims to be a api

for a very open ended and customizable mud

codebase.

--------------------------------------------------------------------

=^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^.^=

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

--------------------------------------------------------------------

-- Creature Database / Object Overhaul

--------------------------------------------------------------------

    As mentioned in the first minor release the objects and maps

    are going through an overhaul.  there is a creature database

    created though not yet implemented.  It will give creatures

    assigned unique numbers and seperate them from static maps.

    Allowing them to move and be interacted with and killed as

    well as looted once the inventory database is set up.

--------------------------------------------------------------------

-- Refined maps

--------------------------------------------------------------------

    Maps are currently being templated to work with the current

    manner of interaction.  They will be bare, however crash proof

    allowing characters to move around and get aquainted with the

    game.  There will be a few randoom poke objects to interact

    with and make use of some of the commands.

--------------------------------------------------------------------

-- Comment Cleanup

--------------------------------------------------------------------

    Though this does not affect the user, the goal is to provide

    clear documentation and templates for the nixmud codebase.

    Therefore it is essential to make sure current features have

    reasonably neat and readable comments.

    You will find that much more useable moving forward, and

    expect the documentation to continue with further releases.

--------------------------------------------------------------------

-- Emergency Reset

--------------------------------------------------------------------

    We have implemented a failsafe which in times of server crash

    risk it will disconnect the player in question, and send them

    back to a usable login screen.  This will help with error

    handling and is a nice bump to start for known issues.

    currently it is only used when issues of eternal loops occur.

--------------------------------------------------------------------

Team: Dragonkeeper, Lunacorn  Dec 26th, 2018
--------------------------------------------------------------------

Nix-mud 0.1.0                           https://nixheads.co.uk

--------------------------------------------------------------------

This version implements the following features

--------------------------------------------------------------------

-- New player creation

--------------------------------------------------------------------

    New player creation with the ability to save and login via

    character name and password.

---------------------------------------------------------------------

-- objects

---------------------------------------------------------------------

    Objects are allowed to be examined, or attacked.  This will go

through heavy overhaul in the version to come as a combat system is

implemnented.  For now they are very loose fitings.

---------------------------------------------------------------------

-- System Message

---------------------------------------------------------------------

    A command 'system' allows your to speak to whole of server as a

channel.  Similar to say, though it works beyond a single room.

---------------------------------------------------------------------

Team: Dragonkeeper, Lunacorn  Dec 25th-26th, 2018
