#import the 'tkinter' module
from tkinter import *
from tkinter import filedialog
import json
#create a new window
window = Tk()
#set the window title
window.title("Map Builder - Json")
#set the window icon
#window.wm_iconbitmap('alien.ico')

#    Label(window, text="How Many Levels?").grid(row=0,column=0)

#create a text entry widget called 'ent'
#create a button widget called btn
#btn = Button(window, text="Create").grid(row=1,column=1)

#pack (add) the widgets into the window
def RoomCount():
    roomamount[0] += 1
    AddRoom()

def AddRoom():
    if generate[0] == 0:
        if roomamount[0] == 1:
            addlevelsbutton = Button(window, text="Add room", command=lambda: RoomCount()).grid(row=0,column=4)
            generatebutton = Button(window, text="Generate", command=lambda: Generate()).grid(row=0,column=6)
            browsebutton = Button(window, text="Browse", command=lambda: OpenFileBrowse()).grid(row=0,column=5)

            Label(window, text="Top Level Room Name").grid(row=0,column=1)
            Label(window, text="room 1").grid(row=1,column=0)
            room1 = Entry(window).grid(row=1,column=1)
            Label(window, text="Name").grid(row=0,column=2)
            name1 = Entry(window).grid(row=1,column=2)
            Label(window, text="description").grid(row=0,column=3)
            desc1 = Entry(window).grid(row=1,column=3)
            Label(window, text="-----------------").grid(row=11,column=1)
            Label(window, text="-----------------").grid(row=11,column=2)
            Label(window, text="-----------------").grid(row=11,column=3)
            Label(window, text="Room 1 exits").grid(row=12,column=0)
            Label(window, text=" destination").grid(row=13,column=0)
            r1exits1 = Entry(window).grid(row=12,column=1)
            r1exits2 = Entry(window).grid(row=12,column=2)
            r1exits3 = Entry(window).grid(row=12,column=3)
            r1exits4 = Entry(window).grid(row=12,column=4)
            r1exits5 = Entry(window).grid(row=12,column=5)
            r1exits6 = Entry(window).grid(row=12,column=6)
            r1exits7 = Entry(window).grid(row=12,column=7)
            r1exits1a = Entry(window).grid(row=13,column=1)
            r1exits2a = Entry(window).grid(row=13,column=2)
            r1exits3a = Entry(window).grid(row=13,column=3)
            r1exits4a = Entry(window).grid(row=13,column=4)
            r1exits5a = Entry(window).grid(row=13,column=5)
            r1exits6a = Entry(window).grid(row=13,column=6)
            r1exits7a = Entry(window).grid(row=13,column=7)
            Label(window, text=" objects name").grid(row=14,column=0)
            Label(window, text=" objects desc").grid(row=15,column=0)
            r1objects1 = Entry(window).grid(row=14,column=1)
            r1objects1a = Entry(window).grid(row=15,column=1)
            r1objects2 = Entry(window).grid(row=14,column=2)
            r1objects2a = Entry(window).grid(row=15,column=2)
            Label(window, text="Door :").grid(row=14,column=3)
            Label(window, text="status").grid(row=14,column=4)
            Label(window, text="exit").grid(row=14,column=5)
            Label(window, text="locked").grid(row=14,column=6)
            Label(window, text="mapto").grid(row=14,column=7)
            r1doorstatus = Entry(window).grid(row=15,column=4)
            r1doorexit = Entry(window).grid(row=15,column=5)
            r1doorlocked = Entry(window).grid(row=15,column=6)
            r1doormapto = Entry(window).grid(row=15,column=7)
            Label(window, text="-----------------").grid(row=16,column=1)
            Label(window, text="-----------------").grid(row=16,column=2)
            Label(window, text="-----------------").grid(row=16,column=3)
            Label(window, text="-----------------").grid(row=16,column=4)
            Label(window, text="-----------------").grid(row=16,column=5)
            Label(window, text="-----------------").grid(row=16,column=6)
            Label(window, text="-----------------").grid(row=16,column=7)
        if roomamount[0] == 2:
            Label(window, text="room 2").grid(row=2,column=0)
            room2 = Entry(window).grid(row=2,column=1)
            name2 = Entry(window).grid(row=2,column=2)
            desc2 = Entry(window).grid(row=2,column=3)
            Label(window, text="Room 2 exits").grid(row=row[0],column=0)
            r2exits1 = Entry(window).grid(row=row[0],column=1)
            r2exits2 = Entry(window).grid(row=row[0],column=2)
            r2exits3 = Entry(window).grid(row=row[0],column=3)
            r2exits4 = Entry(window).grid(row=row[0],column=4)
            r2exits5 = Entry(window).grid(row=row[0],column=5)
            r2exits6 = Entry(window).grid(row=row[0],column=6)
            r2exits7 = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" destination").grid(row=row[0],column=0)
            r2exits1a = Entry(window).grid(row=row[0],column=1)
            r2exits2a = Entry(window).grid(row=row[0],column=2)
            r2exits3a = Entry(window).grid(row=row[0],column=3)
            r2exits4a = Entry(window).grid(row=row[0],column=4)
            r2exits5a = Entry(window).grid(row=row[0],column=5)
            r2exits6a = Entry(window).grid(row=row[0],column=6)
            r2exits7a = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects name").grid(row=row[0],column=0)
            r2objects1 = Entry(window).grid(row=row[0],column=1)
            r2objects1 = Entry(window).grid(row=row[0],column=1)
            r2objects2 = Entry(window).grid(row=row[0],column=2)
            Label(window, text="Door :").grid(row=row[0],column=3)
            Label(window, text="status").grid(row=row[0],column=4)
            Label(window, text="exit").grid(row=row[0],column=5)
            Label(window, text="locked").grid(row=row[0],column=6)
            Label(window, text="mapto").grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects desc").grid(row=row[0],column=0)
            r2objects1a = Entry(window).grid(row=row[0],column=1)
            r2objects2a = Entry(window).grid(row=row[0],column=2)
            r2doorstatus = Entry(window).grid(row=row[0],column=4)
            r2doorexit = Entry(window).grid(row=row[0],column=5)
            r2doorlocked = Entry(window).grid(row=row[0],column=6)
            r2doormapto = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text="-----------------").grid(row=row[0],column=1)
            Label(window, text="-----------------").grid(row=row[0],column=2)
            Label(window, text="-----------------").grid(row=row[0],column=3)
            Label(window, text="-----------------").grid(row=row[0],column=4)
            Label(window, text="-----------------").grid(row=row[0],column=5)
            Label(window, text="-----------------").grid(row=row[0],column=6)
            Label(window, text="-----------------").grid(row=row[0],column=7)
            row[0] += 1
        if roomamount[0] == 3:
            Label(window, text="room 3").grid(row=3,column=0)
            room3 = Entry(window).grid(row=3,column=1)
            name3 = Entry(window).grid(row=3,column=2)
            desc3 = Entry(window).grid(row=3,column=3)
            Label(window, text="Room 3 exits").grid(row=row[0],column=0)
            r3exits1 = Entry(window).grid(row=row[0],column=1)
            r3exits2 = Entry(window).grid(row=row[0],column=2)
            r3exits3 = Entry(window).grid(row=row[0],column=3)
            r3exits4 = Entry(window).grid(row=row[0],column=4)
            r3exits5 = Entry(window).grid(row=row[0],column=5)
            r3exits6 = Entry(window).grid(row=row[0],column=6)
            r3exits7 = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" destination").grid(row=row[0],column=0)
            r3exits1a = Entry(window).grid(row=row[0],column=1)
            r3exits2a = Entry(window).grid(row=row[0],column=2)
            r3exits3a = Entry(window).grid(row=row[0],column=3)
            r3exits4a = Entry(window).grid(row=row[0],column=4)
            r3exits5a = Entry(window).grid(row=row[0],column=5)
            r3exits6a = Entry(window).grid(row=row[0],column=6)
            r3exits7a = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects name").grid(row=row[0],column=0)
            r3objects1 = Entry(window).grid(row=row[0],column=1)
            r3objects1 = Entry(window).grid(row=row[0],column=1)
            r3objects2 = Entry(window).grid(row=row[0],column=2)
            Label(window, text="Door :").grid(row=row[0],column=3)
            Label(window, text="status").grid(row=row[0],column=4)
            Label(window, text="exit").grid(row=row[0],column=5)
            Label(window, text="locked").grid(row=row[0],column=6)
            Label(window, text="mapto").grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects desc").grid(row=row[0],column=0)
            r3objects1a = Entry(window).grid(row=row[0],column=1)
            r3objects2a = Entry(window).grid(row=row[0],column=2)
            r3doorstatus = Entry(window).grid(row=row[0],column=4)
            r3doorexit = Entry(window).grid(row=row[0],column=5)
            r3doorlocked = Entry(window).grid(row=row[0],column=6)
            r3doormapto = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text="-----------------").grid(row=row[0],column=1)
            Label(window, text="-----------------").grid(row=row[0],column=2)
            Label(window, text="-----------------").grid(row=row[0],column=3)
            Label(window, text="-----------------").grid(row=row[0],column=4)
            Label(window, text="-----------------").grid(row=row[0],column=5)
            Label(window, text="-----------------").grid(row=row[0],column=6)
            Label(window, text="-----------------").grid(row=row[0],column=7)
            row[0] += 1

        if roomamount[0] == 4:
            Label(window, text="room 4").grid(row=4,column=0)
            room4 = Entry(window).grid(row=4,column=1)
            name4 = Entry(window).grid(row=4,column=2)
            desc4 = Entry(window).grid(row=4,column=3)
            Label(window, text="Room 4 exits").grid(row=row[0],column=0)
            r4exits1 = Entry(window).grid(row=row[0],column=1)
            r4exits2 = Entry(window).grid(row=row[0],column=2)
            r4exits3 = Entry(window).grid(row=row[0],column=3)
            r4exits4 = Entry(window).grid(row=row[0],column=4)
            r4exits5 = Entry(window).grid(row=row[0],column=5)
            r4exits6 = Entry(window).grid(row=row[0],column=6)
            r4exits7 = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" destination").grid(row=row[0],column=0)
            r4exits1a = Entry(window).grid(row=row[0],column=1)
            r4exits2a = Entry(window).grid(row=row[0],column=2)
            r4exits3a = Entry(window).grid(row=row[0],column=3)
            r4exits4a = Entry(window).grid(row=row[0],column=4)
            r4exits5a = Entry(window).grid(row=row[0],column=5)
            r4exits6a = Entry(window).grid(row=row[0],column=6)
            r4exits7a = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects name").grid(row=row[0],column=0)
            r4objects1 = Entry(window).grid(row=row[0],column=1)
            r4objects1 = Entry(window).grid(row=row[0],column=1)
            r4objects2 = Entry(window).grid(row=row[0],column=2)
            Label(window, text="Door :").grid(row=row[0],column=3)
            Label(window, text="status").grid(row=row[0],column=4)
            Label(window, text="exit").grid(row=row[0],column=5)
            Label(window, text="locked").grid(row=row[0],column=6)
            Label(window, text="mapto").grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects desc").grid(row=row[0],column=0)
            r4objects1a = Entry(window).grid(row=row[0],column=1)
            r4objects2a = Entry(window).grid(row=row[0],column=2)
            r4doorstatus = Entry(window).grid(row=row[0],column=4)
            r4doorexit = Entry(window).grid(row=row[0],column=5)
            r4doorlocked = Entry(window).grid(row=row[0],column=6)
            r4doormapto = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text="-----------------").grid(row=row[0],column=1)
            Label(window, text="-----------------").grid(row=row[0],column=2)
            Label(window, text="-----------------").grid(row=row[0],column=3)
            Label(window, text="-----------------").grid(row=row[0],column=4)
            Label(window, text="-----------------").grid(row=row[0],column=5)
            Label(window, text="-----------------").grid(row=row[0],column=6)
            Label(window, text="-----------------").grid(row=row[0],column=7)
            row[0] += 1

        if roomamount[0] == 5:
            Label(window, text="room 5").grid(row=5,column=0)
            room5 = Entry(window).grid(row=5,column=1)
            name5 = Entry(window).grid(row=5,column=2)
            desc5 = Entry(window).grid(row=5,column=3)
            Label(window, text="Room 5 exits").grid(row=row[0],column=0)
            r5exits1 = Entry(window).grid(row=row[0],column=1)
            r5exits2 = Entry(window).grid(row=row[0],column=2)
            r5exits3 = Entry(window).grid(row=row[0],column=3)
            r5exits4 = Entry(window).grid(row=row[0],column=4)
            r5exits5 = Entry(window).grid(row=row[0],column=5)
            r5exits6 = Entry(window).grid(row=row[0],column=6)
            r5exits7 = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" destination").grid(row=row[0],column=0)
            r5exits1a = Entry(window).grid(row=row[0],column=1)
            r5exits2a = Entry(window).grid(row=row[0],column=2)
            r5exits3a = Entry(window).grid(row=row[0],column=3)
            r5exits4a = Entry(window).grid(row=row[0],column=4)
            r5exits5a = Entry(window).grid(row=row[0],column=5)
            r5exits6a = Entry(window).grid(row=row[0],column=6)
            r5exits7a = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects name").grid(row=row[0],column=0)
            r5objects1 = Entry(window).grid(row=row[0],column=1)
            r5objects1 = Entry(window).grid(row=row[0],column=1)
            r5objects2 = Entry(window).grid(row=row[0],column=2)
            Label(window, text="Door :").grid(row=row[0],column=3)
            Label(window, text="status").grid(row=row[0],column=4)
            Label(window, text="exit").grid(row=row[0],column=5)
            Label(window, text="locked").grid(row=row[0],column=6)
            Label(window, text="mapto").grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects desc").grid(row=row[0],column=0)
            r5objects1a = Entry(window).grid(row=row[0],column=1)
            r5objects2a = Entry(window).grid(row=row[0],column=2)
            r5doorstatus = Entry(window).grid(row=row[0],column=4)
            r5doorexit = Entry(window).grid(row=row[0],column=5)
            r5doorlocked = Entry(window).grid(row=row[0],column=6)
            r5doormapto = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text="-----------------").grid(row=row[0],column=1)
            Label(window, text="-----------------").grid(row=row[0],column=2)
            Label(window, text="-----------------").grid(row=row[0],column=3)
            Label(window, text="-----------------").grid(row=row[0],column=4)
            Label(window, text="-----------------").grid(row=row[0],column=5)
            Label(window, text="-----------------").grid(row=row[0],column=6)
            Label(window, text="-----------------").grid(row=row[0],column=7)
            row[0] += 1

        if roomamount[0] == 6:
            Label(window, text="room 6").grid(row=6,column=0)
            room6 = Entry(window).grid(row=6,column=1)
            name6 = Entry(window).grid(row=6,column=2)
            desc6 = Entry(window).grid(row=6,column=3)
            Label(window, text="Room 6 exits").grid(row=row[0],column=0)
            r6exits1 = Entry(window).grid(row=row[0],column=1)
            r6exits2 = Entry(window).grid(row=row[0],column=2)
            r6exits3 = Entry(window).grid(row=row[0],column=3)
            r6exits4 = Entry(window).grid(row=row[0],column=4)
            r6exits5 = Entry(window).grid(row=row[0],column=5)
            r6exits6 = Entry(window).grid(row=row[0],column=6)
            r6exits7 = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" destination").grid(row=row[0],column=0)
            r6exits1a = Entry(window).grid(row=row[0],column=1)
            r6exits2a = Entry(window).grid(row=row[0],column=2)
            r6exits3a = Entry(window).grid(row=row[0],column=3)
            r6exits4a = Entry(window).grid(row=row[0],column=4)
            r6exits5a = Entry(window).grid(row=row[0],column=5)
            r6exits6a = Entry(window).grid(row=row[0],column=6)
            r6exits7a = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects name").grid(row=row[0],column=0)
            r6objects1 = Entry(window).grid(row=row[0],column=1)
            r6objects1 = Entry(window).grid(row=row[0],column=1)
            r6objects2 = Entry(window).grid(row=row[0],column=2)
            Label(window, text="Door :").grid(row=row[0],column=3)
            Label(window, text="status").grid(row=row[0],column=4)
            Label(window, text="exit").grid(row=row[0],column=5)
            Label(window, text="locked").grid(row=row[0],column=6)
            Label(window, text="mapto").grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects desc").grid(row=row[0],column=0)
            r6objects1a = Entry(window).grid(row=row[0],column=1)
            r6objects2a = Entry(window).grid(row=row[0],column=2)
            r6doorstatus = Entry(window).grid(row=row[0],column=4)
            r6doorexit = Entry(window).grid(row=row[0],column=5)
            r6doorlocked = Entry(window).grid(row=row[0],column=6)
            r6doormapto = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text="-----------------").grid(row=row[0],column=1)
            Label(window, text="-----------------").grid(row=row[0],column=2)
            Label(window, text="-----------------").grid(row=row[0],column=3)
            Label(window, text="-----------------").grid(row=row[0],column=4)
            Label(window, text="-----------------").grid(row=row[0],column=5)
            Label(window, text="-----------------").grid(row=row[0],column=6)
            Label(window, text="-----------------").grid(row=row[0],column=7)
            row[0] += 1

        if roomamount[0] == 7:
            Label(window, text="room 7").grid(row=7,column=0)
            room7 = Entry(window).grid(row=7,column=1)
            name7 = Entry(window).grid(row=7,column=2)
            desc7 = Entry(window).grid(row=7,column=3)
            Label(window, text="Room 7 exits").grid(row=row[0],column=0)
            r7exits1 = Entry(window).grid(row=row[0],column=1)
            r7exits2 = Entry(window).grid(row=row[0],column=2)
            r7exits3 = Entry(window).grid(row=row[0],column=3)
            r7exits4 = Entry(window).grid(row=row[0],column=4)
            r7exits5 = Entry(window).grid(row=row[0],column=5)
            r7exits6 = Entry(window).grid(row=row[0],column=6)
            r7exits7 = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" destination").grid(row=row[0],column=0)
            r7exits1a = Entry(window).grid(row=row[0],column=1)
            r7exits2a = Entry(window).grid(row=row[0],column=2)
            r7exits3a = Entry(window).grid(row=row[0],column=3)
            r7exits4a = Entry(window).grid(row=row[0],column=4)
            r7exits5a = Entry(window).grid(row=row[0],column=5)
            r7exits6a = Entry(window).grid(row=row[0],column=6)
            r7exits7a = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects name").grid(row=row[0],column=0)
            r7objects1 = Entry(window).grid(row=row[0],column=1)
            r7objects1 = Entry(window).grid(row=row[0],column=1)
            r7objects2 = Entry(window).grid(row=row[0],column=2)
            Label(window, text="Door :").grid(row=row[0],column=3)
            Label(window, text="status").grid(row=row[0],column=4)
            Label(window, text="exit").grid(row=row[0],column=5)
            Label(window, text="locked").grid(row=row[0],column=6)
            Label(window, text="mapto").grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects desc").grid(row=row[0],column=0)
            r7objects1a = Entry(window).grid(row=row[0],column=1)
            r7objects2a = Entry(window).grid(row=row[0],column=2)
            r7doorstatus = Entry(window).grid(row=row[0],column=4)
            r7doorexit = Entry(window).grid(row=row[0],column=5)
            r7doorlocked = Entry(window).grid(row=row[0],column=6)
            r7doormapto = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text="-----------------").grid(row=row[0],column=1)
            Label(window, text="-----------------").grid(row=row[0],column=2)
            Label(window, text="-----------------").grid(row=row[0],column=3)
            Label(window, text="-----------------").grid(row=row[0],column=4)
            Label(window, text="-----------------").grid(row=row[0],column=5)
            Label(window, text="-----------------").grid(row=row[0],column=6)
            Label(window, text="-----------------").grid(row=row[0],column=7)
            row[0] += 1

        if roomamount[0] == 8:
            Label(window, text="room 8").grid(row=8,column=0)
            room8 = Entry(window).grid(row=8,column=1)
            name8 = Entry(window).grid(row=8,column=2)
            desc8 = Entry(window).grid(row=8,column=3)
            Label(window, text="Room 8 exits").grid(row=row[0],column=0)
            r8exits1 = Entry(window).grid(row=row[0],column=1)
            r8exits2 = Entry(window).grid(row=row[0],column=2)
            r8exits3 = Entry(window).grid(row=row[0],column=3)
            r8exits4 = Entry(window).grid(row=row[0],column=4)
            r8exits5 = Entry(window).grid(row=row[0],column=5)
            r8exits6 = Entry(window).grid(row=row[0],column=6)
            r8exits7 = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" destination").grid(row=row[0],column=0)
            r8exits1a = Entry(window).grid(row=row[0],column=1)
            r8exits2a = Entry(window).grid(row=row[0],column=2)
            r8exits3a = Entry(window).grid(row=row[0],column=3)
            r8exits4a = Entry(window).grid(row=row[0],column=4)
            r8exits5a = Entry(window).grid(row=row[0],column=5)
            r8exits6a = Entry(window).grid(row=row[0],column=6)
            r8exits7a = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects name").grid(row=row[0],column=0)
            r8objects1 = Entry(window).grid(row=row[0],column=1)
            r8objects1 = Entry(window).grid(row=row[0],column=1)
            r8objects2 = Entry(window).grid(row=row[0],column=2)
            Label(window, text="Door :").grid(row=row[0],column=3)
            Label(window, text="status").grid(row=row[0],column=4)
            Label(window, text="exit").grid(row=row[0],column=5)
            Label(window, text="locked").grid(row=row[0],column=6)
            Label(window, text="mapto").grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects desc").grid(row=row[0],column=0)
            r8objects1a = Entry(window).grid(row=row[0],column=1)
            r8objects2a = Entry(window).grid(row=row[0],column=2)
            r8doorstatus = Entry(window).grid(row=row[0],column=4)
            r8doorexit = Entry(window).grid(row=row[0],column=5)
            r8doorlocked = Entry(window).grid(row=row[0],column=6)
            r8doormapto = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text="-----------------").grid(row=row[0],column=1)
            Label(window, text="-----------------").grid(row=row[0],column=2)
            Label(window, text="-----------------").grid(row=row[0],column=3)
            Label(window, text="-----------------").grid(row=row[0],column=4)
            Label(window, text="-----------------").grid(row=row[0],column=5)
            Label(window, text="-----------------").grid(row=row[0],column=6)
            Label(window, text="-----------------").grid(row=row[0],column=7)
            row[0] += 1

        if roomamount[0] == 9:
            Label(window, text="room 9").grid(row=9,column=0)
            room9 = Entry(window).grid(row=9,column=1)
            name9 = Entry(window).grid(row=9,column=2)
            desc9 = Entry(window).grid(row=9,column=3)
            Label(window, text="Room 9 exits").grid(row=row[0],column=0)
            r9exits1 = Entry(window).grid(row=row[0],column=1)
            r9exits2 = Entry(window).grid(row=row[0],column=2)
            r9exits3 = Entry(window).grid(row=row[0],column=3)
            r9exits4 = Entry(window).grid(row=row[0],column=4)
            r9exits5 = Entry(window).grid(row=row[0],column=5)
            r9exits6 = Entry(window).grid(row=row[0],column=6)
            r9exits7 = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" destination").grid(row=row[0],column=0)
            r9exits1a = Entry(window).grid(row=row[0],column=1)
            r9exits2a = Entry(window).grid(row=row[0],column=2)
            r9exits3a = Entry(window).grid(row=row[0],column=3)
            r9exits4a = Entry(window).grid(row=row[0],column=4)
            r9exits5a = Entry(window).grid(row=row[0],column=5)
            r9exits6a = Entry(window).grid(row=row[0],column=6)
            r9exits7a = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects name").grid(row=row[0],column=0)
            r9objects1 = Entry(window).grid(row=row[0],column=1)
            r9objects1 = Entry(window).grid(row=row[0],column=1)
            r9objects2 = Entry(window).grid(row=row[0],column=2)
            Label(window, text="Door :").grid(row=row[0],column=3)
            Label(window, text="status").grid(row=row[0],column=4)
            Label(window, text="exit").grid(row=row[0],column=5)
            Label(window, text="locked").grid(row=row[0],column=6)
            Label(window, text="mapto").grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects desc").grid(row=row[0],column=0)
            r9objects1a = Entry(window).grid(row=row[0],column=1)
            r9objects2a = Entry(window).grid(row=row[0],column=2)
            r9doorstatus = Entry(window).grid(row=row[0],column=4)
            r9doorexit = Entry(window).grid(row=row[0],column=5)
            r9doorlocked = Entry(window).grid(row=row[0],column=6)
            r9doormapto = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text="-----------------").grid(row=row[0],column=1)
            Label(window, text="-----------------").grid(row=row[0],column=2)
            Label(window, text="-----------------").grid(row=row[0],column=3)
            Label(window, text="-----------------").grid(row=row[0],column=4)
            Label(window, text="-----------------").grid(row=row[0],column=5)
            Label(window, text="-----------------").grid(row=row[0],column=6)
            Label(window, text="-----------------").grid(row=row[0],column=7)
            row[0] += 1

        if roomamount[0] == 10:
            Label(window, text="room 10").grid(row=10,column=0)
            room10 = Entry(window).grid(row=10,column=1)
            name10 = Entry(window).grid(row=10,column=2)
            desc10 = Entry(window).grid(row=10,column=3)
            Label(window, text="Room 10 exits").grid(row=row[0],column=0)
            r10exits1 = Entry(window).grid(row=row[0],column=1)
            r10exits2 = Entry(window).grid(row=row[0],column=2)
            r10exits3 = Entry(window).grid(row=row[0],column=3)
            r10exits4 = Entry(window).grid(row=row[0],column=4)
            r10exits5 = Entry(window).grid(row=row[0],column=5)
            r10exits6 = Entry(window).grid(row=row[0],column=6)
            r10exits7 = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" destination").grid(row=row[0],column=0)
            r10exits1a = Entry(window).grid(row=row[0],column=1)
            r10exits2a = Entry(window).grid(row=row[0],column=2)
            r10exits3a = Entry(window).grid(row=row[0],column=3)
            r10exits4a = Entry(window).grid(row=row[0],column=4)
            r10exits5a = Entry(window).grid(row=row[0],column=5)
            r10exits6a = Entry(window).grid(row=row[0],column=6)
            r10exits7a = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects name").grid(row=row[0],column=0)
            r10objects1 = Entry(window).grid(row=row[0],column=1)
            r10objects1 = Entry(window).grid(row=row[0],column=1)
            r10objects2 = Entry(window).grid(row=row[0],column=2)
            Label(window, text="Door :").grid(row=row[0],column=3)
            Label(window, text="status").grid(row=row[0],column=4)
            Label(window, text="exit").grid(row=row[0],column=5)
            Label(window, text="locked").grid(row=row[0],column=6)
            Label(window, text="mapto").grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text=" objects desc").grid(row=row[0],column=0)
            r10objects1a = Entry(window).grid(row=row[0],column=1)
            r10objects2a = Entry(window).grid(row=row[0],column=2)
            r10doorstatus = Entry(window).grid(row=row[0],column=4)
            r10doorexit = Entry(window).grid(row=row[0],column=5)
            r10doorlocked = Entry(window).grid(row=row[0],column=6)
            r10doormapto = Entry(window).grid(row=row[0],column=7)
            row[0] += 1
            Label(window, text="-----------------").grid(row=row[0],column=1)
            Label(window, text="-----------------").grid(row=row[0],column=2)
            Label(window, text="-----------------").grid(row=row[0],column=3)
            Label(window, text="-----------------").grid(row=row[0],column=4)
            Label(window, text="-----------------").grid(row=row[0],column=5)
            Label(window, text="-----------------").grid(row=row[0],column=6)
            Label(window, text="-----------------").grid(row=row[0],column=7)
            row[0] += 1
    if generate[0] == 1:
        if file[0] == ' ':
            filetext.set("You need to select a save file")
        if file[0] != ' ':
            output = {}
            with open(file[0], 'w') as savefile:
                if roomamount[0] == 1:
                    output = {room1: {'name': name1, 'description': desc1, 'objects': {r1objects1: r1objects1a, r1objects2: r1objects2a}, 'exits': {r1exits1: r1exits1a, r1exits2: r1exits2a, r1exits3: r1exits3a, r1exits4: r1exits4a, r1exits5: r1exits5a, r1exits6: r1exits6a, r1exits7: r1exits7a, '': {'object': 'door', 'status': r1doorstatus, 'exits': r1doorexit, 'locked': r1doorlocked, 'mapto': r1doormapto}}}}
                if roomamount[0] == 2:
                    output = {room1: {'name': name1, 'description': desc1, 'objects': {r1objects1: r1objects1a, r1objects2: r1objects2a}, 'exits': {r1exits1: r1exits1a, r1exits2: r1exits2a, r1exits3: r1exits3a, r1exits4: r1exits4a, r1exits5: r1exits5a, r1exits6: r1exits6a, r1exits7: r1exits7a, '': {'object': 'door', 'status': r1doorstatus, 'exits': r1doorexit, 'locked': r1doorlocked, 'mapto': r1doormapto}}},room2: {'name': name2, 'description': desc2, 'objects': {r2objects1: r2objects1a, r2objects2: r2objects2a}, 'exits': {r2exits1: r2exits1a, r2exits2: r2exits2a, r2exits3: r2exits3a, r2exits4: r2exits4a, r2exits5: r2exits5a, r2exits6: r2exits6a, r2exits7: r2exits7a, '': {'object': 'door', 'status': r2doorstatus, 'exits': r2doorexit, 'locked': r2doorlocked, 'mapto': r2doormapto}}}}
                if roomamount[0] == 3:
                    output = {room1: {'name': name1, 'description': desc1, 'objects': {r1objects1: r1objects1a, r1objects2: r1objects2a}, 'exits': {r1exits1: r1exits1a, r1exits2: r1exits2a, r1exits3: r1exits3a, r1exits4: r1exits4a, r1exits5: r1exits5a, r1exits6: r1exits6a, r1exits7: r1exits7a, '': {'object': 'door', 'status': r1doorstatus, 'exits': r1doorexit, 'locked': r1doorlocked, 'mapto': r1doormapto}}},room2: {'name': name2, 'description': desc2, 'objects': {r2objects1: r2objects1a, r2objects2: r2objects2a}, 'exits': {r2exits1: r2exits1a, r2exits2: r2exits2a, r2exits3: r2exits3a, r2exits4: r2exits4a, r2exits5: r2exits5a, r2exits6: r2exits6a, r2exits7: r2exits7a, '': {'object': 'door', 'status': r2doorstatus, 'exits': r2doorexit, 'locked': r2doorlocked, 'mapto': r2doormapto}}},room3: {'name': name3, 'description': desc3, 'objects': {r3objects1: r3objects1a, r3objects2: r3objects2a}, 'exits': {r3exits1: r3exits1a, r3exits2: r3exits2a, r3exits3: r3exits3a, r3exits4: r3exits4a, r3exits5: r3exits5a, r3exits6: r3exits6a, r3exits7: r3exits7a, '': {'object': 'door', 'status': r3doorstatus, 'exits': r3doorexit, 'locked': r3doorlocked, 'mapto': r3doormapto}}}}
                if roomamount[0] == 4:
                    output = {room1: {'name': name1, 'description': desc1, 'objects': {r1objects1: r1objects1a, r1objects2: r1objects2a}, 'exits': {r1exits1: r1exits1a, r1exits2: r1exits2a, r1exits3: r1exits3a, r1exits4: r1exits4a, r1exits5: r1exits5a, r1exits6: r1exits6a, r1exits7: r1exits7a, '': {'object': 'door', 'status': r1doorstatus, 'exits': r1doorexit, 'locked': r1doorlocked, 'mapto': r1doormapto}}},room2: {'name': name2, 'description': desc2, 'objects': {r2objects1: r2objects1a, r2objects2: r2objects2a}, 'exits': {r2exits1: r2exits1a, r2exits2: r2exits2a, r2exits3: r2exits3a, r2exits4: r2exits4a, r2exits5: r2exits5a, r2exits6: r2exits6a, r2exits7: r2exits7a, '': {'object': 'door', 'status': r2doorstatus, 'exits': r2doorexit, 'locked': r2doorlocked, 'mapto': r2doormapto}}},room3: {'name': name3, 'description': desc3, 'objects': {r3objects1: r3objects1a, r3objects2: r3objects2a}, 'exits': {r3exits1: r3exits1a, r3exits2: r3exits2a, r3exits3: r3exits3a, r3exits4: r3exits4a, r3exits5: r3exits5a, r3exits6: r3exits6a, r3exits7: r3exits7a, '': {'object': 'door', 'status': r3doorstatus, 'exits': r3doorexit, 'locked': r3doorlocked, 'mapto': r3doormapto}}},room4: {'name': name4, 'description': desc4, 'objects': {r4objects1: r4objects1a, r4objects2: r4objects2a}, 'exits': {r4exits1: r4exits1a, r4exits2: r4exits2a, r4exits3: r4exits3a, r4exits4: r4exits4a, r4exits5: r4exits5a, r4exits6: r4exits6a, r4exits7: r4exits7a, '': {'object': 'door', 'status': r4doorstatus, 'exits': r4doorexit, 'locked': r4doorlocked, 'mapto': r4doormapto}}}}
                if roomamount[0] == 5:
                    output = {room1: {'name': name1, 'description': desc1, 'objects': {r1objects1: r1objects1a, r1objects2: r1objects2a}, 'exits': {r1exits1: r1exits1a, r1exits2: r1exits2a, r1exits3: r1exits3a, r1exits4: r1exits4a, r1exits5: r1exits5a, r1exits6: r1exits6a, r1exits7: r1exits7a, '': {'object': 'door', 'status': r1doorstatus, 'exits': r1doorexit, 'locked': r1doorlocked, 'mapto': r1doormapto}}},room2: {'name': name2, 'description': desc2, 'objects': {r2objects1: r2objects1a, r2objects2: r2objects2a}, 'exits': {r2exits1: r2exits1a, r2exits2: r2exits2a, r2exits3: r2exits3a, r2exits4: r2exits4a, r2exits5: r2exits5a, r2exits6: r2exits6a, r2exits7: r2exits7a, '': {'object': 'door', 'status': r2doorstatus, 'exits': r2doorexit, 'locked': r2doorlocked, 'mapto': r2doormapto}}},room3: {'name': name3, 'description': desc3, 'objects': {r3objects1: r3objects1a, r3objects2: r3objects2a}, 'exits': {r3exits1: r3exits1a, r3exits2: r3exits2a, r3exits3: r3exits3a, r3exits4: r3exits4a, r3exits5: r3exits5a, r3exits6: r3exits6a, r3exits7: r3exits7a, '': {'object': 'door', 'status': r3doorstatus, 'exits': r3doorexit, 'locked': r3doorlocked, 'mapto': r3doormapto}}},room4: {'name': name4, 'description': desc4, 'objects': {r4objects1: r4objects1a, r4objects2: r4objects2a}, 'exits': {r4exits1: r4exits1a, r4exits2: r4exits2a, r4exits3: r4exits3a, r4exits4: r4exits4a, r4exits5: r4exits5a, r4exits6: r4exits6a, r4exits7: r4exits7a, '': {'object': 'door', 'status': r4doorstatus, 'exits': r4doorexit, 'locked': r4doorlocked, 'mapto': r4doormapto}}},room5: {'name': name5, 'description': desc5, 'objects': {r5objects1: r5objects1a, r5objects2: r5objects2a}, 'exits': {r5exits1: r5exits1a, r5exits2: r5exits2a, r5exits3: r5exits3a, r5exits4: r5exits4a, r5exits5: r5exits5a, r5exits6: r5exits6a, r5exits7: r5exits7a, '': {'object': 'door', 'status': r5doorstatus, 'exits': r5doorexit, 'locked': r5doorlocked, 'mapto': r5doormapto}}}}
                if roomamount[0] == 6:
                    output = {room1: {'name': name1, 'description': desc1, 'objects': {r1objects1: r1objects1a, r1objects2: r1objects2a}, 'exits': {r1exits1: r1exits1a, r1exits2: r1exits2a, r1exits3: r1exits3a, r1exits4: r1exits4a, r1exits5: r1exits5a, r1exits6: r1exits6a, r1exits7: r1exits7a, '': {'object': 'door', 'status': r1doorstatus, 'exits': r1doorexit, 'locked': r1doorlocked, 'mapto': r1doormapto}}},room2: {'name': name2, 'description': desc2, 'objects': {r2objects1: r2objects1a, r2objects2: r2objects2a}, 'exits': {r2exits1: r2exits1a, r2exits2: r2exits2a, r2exits3: r2exits3a, r2exits4: r2exits4a, r2exits5: r2exits5a, r2exits6: r2exits6a, r2exits7: r2exits7a, '': {'object': 'door', 'status': r2doorstatus, 'exits': r2doorexit, 'locked': r2doorlocked, 'mapto': r2doormapto}}},room3: {'name': name3, 'description': desc3, 'objects': {r3objects1: r3objects1a, r3objects2: r3objects2a}, 'exits': {r3exits1: r3exits1a, r3exits2: r3exits2a, r3exits3: r3exits3a, r3exits4: r3exits4a, r3exits5: r3exits5a, r3exits6: r3exits6a, r3exits7: r3exits7a, '': {'object': 'door', 'status': r3doorstatus, 'exits': r3doorexit, 'locked': r3doorlocked, 'mapto': r3doormapto}}},room4: {'name': name4, 'description': desc4, 'objects': {r4objects1: r4objects1a, r4objects2: r4objects2a}, 'exits': {r4exits1: r4exits1a, r4exits2: r4exits2a, r4exits3: r4exits3a, r4exits4: r4exits4a, r4exits5: r4exits5a, r4exits6: r4exits6a, r4exits7: r4exits7a, '': {'object': 'door', 'status': r4doorstatus, 'exits': r4doorexit, 'locked': r4doorlocked, 'mapto': r4doormapto}}},room5: {'name': name5, 'description': desc5, 'objects': {r5objects1: r5objects1a, r5objects2: r5objects2a}, 'exits': {r5exits1: r5exits1a, r5exits2: r5exits2a, r5exits3: r5exits3a, r5exits4: r5exits4a, r5exits5: r5exits5a, r5exits6: r5exits6a, r5exits7: r5exits7a, '': {'object': 'door', 'status': r5doorstatus, 'exits': r5doorexit, 'locked': r5doorlocked, 'mapto': r5doormapto}}},room6: {'name': name6, 'description': desc6, 'objects': {r6objects1: r6objects1a, r6objects2: r6objects2a}, 'exits': {r6exits1: r6exits1a, r6exits2: r6exits2a, r6exits3: r6exits3a, r6exits4: r6exits4a, r6exits5: r6exits5a, r6exits6: r6exits6a, r6exits7: r6exits7a, '': {'object': 'door', 'status': r6doorstatus, 'exits': r6doorexit, 'locked': r6doorlocked, 'mapto': r6doormapto}}}}
                if roomamount[0] == 7:
                    output = {room1: {'name': name1, 'description': desc1, 'objects': {r1objects1: r1objects1a, r1objects2: r1objects2a}, 'exits': {r1exits1: r1exits1a, r1exits2: r1exits2a, r1exits3: r1exits3a, r1exits4: r1exits4a, r1exits5: r1exits5a, r1exits6: r1exits6a, r1exits7: r1exits7a, '': {'object': 'door', 'status': r1doorstatus, 'exits': r1doorexit, 'locked': r1doorlocked, 'mapto': r1doormapto}}},room2: {'name': name2, 'description': desc2, 'objects': {r2objects1: r2objects1a, r2objects2: r2objects2a}, 'exits': {r2exits1: r2exits1a, r2exits2: r2exits2a, r2exits3: r2exits3a, r2exits4: r2exits4a, r2exits5: r2exits5a, r2exits6: r2exits6a, r2exits7: r2exits7a, '': {'object': 'door', 'status': r2doorstatus, 'exits': r2doorexit, 'locked': r2doorlocked, 'mapto': r2doormapto}}},room3: {'name': name3, 'description': desc3, 'objects': {r3objects1: r3objects1a, r3objects2: r3objects2a}, 'exits': {r3exits1: r3exits1a, r3exits2: r3exits2a, r3exits3: r3exits3a, r3exits4: r3exits4a, r3exits5: r3exits5a, r3exits6: r3exits6a, r3exits7: r3exits7a, '': {'object': 'door', 'status': r3doorstatus, 'exits': r3doorexit, 'locked': r3doorlocked, 'mapto': r3doormapto}}},room4: {'name': name4, 'description': desc4, 'objects': {r4objects1: r4objects1a, r4objects2: r4objects2a}, 'exits': {r4exits1: r4exits1a, r4exits2: r4exits2a, r4exits3: r4exits3a, r4exits4: r4exits4a, r4exits5: r4exits5a, r4exits6: r4exits6a, r4exits7: r4exits7a, '': {'object': 'door', 'status': r4doorstatus, 'exits': r4doorexit, 'locked': r4doorlocked, 'mapto': r4doormapto}}},room5: {'name': name5, 'description': desc5, 'objects': {r5objects1: r5objects1a, r5objects2: r5objects2a}, 'exits': {r5exits1: r5exits1a, r5exits2: r5exits2a, r5exits3: r5exits3a, r5exits4: r5exits4a, r5exits5: r5exits5a, r5exits6: r5exits6a, r5exits7: r5exits7a, '': {'object': 'door', 'status': r5doorstatus, 'exits': r5doorexit, 'locked': r5doorlocked, 'mapto': r5doormapto}}},room6: {'name': name6, 'description': desc6, 'objects': {r6objects1: r6objects1a, r6objects2: r6objects2a}, 'exits': {r6exits1: r6exits1a, r6exits2: r6exits2a, r6exits3: r6exits3a, r6exits4: r6exits4a, r6exits5: r6exits5a, r6exits6: r6exits6a, r6exits7: r6exits7a, '': {'object': 'door', 'status': r6doorstatus, 'exits': r6doorexit, 'locked': r6doorlocked, 'mapto': r6doormapto}}},room7: {'name': name7, 'description': desc7, 'objects': {r7objects1: r7objects1a, r7objects2: r7objects2a}, 'exits': {r7exits1: r7exits1a, r7exits2: r7exits2a, r7exits3: r7exits3a, r7exits4: r7exits4a, r7exits5: r7exits5a, r7exits6: r7exits6a, r7exits7: r7exits7a, '': {'object': 'door', 'status': r7doorstatus, 'exits': r7doorexit, 'locked': r7doorlocked, 'mapto': r7doormapto}}}}
                if roomamount[0] == 8:
                    output = {room1: {'name': name1, 'description': desc1, 'objects': {r1objects1: r1objects1a, r1objects2: r1objects2a}, 'exits': {r1exits1: r1exits1a, r1exits2: r1exits2a, r1exits3: r1exits3a, r1exits4: r1exits4a, r1exits5: r1exits5a, r1exits6: r1exits6a, r1exits7: r1exits7a, '': {'object': 'door', 'status': r1doorstatus, 'exits': r1doorexit, 'locked': r1doorlocked, 'mapto': r1doormapto}}},room2: {'name': name2, 'description': desc2, 'objects': {r2objects1: r2objects1a, r2objects2: r2objects2a}, 'exits': {r2exits1: r2exits1a, r2exits2: r2exits2a, r2exits3: r2exits3a, r2exits4: r2exits4a, r2exits5: r2exits5a, r2exits6: r2exits6a, r2exits7: r2exits7a, '': {'object': 'door', 'status': r2doorstatus, 'exits': r2doorexit, 'locked': r2doorlocked, 'mapto': r2doormapto}}},room3: {'name': name3, 'description': desc3, 'objects': {r3objects1: r3objects1a, r3objects2: r3objects2a}, 'exits': {r3exits1: r3exits1a, r3exits2: r3exits2a, r3exits3: r3exits3a, r3exits4: r3exits4a, r3exits5: r3exits5a, r3exits6: r3exits6a, r3exits7: r3exits7a, '': {'object': 'door', 'status': r3doorstatus, 'exits': r3doorexit, 'locked': r3doorlocked, 'mapto': r3doormapto}}},room4: {'name': name4, 'description': desc4, 'objects': {r4objects1: r4objects1a, r4objects2: r4objects2a}, 'exits': {r4exits1: r4exits1a, r4exits2: r4exits2a, r4exits3: r4exits3a, r4exits4: r4exits4a, r4exits5: r4exits5a, r4exits6: r4exits6a, r4exits7: r4exits7a, '': {'object': 'door', 'status': r4doorstatus, 'exits': r4doorexit, 'locked': r4doorlocked, 'mapto': r4doormapto}}},room5: {'name': name5, 'description': desc5, 'objects': {r5objects1: r5objects1a, r5objects2: r5objects2a}, 'exits': {r5exits1: r5exits1a, r5exits2: r5exits2a, r5exits3: r5exits3a, r5exits4: r5exits4a, r5exits5: r5exits5a, r5exits6: r5exits6a, r5exits7: r5exits7a, '': {'object': 'door', 'status': r5doorstatus, 'exits': r5doorexit, 'locked': r5doorlocked, 'mapto': r5doormapto}}},room6: {'name': name6, 'description': desc6, 'objects': {r6objects1: r6objects1a, r6objects2: r6objects2a}, 'exits': {r6exits1: r6exits1a, r6exits2: r6exits2a, r6exits3: r6exits3a, r6exits4: r6exits4a, r6exits5: r6exits5a, r6exits6: r6exits6a, r6exits7: r6exits7a, '': {'object': 'door', 'status': r6doorstatus, 'exits': r6doorexit, 'locked': r6doorlocked, 'mapto': r6doormapto}}},room7: {'name': name7, 'description': desc7, 'objects': {r7objects1: r7objects1a, r7objects2: r7objects2a}, 'exits': {r7exits1: r7exits1a, r7exits2: r7exits2a, r7exits3: r7exits3a, r7exits4: r7exits4a, r7exits5: r7exits5a, r7exits6: r7exits6a, r7exits7: r7exits7a, '': {'object': 'door', 'status': r7doorstatus, 'exits': r7doorexit, 'locked': r7doorlocked, 'mapto': r7doormapto}}},room8: {'name': name8, 'description': desc8, 'objects': {r8objects1: r8objects1a, r8objects2: r8objects2a}, 'exits': {r8exits1: r8exits1a, r8exits2: r8exits2a, r8exits3: r8exits3a, r8exits4: r8exits4a, r8exits5: r8exits5a, r8exits6: r8exits6a, r8exits7: r8exits7a, '': {'object': 'door', 'status': r8doorstatus, 'exits': r8doorexit, 'locked': r8doorlocked, 'mapto': r8doormapto}}}}
                if roomamount[0] == 9:
                    output = {room1: {'name': name1, 'description': desc1, 'objects': {r1objects1: r1objects1a, r1objects2: r1objects2a}, 'exits': {r1exits1: r1exits1a, r1exits2: r1exits2a, r1exits3: r1exits3a, r1exits4: r1exits4a, r1exits5: r1exits5a, r1exits6: r1exits6a, r1exits7: r1exits7a, '': {'object': 'door', 'status': r1doorstatus, 'exits': r1doorexit, 'locked': r1doorlocked, 'mapto': r1doormapto}}},room2: {'name': name2, 'description': desc2, 'objects': {r2objects1: r2objects1a, r2objects2: r2objects2a}, 'exits': {r2exits1: r2exits1a, r2exits2: r2exits2a, r2exits3: r2exits3a, r2exits4: r2exits4a, r2exits5: r2exits5a, r2exits6: r2exits6a, r2exits7: r2exits7a, '': {'object': 'door', 'status': r2doorstatus, 'exits': r2doorexit, 'locked': r2doorlocked, 'mapto': r2doormapto}}},room3: {'name': name3, 'description': desc3, 'objects': {r3objects1: r3objects1a, r3objects2: r3objects2a}, 'exits': {r3exits1: r3exits1a, r3exits2: r3exits2a, r3exits3: r3exits3a, r3exits4: r3exits4a, r3exits5: r3exits5a, r3exits6: r3exits6a, r3exits7: r3exits7a, '': {'object': 'door', 'status': r3doorstatus, 'exits': r3doorexit, 'locked': r3doorlocked, 'mapto': r3doormapto}}},room4: {'name': name4, 'description': desc4, 'objects': {r4objects1: r4objects1a, r4objects2: r4objects2a}, 'exits': {r4exits1: r4exits1a, r4exits2: r4exits2a, r4exits3: r4exits3a, r4exits4: r4exits4a, r4exits5: r4exits5a, r4exits6: r4exits6a, r4exits7: r4exits7a, '': {'object': 'door', 'status': r4doorstatus, 'exits': r4doorexit, 'locked': r4doorlocked, 'mapto': r4doormapto}}},room5: {'name': name5, 'description': desc5, 'objects': {r5objects1: r5objects1a, r5objects2: r5objects2a}, 'exits': {r5exits1: r5exits1a, r5exits2: r5exits2a, r5exits3: r5exits3a, r5exits4: r5exits4a, r5exits5: r5exits5a, r5exits6: r5exits6a, r5exits7: r5exits7a, '': {'object': 'door', 'status': r5doorstatus, 'exits': r5doorexit, 'locked': r5doorlocked, 'mapto': r5doormapto}}},room6: {'name': name6, 'description': desc6, 'objects': {r6objects1: r6objects1a, r6objects2: r6objects2a}, 'exits': {r6exits1: r6exits1a, r6exits2: r6exits2a, r6exits3: r6exits3a, r6exits4: r6exits4a, r6exits5: r6exits5a, r6exits6: r6exits6a, r6exits7: r6exits7a, '': {'object': 'door', 'status': r6doorstatus, 'exits': r6doorexit, 'locked': r6doorlocked, 'mapto': r6doormapto}}},room7: {'name': name7, 'description': desc7, 'objects': {r7objects1: r7objects1a, r7objects2: r7objects2a}, 'exits': {r7exits1: r7exits1a, r7exits2: r7exits2a, r7exits3: r7exits3a, r7exits4: r7exits4a, r7exits5: r7exits5a, r7exits6: r7exits6a, r7exits7: r7exits7a, '': {'object': 'door', 'status': r7doorstatus, 'exits': r7doorexit, 'locked': r7doorlocked, 'mapto': r7doormapto}}},room8: {'name': name8, 'description': desc8, 'objects': {r8objects1: r8objects1a, r8objects2: r8objects2a}, 'exits': {r8exits1: r8exits1a, r8exits2: r8exits2a, r8exits3: r8exits3a, r8exits4: r8exits4a, r8exits5: r8exits5a, r8exits6: r8exits6a, r8exits7: r8exits7a, '': {'object': 'door', 'status': r8doorstatus, 'exits': r8doorexit, 'locked': r8doorlocked, 'mapto': r8doormapto}}},room9: {'name': name9, 'description': desc9, 'objects': {r9objects1: r9objects1a, r9objects2: r9objects2a}, 'exits': {r9exits1: r9exits1a, r9exits2: r9exits2a, r9exits3: r9exits3a, r9exits4: r9exits4a, r9exits5: r9exits5a, r9exits6: r9exits6a, r9exits7: r9exits7a, '': {'object': 'door', 'status': r9doorstatus, 'exits': r9doorexit, 'locked': r9doorlocked, 'mapto': r9doormapto}}}}
                if roomamount[0] == 10:
                    output = {room1: {'name': name1, 'description': desc1, 'objects': {r1objects1: r1objects1a, r1objects2: r1objects2a}, 'exits': {r1exits1: r1exits1a, r1exits2: r1exits2a, r1exits3: r1exits3a, r1exits4: r1exits4a, r1exits5: r1exits5a, r1exits6: r1exits6a, r1exits7: r1exits7a, '': {'object': 'door', 'status': r1doorstatus, 'exits': r1doorexit, 'locked': r1doorlocked, 'mapto': r1doormapto}}},room2: {'name': name2, 'description': desc2, 'objects': {r2objects1: r2objects1a, r2objects2: r2objects2a}, 'exits': {r2exits1: r2exits1a, r2exits2: r2exits2a, r2exits3: r2exits3a, r2exits4: r2exits4a, r2exits5: r2exits5a, r2exits6: r2exits6a, r2exits7: r2exits7a, '': {'object': 'door', 'status': r2doorstatus, 'exits': r2doorexit, 'locked': r2doorlocked, 'mapto': r2doormapto}}},room3: {'name': name3, 'description': desc3, 'objects': {r3objects1: r3objects1a, r3objects2: r3objects2a}, 'exits': {r3exits1: r3exits1a, r3exits2: r3exits2a, r3exits3: r3exits3a, r3exits4: r3exits4a, r3exits5: r3exits5a, r3exits6: r3exits6a, r3exits7: r3exits7a, '': {'object': 'door', 'status': r3doorstatus, 'exits': r3doorexit, 'locked': r3doorlocked, 'mapto': r3doormapto}}},room4: {'name': name4, 'description': desc4, 'objects': {r4objects1: r4objects1a, r4objects2: r4objects2a}, 'exits': {r4exits1: r4exits1a, r4exits2: r4exits2a, r4exits3: r4exits3a, r4exits4: r4exits4a, r4exits5: r4exits5a, r4exits6: r4exits6a, r4exits7: r4exits7a, '': {'object': 'door', 'status': r4doorstatus, 'exits': r4doorexit, 'locked': r4doorlocked, 'mapto': r4doormapto}}},room5: {'name': name5, 'description': desc5, 'objects': {r5objects1: r5objects1a, r5objects2: r5objects2a}, 'exits': {r5exits1: r5exits1a, r5exits2: r5exits2a, r5exits3: r5exits3a, r5exits4: r5exits4a, r5exits5: r5exits5a, r5exits6: r5exits6a, r5exits7: r5exits7a, '': {'object': 'door', 'status': r5doorstatus, 'exits': r5doorexit, 'locked': r5doorlocked, 'mapto': r5doormapto}}},room6: {'name': name6, 'description': desc6, 'objects': {r6objects1: r6objects1a, r6objects2: r6objects2a}, 'exits': {r6exits1: r6exits1a, r6exits2: r6exits2a, r6exits3: r6exits3a, r6exits4: r6exits4a, r6exits5: r6exits5a, r6exits6: r6exits6a, r6exits7: r6exits7a, '': {'object': 'door', 'status': r6doorstatus, 'exits': r6doorexit, 'locked': r6doorlocked, 'mapto': r6doormapto}}},room7: {'name': name7, 'description': desc7, 'objects': {r7objects1: r7objects1a, r7objects2: r7objects2a}, 'exits': {r7exits1: r7exits1a, r7exits2: r7exits2a, r7exits3: r7exits3a, r7exits4: r7exits4a, r7exits5: r7exits5a, r7exits6: r7exits6a, r7exits7: r7exits7a, '': {'object': 'door', 'status': r7doorstatus, 'exits': r7doorexit, 'locked': r7doorlocked, 'mapto': r7doormapto}}},room8: {'name': name8, 'description': desc8, 'objects': {r8objects1: r8objects1a, r8objects2: r8objects2a}, 'exits': {r8exits1: r8exits1a, r8exits2: r8exits2a, r8exits3: r8exits3a, r8exits4: r8exits4a, r8exits5: r8exits5a, r8exits6: r8exits6a, r8exits7: r8exits7a, '': {'object': 'door', 'status': r8doorstatus, 'exits': r8doorexit, 'locked': r8doorlocked, 'mapto': r8doormapto}}},room9: {'name': name9, 'description': desc9, 'objects': {r9objects1: r9objects1a, r9objects2: r9objects2a}, 'exits': {r9exits1: r9exits1a, r9exits2: r9exits2a, r9exits3: r9exits3a, r9exits4: r9exits4a, r9exits5: r9exits5a, r9exits6: r9exits6a, r9exits7: r9exits7a, '': {'object': 'door', 'status': r9doorstatus, 'exits': r9doorexit, 'locked': r9doorlocked, 'mapto': r9doormapto}}},room10: {'name': name10, 'description': desc10, 'objects': {r10objects1: r10objects1a, r10objects2: r10objects2a}, 'exits': {r10exits1: r10exits1a, r10exits2: r10exits2a, r10exits3: r10exits3a, r10exits4: r10exits4a, r10exits5: r10exits5a, r10exits6: r10exits6a, r10exits7: r10exits7a, '': {'object': 'door', 'status': r10doorstatus, 'exits': r10doorexit, 'locked': r10doorlocked, 'mapto': r10doormapto}}}}
                json.dump(output, savefile, indent=4, sort_keys=True)
                print("dumped :  "+str(output)+"  to file "+str(savefile))


def Generate():
    generate[0] = 1
    AddRoom()
    generate[0] = 0

def OpenFileBrowse():
    file[0] = filedialog.asksaveasfilename(parent=window,title='Create a json file')
    filetext.set(str(file[0]))


generate = [0]
roomamount = [1]
row = [17, 0]
file = [" "]

filetext = StringVar()
Label(window, textvariable=str(filetext)).grid(row=1,column=5)
filetext.set(str(file[0]))
##
AddRoom()

#draw the window, and start the 'application'
window.mainloop()
