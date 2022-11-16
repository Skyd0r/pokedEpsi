import sys
import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel

class Pokemon:

    def __init__(self, nom, pv, attaque, defense, attaqueSpe,defenseSpe, speed):
        self.nom = nom
        self.pv = pv
        self.attaque = attaque
        self.defense = defense
        self.attaqueSpe = attaqueSpe
        self.defenseSpe = defenseSpe        
        self.speed = speed


bulbasaur = Pokemon(name, 45, 49, 49, 65, 65, 45)

class WindowLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        name = QLabel(bulbasaur.nom)
        img = QPixmap('bulbasaur.png')
        smaller_img = img.scaled(100, 100)
        labelImg = QLabel(self)
        labelImg.setPixmap(smaller_img)
        labelHp = QLabel("Points de vie : ")
        hp = QLabel(str(bulbasaur.pv))
        labelAttack = QLabel("Attaque : ")
        attack = QLabel(str(bulbasaur.attaque))
        labelDefense = QLabel("Défense : ")
        defense = QLabel(str(bulbasaur.defense))
        labelAttackSpe = QLabel("AttaqueSpe : ")
        attackSpe = QLabel(str(bulbasaur.attaqueSpe))
        labelDefenseSpe = QLabel("DéfenseSpe : ")
        defenseSpe = QLabel(str(bulbasaur.defenseSpe))
        labelSpeed = QLabel("Vitesse : ")
        speed = QLabel(str(bulbasaur.speed))


        wLayout = QGridLayout()
        wLayout.addWidget(name, 0, 3)
        wLayout.addWidget(labelImg, 1, 3)
        wLayout.addWidget(labelHp, 3, 0)
        wLayout.addWidget(hp, 3, 1)
        wLayout.addWidget(labelSpeed, 3, 4)
        wLayout.addWidget(speed, 3, 5)
        wLayout.addWidget(labelAttack, 4, 0)
        wLayout.addWidget(attack, 4, 1)
        wLayout.addWidget(labelDefense, 4, 4)
        wLayout.addWidget(defense, 4, 5)
        wLayout.addWidget(labelAttackSpe, 5, 0)
        wLayout.addWidget(attackSpe, 5, 1)
        wLayout.addWidget(labelDefenseSpe, 5, 4)
        wLayout.addWidget(defenseSpe, 5, 5)

        self.setLayout(wLayout)
        self.setGeometry(400, 200, 200, 300)
        self.setWindowTitle("Pokemon")
        self.show()


def main():
    app = QApplication([])
    w = WindowLayout()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()