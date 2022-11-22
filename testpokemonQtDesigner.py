import sys
import requests

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QImage



class Pokemon:

    def __init__(self, num, nom, type1, type2, height, weight, pv, attaque, defense, attaqueSpe,defenseSpe, speed):
        self.num = num
        self.nom = nom
        self.type1 = type1
        self.type2 = type2
        self.height = height
        self.weight = weight
        self.pv = pv
        self.attaque = attaque
        self.defense = defense
        self.attaqueSpe = attaqueSpe
        self.defenseSpe = defenseSpe        
        self.speed = speed

r = requests.get("https://pokeapi.co/api/v2/pokemon/6")

result = r.json()


bulbasaur = Pokemon(result["id"], result["name"], result["types"][0]["type"]["name"], result["types"][1]["type"]["name"], result["height"], result["weight"], result["stats"][0]["base_stat"], result["stats"][1]["base_stat"], result["stats"][2]["base_stat"], result["stats"][3]["base_stat"], result["stats"][4]["base_stat"], result["stats"][5]["base_stat"])


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("poke.ui",self)

        qpixmap = QPixmap('2200032_50ba6.jpg')
        self.Background.setPixmap(qpixmap)

        name = bulbasaur.nom
        self.Name.setText(name)

        url_img = result["sprites"]["front_default"]
        image = QImage()
        image.loadFromData(requests.get(url_img).content)
        bigger_img = image.scaled(221, 221)
        self.ImagePokemon.setPixmap(QPixmap(bigger_img))

        num = str(bulbasaur.num)
        self.Num.setText(num)

        type1 = bulbasaur.type1
        self.Type1.setText(type1)

        type2 = bulbasaur.type2
        self.Type2.setText(type2)

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


# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(450)
widget.setFixedWidth(600)
widget.show()
widget.setWindowTitle("Pokedex")
try:
    sys.exit(app.exec_())
except:
    print("Exiting")