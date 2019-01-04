import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import json

class App(QMainWindow):
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.filename.text()
        roomstodo = 0
        readytocreate = 0
        output = {}
        if self.room1.text() != '' and self.room2.text() == '' and self.room3.text() == '' and self.room4.text() == '' and self.room5.text() == '':
            roomstodo = 1
        if self.room1.text() != '' and self.room2.text() != '' and self.room3.text() == '' and self.room4.text() == '' and self.room5.text() == '':
            roomstodo = 2
        if self.room1.text() != '' and self.room2.text() != '' and self.room3.text() != '' and self.room4.text() == '' and self.room5.text() == '':
            roomstodo = 3
        if self.room1.text() != '' and self.room2.text() != '' and self.room3.text() != '' and self.room4.text() != '' and self.room5.text() == '':
            roomstodo = 4
        if self.room1.text() != '' and self.room2.text() != '' and self.room3.text() != '' and self.room4.text() != '' and self.room5.text() != '':
            roomstodo = 5

        if textboxValue == '' and self.room1.text() == '':
            QMessageBox.question(self, 'Map failed', "Please input a filename and create at least one room", QMessageBox.Ok, QMessageBox.Ok)
        elif textboxValue != '' and self.room1.text() == '':
            QMessageBox.question(self, 'Map failed', "Please create at least one room", QMessageBox.Ok, QMessageBox.Ok)
        elif textboxValue == '':
            QMessageBox.question(self, 'Map failed', "Please input a filename", QMessageBox.Ok, QMessageBox.Ok)
        else:
            readytocreate = 1
        if readytocreate == 1:
            if roomstodo == 1:
                output = {self.room1.text(): {'name': self.room1.text(), 'description': self.desc1.text(), 'objects': {self.object1.text(): self.objectv1.text(), self.objectb1.text(): self.objectbv1.text()}, 'exits': {self.rmexita1.text(): self.rmexitb1.text(), self.rmexitc1.text(): self.rmexitd1.text(), self.rmexite1.text(): self.rmexitf1.text(), self.rmexitg1.text(): self.rmexith1.text(), '': {'object': 'door', 'status': self.status1.text(), 'exits': self.exit1.text(), 'locked': self.locked1.text(), 'mapto': self.mapto1.text()}}}}
            if roomstodo == 2:
                output = {self.room1.text(): {'name': self.room1.text(), 'description': self.desc1.text(), 'objects': {self.object1.text(): self.objectv1.text(), self.objectb1.text(): self.objectbv1.text()}, 'exits': {self.rmexita1.text(): self.rmexitb1.text(), self.rmexitc1.text(): self.rmexitd1.text(), self.rmexite1.text(): self.rmexitf1.text(), self.rmexitg1.text(): self.rmexith1.text(), '': {'object': 'door', 'status': self.status1.text(), 'exits': self.exit1.text(), 'locked': self.locked1.text(), 'mapto': self.mapto1.text()}}},self.room2.text(): {'name': self.room2.text(), 'description': self.desc2.text(), 'objects': {self.object2.text(): self.objectv2.text(), self.objectb2.text(): self.objectbv2.text()}, 'exits': {self.rmexita2.text(): self.rmexitb2.text(), self.rmexitc2.text(): self.rmexitd2.text(), self.rmexite2.text(): self.rmexitf2.text(), self.rmexitg2.text(): self.rmexith2.text(), '': {'object': 'door', 'status': self.status2.text(), 'exits': self.exit2.text(), 'locked': self.locked2.text(), 'mapto': self.mapto2.text()}}}}
            if roomstodo == 3:
                output = {self.room1: {'name': self.room1, 'description': self.desc1, 'objects': {self.object1: self.objectv1, self.objectb1: self.objectbv1}, 'exits': {self.rmexita1: self.rmexitb1, self.rmexitc1: self.rmexitd1, self.rmexite1: self.rmexitf1, self.rmexitg1: self.rmexith1, '': {'object': 'door', 'status': self.status1, 'exits': self.exit1, 'locked': self.locked1, 'mapto': self.mapto1}}},self.room2: {'name': self.room2, 'description': self.desc2, 'objects': {self.object2: self.objectv2, self.objectb2: self.objectbv2}, 'exits': {self.rmexita2: self.rmexitb2, self.rmexitc2: self.rmexitd2, self.rmexite2: self.rmexitf2, self.rmexitg2: self.rmexith2, '': {'object': 'door', 'status': self.status2, 'exits': self.exit2, 'locked': self.locked2, 'mapto': self.mapto2}}},self.room3: {'name': self.room3, 'description': self.desc3, 'objects': {self.object3: self.objectv3, self.objectb3: self.objectbv3}, 'exits': {self.rmexita3: self.rmexitb3, self.rmexitc3: self.rmexitd3, self.rmexite3: self.rmexitf3, self.rmexitg3: self.rmexith3, '': {'object': 'door', 'status': self.status3, 'exits': self.exit3, 'locked': self.locked3, 'mapto': self.mapto3}}}}
            if roomstodo == 4:
                output = {self.room1.text(): {'name': self.room1.text(), 'description': self.desc1.text(), 'objects': {self.object1.text(): self.objectv1.text(), self.objectb1.text(): self.objectbv1.text()}, 'exits': {self.rmexita1.text(): self.rmexitb1.text(), self.rmexitc1.text(): self.rmexitd1.text(), self.rmexite1.text(): self.rmexitf1.text(), self.rmexitg1.text(): self.rmexith1.text(), '': {'object': 'door', 'status': self.status1.text(), 'exits': self.exit1.text(), 'locked': self.locked1.text(), 'mapto': self.mapto1.text()}}},self.room2.text(): {'name': self.room2.text(), 'description': self.desc2.text(), 'objects': {self.object2.text(): self.objectv2.text(), self.objectb2.text(): self.objectbv2.text()}, 'exits': {self.rmexita2.text(): self.rmexitb2.text(), self.rmexitc2.text(): self.rmexitd2.text(), self.rmexite2.text(): self.rmexitf2.text(), self.rmexitg2.text(): self.rmexith2.text(), '': {'object': 'door', 'status': self.status2.text(), 'exits': self.exit2.text(), 'locked': self.locked2.text(), 'mapto': self.mapto2.text()}}},self.room3.text(): {'name': self.room3.text(), 'description': self.desc3.text(), 'objects': {self.object3.text(): self.objectv3.text(), self.objectb3.text(): self.objectbv3.text()}, 'exits': {self.rmexita3.text(): self.rmexitb3.text(), self.rmexitc3.text(): self.rmexitd3.text(), self.rmexite3.text(): self.rmexitf3.text(), self.rmexitg3.text(): self.rmexith3.text(), '': {'object': 'door', 'status': self.status3.text(), 'exits': self.exit3.text(), 'locked': self.locked3.text(), 'mapto': self.mapto3.text()}}},self.room4.text(): {'name': self.room4.text(), 'description': self.desc4.text(), 'objects': {self.object4.text(): self.objectv4.text(), self.objectb4.text(): self.objectbv4.text()}, 'exits': {self.rmexita4.text(): self.rmexitb4.text(), self.rmexitc4.text(): self.rmexitd4.text(), self.rmexite4.text(): self.rmexitf4.text(), self.rmexitg4.text(): self.rmexith4.text(), '': {'object': 'door', 'status': self.status4.text(), 'exits': self.exit4.text(), 'locked': self.locked4.text(), 'mapto': self.mapto4.text()}}}}
            if roomstodo == 5:
                output = {self.room1.text(): {'name': self.room1.text(), 'description': self.desc1.text(), 'objects': {self.object1.text(): self.objectv1.text(), self.objectb1.text(): self.objectbv1.text()}, 'exits': {self.rmexita1.text(): self.rmexitb1.text(), self.rmexitc1.text(): self.rmexitd1.text(), self.rmexite1.text(): self.rmexitf1.text(), self.rmexitg1.text(): self.rmexith1.text(), '': {'object': 'door', 'status': self.status1.text(), 'exits': self.exit1.text(), 'locked': self.locked1.text(), 'mapto': self.mapto1.text()}}},self.room2.text(): {'name': self.room2.text(), 'description': self.desc2.text(), 'objects': {self.object2.text(): self.objectv2.text(), self.objectb2.text(): self.objectbv2.text()}, 'exits': {self.rmexita2.text(): self.rmexitb2.text(), self.rmexitc2.text(): self.rmexitd2.text(), self.rmexite2.text(): self.rmexitf2.text(), self.rmexitg2.text(): self.rmexith2.text(), '': {'object': 'door', 'status': self.status2.text(), 'exits': self.exit2.text(), 'locked': self.locked2.text(), 'mapto': self.mapto2.text()}}},self.room3.text(): {'name': self.room3.text(), 'description': self.desc3.text(), 'objects': {self.object3.text(): self.objectv3.text(), self.objectb3.text(): self.objectbv3.text()}, 'exits': {self.rmexita3.text(): self.rmexitb3.text(), self.rmexitc3.text(): self.rmexitd3.text(), self.rmexite3.text(): self.rmexitf3.text(), self.rmexitg3.text(): self.rmexith3.text(), '': {'object': 'door', 'status': self.status3.text(), 'exits': self.exit3.text(), 'locked': self.locked3.text(), 'mapto': self.mapto3.text()}}},self.room4.text(): {'name': self.room4.text(), 'description': self.desc4.text(), 'objects': {self.object4.text(): self.objectv4.text(), self.objectb4.text(): self.objectbv4.text()}, 'exits': {self.rmexita4.text(): self.rmexitb4.text(), self.rmexitc4.text(): self.rmexitd4.text(), self.rmexite4.text(): self.rmexitf4.text(), self.rmexitg4.text(): self.rmexith4.text(), '': {'object': 'door', 'status': self.status4.text(), 'exits': self.exit4.text(), 'locked': self.locked4.text(), 'mapto': self.mapto4.text()}}},self.room5.text(): {'name': self.room5.text(), 'description': self.desc5.text(), 'objects': {self.object5.text(): self.objectv5.text(), self.objectb5.text(): self.objectbv5.text()}, 'exits': {self.rmexita5.text(): self.rmexitb5.text(), self.rmexitc5.text(): self.rmexitd5.text(), self.rmexite5.text(): self.rmexitf5.text(), self.rmexitg5.text(): self.rmexith5.text(), '': {'object': 'door', 'status': self.status5.text(), 'exits': self.exit5.text(), 'locked': self.locked5.text(), 'mapto': self.mapto5.text()}}}}

            if output == {}:
                QMessageBox.question(self, 'Failed', str(roomstodo) + " lets try filling out all the boxes", QMessageBox.Ok, QMessageBox.Ok)
            else:
                open(self.filename.text(), 'a').close()
                with open(str("Maps/")+str(self.filename.text()), "w") as savefile:
                    json.dump(output, savefile, indent=4, sort_keys=True)
                QMessageBox.question(self, 'Generated map', str(roomstodo) + " Maps created, saved to 'Maps/" + textboxValue+"'", QMessageBox.Ok, QMessageBox.Ok)

    def __init__(self):
        super().__init__()
        self.title = 'MapBuilder'
        self.left = 10
        self.top = 10
        self.width = 1150
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        padding = 10
        boxh = 40
        boxw = 100

        roomlabel = QLabel('Room', self)
        roomlabel.move(padding*3,10)
        self.room1 = QLineEdit(self)
        self.room1.move(padding, 40)
        self.room1.resize(boxw,boxh)
        self.room2 = QLineEdit(self)
        self.room2.move(padding, 90)
        self.room2.resize(boxw,boxh)
        self.room3 = QLineEdit(self)
        self.room3.move(padding, 140)
        self.room3.resize(boxw,boxh)
        self.room4 = QLineEdit(self)
        self.room4.move(padding, 190)
        self.room4.resize(boxw,boxh)
        self.room5 = QLineEdit(self)
        self.room5.move(padding, 240)
        self.room5.resize(boxw,boxh)
        padding = padding+10+boxw
        desclabel = QLabel('Description', self)
        desclabel.move(padding+5,10)
        self.desc1 = QLineEdit(self)
        self.desc1.move(padding, 40)
        self.desc1.resize(boxw,boxh)
        self.desc2 = QLineEdit(self)
        self.desc2.move(padding, 90)
        self.desc2.resize(boxw,boxh)
        self.desc3 = QLineEdit(self)
        self.desc3.move(padding, 140)
        self.desc3.resize(boxw,boxh)
        self.desc4 = QLineEdit(self)
        self.desc4.move(padding, 190)
        self.desc4.resize(boxw,boxh)
        self.desc5 = QLineEdit(self)
        self.desc5.move(padding, 240)
        self.desc5.resize(boxw,boxh)

        padding = padding+10+boxw
        objectlabel = QLabel('Objects name', self)
        objectlabel.move(padding+5,10)
        self.object1 = QLineEdit(self)
        self.object1.move(padding, 40)
        self.object1.resize(boxw,boxh)
        self.object2 = QLineEdit(self)
        self.object2.move(padding, 90)
        self.object2.resize(boxw,boxh)
        self.object3 = QLineEdit(self)
        self.object3.move(padding, 140)
        self.object3.resize(boxw,boxh)
        self.object4 = QLineEdit(self)
        self.object4.move(padding, 190)
        self.object4.resize(boxw,boxh)
        self.object5 = QLineEdit(self)
        self.object5.move(padding, 240)
        self.object5.resize(boxw,boxh)

        padding = padding+10+boxw
        objectvlabel = QLabel('Objects value', self)
        objectvlabel.move(padding+5,10)
        self.objectv1 = QLineEdit(self)
        self.objectv1.move(padding, 40)
        self.objectv1.resize(boxw,boxh)
        self.objectv2 = QLineEdit(self)
        self.objectv2.move(padding, 90)
        self.objectv2.resize(boxw,boxh)
        self.objectv3 = QLineEdit(self)
        self.objectv3.move(padding, 140)
        self.objectv3.resize(boxw,boxh)
        self.objectv4 = QLineEdit(self)
        self.objectv4.move(padding, 190)
        self.objectv4.resize(boxw,boxh)
        self.objectv5 = QLineEdit(self)
        self.objectv5.move(padding, 240)
        self.objectv5.resize(boxw,boxh)

        padding = padding+10+boxw
        objectblabel = QLabel('Object2 name', self)
        objectblabel.move(padding+5,10)
        self.objectb1 = QLineEdit(self)
        self.objectb1.move(padding, 40)
        self.objectb1.resize(boxw,boxh)
        self.objectb2 = QLineEdit(self)
        self.objectb2.move(padding, 90)
        self.objectb2.resize(boxw,boxh)
        self.objectb3 = QLineEdit(self)
        self.objectb3.move(padding, 140)
        self.objectb3.resize(boxw,boxh)
        self.objectb4 = QLineEdit(self)
        self.objectb4.move(padding, 190)
        self.objectb4.resize(boxw,boxh)
        self.objectb5 = QLineEdit(self)
        self.objectb5.move(padding, 240)
        self.objectb5.resize(boxw,boxh)

        padding = padding+10+boxw
        objectbvlabel = QLabel('Object2 value', self)
        objectbvlabel.move(padding+5,10)
        self.objectbv1 = QLineEdit(self)
        self.objectbv1.move(padding, 40)
        self.objectbv1.resize(boxw,boxh)
        self.objectbv2 = QLineEdit(self)
        self.objectbv2.move(padding, 90)
        self.objectbv2.resize(boxw,boxh)
        self.objectbv3 = QLineEdit(self)
        self.objectbv3.move(padding, 140)
        self.objectbv3.resize(boxw,boxh)
        self.objectbv4 = QLineEdit(self)
        self.objectbv4.move(padding, 190)
        self.objectbv4.resize(boxw,boxh)
        self.objectbv5 = QLineEdit(self)
        self.objectbv5.move(padding, 240)
        self.objectbv5.resize(boxw,boxh)

        padding = padding+10+boxw
        statuslabel = QLabel('Door status', self)
        statuslabel.move(padding+5,10)
        self.status1 = QLineEdit(self)
        self.status1.move(padding, 40)
        self.status1.resize(boxw,boxh)
        self.status2 = QLineEdit(self)
        self.status2.move(padding, 90)
        self.status2.resize(boxw,boxh)
        self.status3 = QLineEdit(self)
        self.status3.move(padding, 140)
        self.status3.resize(boxw,boxh)
        self.status4 = QLineEdit(self)
        self.status4.move(padding, 190)
        self.status4.resize(boxw,boxh)
        self.status5 = QLineEdit(self)
        self.status5.move(padding, 240)
        self.status5.resize(boxw,boxh)

        padding = padding+10+boxw
        exitlabel = QLabel('exit', self)
        exitlabel.move(padding+5,10)
        self.exit1 = QLineEdit(self)
        self.exit1.move(padding, 40)
        self.exit1.resize(boxw,boxh)
        self.exit2 = QLineEdit(self)
        self.exit2.move(padding, 90)
        self.exit2.resize(boxw,boxh)
        self.exit3 = QLineEdit(self)
        self.exit3.move(padding, 140)
        self.exit3.resize(boxw,boxh)
        self.exit4 = QLineEdit(self)
        self.exit4.move(padding, 190)
        self.exit4.resize(boxw,boxh)
        self.exit5 = QLineEdit(self)
        self.exit5.move(padding, 240)
        self.exit5.resize(boxw,boxh)

        padding = padding+10+boxw
        lockedlabel = QLabel('locked', self)
        lockedlabel.move(padding+5,10)
        self.locked1 = QLineEdit(self)
        self.locked1.move(padding, 40)
        self.locked1.resize(boxw,boxh)
        self.locked2 = QLineEdit(self)
        self.locked2.move(padding, 90)
        self.locked2.resize(boxw,boxh)
        self.locked3 = QLineEdit(self)
        self.locked3.move(padding, 140)
        self.locked3.resize(boxw,boxh)
        self.locked4 = QLineEdit(self)
        self.locked4.move(padding, 190)
        self.locked4.resize(boxw,boxh)
        self.locked5 = QLineEdit(self)
        self.locked5.move(padding, 240)
        self.locked5.resize(boxw,boxh)

        padding = padding+10+boxw
        maptolabel = QLabel('mapto', self)
        maptolabel.move(padding+5,10)
        self.mapto1 = QLineEdit(self)
        self.mapto1.move(padding, 40)
        self.mapto1.resize(boxw,boxh)
        self.mapto2 = QLineEdit(self)
        self.mapto2.move(padding, 90)
        self.mapto2.resize(boxw,boxh)
        self.mapto3 = QLineEdit(self)
        self.mapto3.move(padding, 140)
        self.mapto3.resize(boxw,boxh)
        self.mapto4 = QLineEdit(self)
        self.mapto4.move(padding, 190)
        self.mapto4.resize(boxw,boxh)
        self.mapto5 = QLineEdit(self)
        self.mapto5.move(padding, 240)
        self.mapto5.resize(boxw,boxh)

        padding = 100
        roomexitslabel = QLabel(' Room Exits', self)
        roomexitslabel.move(15,290)
        roomexitslabel = QLabel(' Room 1', self)
        roomexitslabel.move(15,340)
        roomexitslabel = QLabel(' Room 2', self)
        roomexitslabel.move(15,390)
        roomexitslabel = QLabel(' Room 3', self)
        roomexitslabel.move(15,440)
        roomexitslabel = QLabel(' Room 4', self)
        roomexitslabel.move(15,490)
        roomexitslabel = QLabel(' Room 5', self)
        roomexitslabel.move(15,540)
        self.rmexita1 = QLineEdit(self)
        self.rmexita1.move(padding, 340)
        self.rmexita1.resize(boxw,boxh)
        self.rmexita2 = QLineEdit(self)
        self.rmexita2.move(padding, 390)
        self.rmexita2.resize(boxw,boxh)
        self.rmexita3 = QLineEdit(self)
        self.rmexita3.move(padding, 440)
        self.rmexita3.resize(boxw,boxh)
        self.rmexita4 = QLineEdit(self)
        self.rmexita4.move(padding, 490)
        self.rmexita4.resize(boxw,boxh)
        self.rmexita5 = QLineEdit(self)
        self.rmexita5.move(padding, 540)
        self.rmexita5.resize(boxw,boxh)
        padding = padding+10+boxw
        self.rmexitb1 = QLineEdit(self)
        self.rmexitb1.move(padding, 340)
        self.rmexitb1.resize(boxw,boxh)
        self.rmexitb2 = QLineEdit(self)
        self.rmexitb2.move(padding, 390)
        self.rmexitb2.resize(boxw,boxh)
        self.rmexitb3 = QLineEdit(self)
        self.rmexitb3.move(padding, 440)
        self.rmexitb3.resize(boxw,boxh)
        self.rmexitb4 = QLineEdit(self)
        self.rmexitb4.move(padding, 490)
        self.rmexitb4.resize(boxw,boxh)
        self.rmexitb5 = QLineEdit(self)
        self.rmexitb5.move(padding, 540)
        self.rmexitb5.resize(boxw,boxh)
        padding = padding+10+boxw
        self.rmexitc1 = QLineEdit(self)
        self.rmexitc1.move(padding, 340)
        self.rmexitc1.resize(boxw,boxh)
        self.rmexitc2 = QLineEdit(self)
        self.rmexitc2.move(padding, 390)
        self.rmexitc2.resize(boxw,boxh)
        self.rmexitc3 = QLineEdit(self)
        self.rmexitc3.move(padding, 440)
        self.rmexitc3.resize(boxw,boxh)
        self.rmexitc4 = QLineEdit(self)
        self.rmexitc4.move(padding, 490)
        self.rmexitc4.resize(boxw,boxh)
        self.rmexitc5 = QLineEdit(self)
        self.rmexitc5.move(padding, 540)
        self.rmexitc5.resize(boxw,boxh)
        padding = padding+10+boxw
        self.rmexitd1 = QLineEdit(self)
        self.rmexitd1.move(padding, 340)
        self.rmexitd1.resize(boxw,boxh)
        self.rmexitd2 = QLineEdit(self)
        self.rmexitd2.move(padding, 390)
        self.rmexitd2.resize(boxw,boxh)
        self.rmexitd3 = QLineEdit(self)
        self.rmexitd3.move(padding, 440)
        self.rmexitd3.resize(boxw,boxh)
        self.rmexitd4 = QLineEdit(self)
        self.rmexitd4.move(padding, 490)
        self.rmexitd4.resize(boxw,boxh)
        self.rmexitd5 = QLineEdit(self)
        self.rmexitd5.move(padding, 540)
        self.rmexitd5.resize(boxw,boxh)
        padding = padding+10+boxw
        self.rmexite1 = QLineEdit(self)
        self.rmexite1.move(padding, 340)
        self.rmexite1.resize(boxw,boxh)
        self.rmexite2 = QLineEdit(self)
        self.rmexite2.move(padding, 390)
        self.rmexite2.resize(boxw,boxh)
        self.rmexite3 = QLineEdit(self)
        self.rmexite3.move(padding, 440)
        self.rmexite3.resize(boxw,boxh)
        self.rmexite4 = QLineEdit(self)
        self.rmexite4.move(padding, 490)
        self.rmexite4.resize(boxw,boxh)
        self.rmexite5 = QLineEdit(self)
        self.rmexite5.move(padding, 540)
        self.rmexite5.resize(boxw,boxh)
        padding = padding+10+boxw
        self.rmexitf1 = QLineEdit(self)
        self.rmexitf1.move(padding, 340)
        self.rmexitf1.resize(boxw,boxh)
        self.rmexitf2 = QLineEdit(self)
        self.rmexitf2.move(padding, 390)
        self.rmexitf2.resize(boxw,boxh)
        self.rmexitf3 = QLineEdit(self)
        self.rmexitf3.move(padding, 440)
        self.rmexitf3.resize(boxw,boxh)
        self.rmexitf4 = QLineEdit(self)
        self.rmexitf4.move(padding, 490)
        self.rmexitf4.resize(boxw,boxh)
        self.rmexitf5 = QLineEdit(self)
        self.rmexitf5.move(padding, 540)
        self.rmexitf5.resize(boxw,boxh)
        padding = padding+10+boxw
        self.rmexitg1 = QLineEdit(self)
        self.rmexitg1.move(padding, 340)
        self.rmexitg1.resize(boxw,boxh)
        self.rmexitg2 = QLineEdit(self)
        self.rmexitg2.move(padding, 390)
        self.rmexitg2.resize(boxw,boxh)
        self.rmexitg3 = QLineEdit(self)
        self.rmexitg3.move(padding, 440)
        self.rmexitg3.resize(boxw,boxh)
        self.rmexitg4 = QLineEdit(self)
        self.rmexitg4.move(padding, 490)
        self.rmexitg4.resize(boxw,boxh)
        self.rmexitg5 = QLineEdit(self)
        self.rmexitg5.move(padding, 540)
        self.rmexitg5.resize(boxw,boxh)
        padding = padding+10+boxw
        self.rmexith1 = QLineEdit(self)
        self.rmexith1.move(padding, 340)
        self.rmexith1.resize(boxw,boxh)
        self.rmexith2 = QLineEdit(self)
        self.rmexith2.move(padding, 390)
        self.rmexith2.resize(boxw,boxh)
        self.rmexith3 = QLineEdit(self)
        self.rmexith3.move(padding, 440)
        self.rmexith3.resize(boxw,boxh)
        self.rmexith4 = QLineEdit(self)
        self.rmexith4.move(padding, 490)
        self.rmexith4.resize(boxw,boxh)
        self.rmexith5 = QLineEdit(self)
        self.rmexith5.move(padding, 540)
        self.rmexith5.resize(boxw,boxh)

        padding = padding+20+boxw
        roomexitslabel = QLabel('filename', self)
        roomexitslabel.move(padding,400)
        self.filename = QLineEdit(self)
        self.filename.move(padding, 440)
        # Create a button in the window
        self.button = QPushButton('Create', self)
        self.button.move(padding, 540)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
