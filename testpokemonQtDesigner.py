import sys
import requests

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QImage




class Pokemon:

    def __init__(self, num, nom, type1, height, weight, pv, attaque, defense, attaqueSpe,defenseSpe, speed):
        self.num = num
        self.nom = nom
        self.type1 = type1
        self.height = height
        self.weight = weight
        self.pv = pv
        self.attaque = attaque
        self.defense = defense
        self.attaqueSpe = attaqueSpe
        self.defenseSpe = defenseSpe        
        self.speed = speed

numchoice = 150
r = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(numchoice))
result = r.json()

bulbasaur = Pokemon(result["id"], result["name"], result["types"][0]["type"]["name"], result["height"], result["weight"], result["stats"][0]["base_stat"], result["stats"][1]["base_stat"], result["stats"][2]["base_stat"], result["stats"][3]["base_stat"], result["stats"][4]["base_stat"], result["stats"][5]["base_stat"])

s1 = 151
r2 = requests.get("https://pokeapi.co/api/v2/pokemon?limit="+str(s1)+"&offset=0")
resultLst = r2.json()

nb = 0
PokemonsLst = resultLst["results"][nb]["name"]
for i in range (0, s1-1):

    nb = nb + 1
    PokemonsLst = PokemonsLst +","+resultLst["results"][nb]["name"]


PokemonsLst = PokemonsLst.split(",")

# if (result["types"][1]["type"]["name"] != ""):
#     type2 = result["types"][1]["type"]["name"]

# else:
#     type2 = ""


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("poke.ui",self)

        qpixmap = QPixmap('pokedex.png')
        self.Background.setPixmap(qpixmap)

        self.ChooseList.addItems(PokemonsLst)
        self.ChooseList.setEditable(True)


        name = bulbasaur.nom
        cap_name = name.title()
        self.Name.setText(cap_name)

        url_img = result["sprites"]["front_default"]
        image = QImage()
        image.loadFromData(requests.get(url_img).content)
        bigger_img = image.scaled(361, 361)
        self.ImagePokemon.setPixmap(QPixmap(bigger_img))

        num = str(bulbasaur.num)
        self.Num.setText(num)

        type1 = bulbasaur.type1
        self.Type1.setText(type1)

        # self.Type2.setText(type2)

        hp = str(bulbasaur.pv)
        self.PV.setText(hp)

        weight = str(bulbasaur.weight / 10)
        self.Weight.setText(weight)

        height = str(bulbasaur.height / 10)
        self.Height.setText(height)

        attack = str(bulbasaur.attaque)
        self.Attaque.setText(attack)

        defense = str(bulbasaur.defense)
        self.Defense.setText(defense)

        attackSpe = str(bulbasaur.attaqueSpe)
        self.AttaqueSpe.setText(attackSpe)

        defenseSpe = str(bulbasaur.defenseSpe)
        self.DefenseSpe.setText(defenseSpe)

        speed = str(bulbasaur.speed)
        self.Speed.setText(speed)

        self.ButtonNext.clicked.connect(self.plus)

        self.ButtonBack.clicked.connect(self.moins)


    def plus(self):
        numchoice = numchoice + 1

    def moins(self):
        numchoice = numchoice - 1



# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(675)
widget.setFixedWidth(900)
widget.show()
widget.setWindowTitle("Pokedex")
try:
    sys.exit(app.exec_())
except:
    print("Exiting")