from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random
import sys
import time

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):
        self.setWindowTitle("Test Your Math...")
        self.r1 = QRadioButton("addition")
        self.r2 = QRadioButton("extraction")
        self.r3 = QRadioButton("multiplication")
        self.r4 = QRadioButton("division")

        self.point = 0

        h_box = QHBoxLayout()
        h_box.addWidget(self.r1)
        h_box.addWidget(self.r2)
        h_box.addWidget(self.r3)
        h_box.addWidget(self.r4)

        self.label_text = QLabel("Welcome To This Test.")
        self.label_text.setAlignment(Qt.AlignCenter)
        self.label_text.setStyleSheet("color: rgb(137,10,48);font-weight:bold; font-size: 16pt")

        self.v_box = QVBoxLayout()

        self.v_box.addWidget(self.label_text)

        self.v_box.addStretch()
        self.v_box.addLayout(h_box)

        self.cb = QComboBox()
        self.v_box.addWidget(self.cb)
        self.cb.addItems(["easy", "normal", "hard", "better than the coder"])



        self.cb2 = QComboBox()
        self.cb2.addItems(["1","2","3","4","5"])

        self.minitues = QLabel("Minitues for time limit")

        self.h3_box = QHBoxLayout()
        self.h3_box.addWidget(self.minitues)
        self.h3_box.addStretch()
        self.h3_box.addWidget(self.cb2)

        self.v_box.addLayout(self.h3_box)


        self.answer_place = QLineEdit("Write your answer here.")
        self.v_box.addWidget(self.answer_place)

        self.v_box.addStretch()

        self.h2_box = QHBoxLayout()

        self.startbutton = QPushButton()
        self.startbutton.setIcon(QIcon("startbutton.png"))
        self.startbutton.setIconSize(QSize(65,65))
        self.h2_box.addWidget(self.startbutton)
        self.startbutton.clicked.connect(self.chg)

        self.send_button = QPushButton()
        self.send_button.setIcon(QIcon("indir.png"))
        self.send_button.setIconSize(QSize(65,65))
        self.h2_box.addWidget(self.send_button)


        self.v_box.addLayout(self.h2_box)

        self.question_text =QLabel("Click start to see first question.")
        self.v_box.addWidget(self.question_text)

        self.v_box.addStretch()

        self.point_place = QLabel("Your Point will be shown here.Your point <br> will change depend on the level of difficulty")
        self.point_place.setAlignment(Qt.AlignCenter)
        self.point_place.setStyleSheet("color: rgb(137,10,48);font-weight:bold; font-size: 16pt")
        self.v_box.addWidget(self.point_place)


        self.setLayout(self.v_box)










    def chg(self):

        self.question_text.setText("Click next icon to see next question ...")
        self.timeout = time.time() + int(self.cb2.currentIndex()+1)*60





        if self.r1.isChecked():


            if str(self.cb.currentText()) == "easy":




                self.a = str(random.randint(1,99))
                self.b = str(random.randint(1,99))
                self.c = self.a+"+"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.addition_easy)


            elif str(self.cb.currentText()) == "normal":

                self.a = str(random.randint(100,1000))
                self.b = str(random.randint(1,1000))
                self.c = self.a+"+"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.addition_normal)

            elif str(self.cb.currentText()) == "hard":

                self.a = str(random.randint(1000,99999))
                self.b = str(random.randint(1000,99999))
                self.c = self.a+"+"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.addition_hard)
            elif str(self.cb.currentText()) == "better than the coder":

                self.a = str(random.randint(99999,999999999))
                self.b = str(random.randint(99999,999999999))
                self.c = self.a+"+"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.addition_better_than_coder)


        elif self.r2.isChecked():


            if str(self.cb.currentText()) == "easy":




                self.a = str(random.randint(1,99))
                self.b = str(random.randint(1,99))
                self.c = self.a+"-"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.extraction_easy)


            elif str(self.cb.currentText()) == "normal":

                self.a = str(random.randint(100,1000))
                self.b = str(random.randint(1,1000))
                self.c = self.a+"-"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.extraction_normal)

            elif str(self.cb.currentText()) == "hard":

                self.a = str(random.randint(1000,99999))
                self.b = str(random.randint(1000,99999))
                self.c = self.a+"-"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.extraction_hard)
            elif str(self.cb.currentText()) == "better than the coder":

                self.a = str(random.randint(99999,999999999))
                self.b = str(random.randint(99999,999999999))
                self.c = self.a+"-"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.extraction_better_than_coder)


        elif self.r3.isChecked():

            if str(self.cb.currentText()) == "easy":




                self.a = str(random.randint(1,99))
                self.b = str(random.randint(1,99))
                self.c = self.a+"*"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.multiplication_easy)


            elif str(self.cb.currentText()) == "normal":

                self.a = str(random.randint(100,1000))
                self.b = str(random.randint(1,1000))
                self.c = self.a+"*"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.multiplication_normal)

            elif str(self.cb.currentText()) == "hard":

                self.a = str(random.randint(1000,99999))
                self.b = str(random.randint(1000,99999))
                self.c = self.a+"*"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.multiplication_hard)
            elif str(self.cb.currentText()) == "better than the coder":

                self.a = str(random.randint(99999,999999999))
                self.b = str(random.randint(99999,999999999))
                self.c = self.a+"*"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.multiplication_better_than_coder)


        elif self.r4.isChecked():

            self.point_place.setText("Not puplished.So soon")
            """if str(self.cb.currentText()) == "easy":




                self.a = str(random.randint(1,99))
                self.b = str(random.randint(1,99))
                self.c = self.a+"/"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.addition_easy)


            elif str(self.cb.currentText()) == "normal":

                self.a = str(random.randint(100,1000))
                self.b = str(random.randint(1,1000))
                self.c = self.a+"/"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.addition_normal)

            elif str(self.cb.currentText()) == "hard":

                self.a = str(random.randint(1000,99999))
                self.b = str(random.randint(1000,99999))
                self.c = self.a+"/"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.addition_hard)
            elif str(self.cb.currentText()) == "better than the coder":

                self.a = str(random.randint(99999,999999999))
                self.b = str(random.randint(99999,999999999))
                self.c = self.a+"/"+self.b
                self.label_text.setText(self.c)

                self.send_button.clicked.connect(self.addition_better_than_coder)"""






    def addition_easy(self):

        pointforeasy = 10

        if time.time() < self.timeout:
            if (int(self.answer_place.text())) == int(self.a)+int(self.b):
                self.point+= pointforeasy
                self.point_place.setText("Your Point is {}".format(self.point))

                self.a = str(random.randint(1, 99))
                self.b = str(random.randint(1, 99))
                self.c = self.a + "+" + self.b
                self.label_text.setText(self.c)



            else :
                self.point-= pointforeasy/4
                self.point_place.setText("Your Point is {}".format(self.point))
                self.a = str(random.randint(1, 99))
                self.b = str(random.randint(1, 99))
                self.c = self.a + "+" + self.b
                self.label_text.setText(self.c)



        elif time.time()> self.timeout:
            self.point_place.setText("Your time is up and your point is{}".format(self.point))

            self.point = 0










    def addition_normal(self):
        pointfornormal = 50

        if time.time() < self.timeout:
            if (int(self.answer_place.text())) == int(self.a) + int(self.b):
                self.point += pointfornormal
                self.point_place.setText("Your Point is {}".format(self.point))

                self.a = str(random.randint(100, 1000))
                self.b = str(random.randint(1, 1000))
                self.c = self.a + "+" + self.b
                self.label_text.setText(self.c)



            else:
                self.point -= pointfornormal / 4
                self.point_place.setText("Your Point is {}".format(self.point))
                self.a = str(random.randint(100, 1000))
                self.b = str(random.randint(1, 1000))
                self.c = self.a + "+" + self.b
                self.label_text.setText(self.c)



        elif time.time() > self.timeout:
            self.point_place.setText("Your time is up and your point is{}".format(self.point))

            self.point = 0

    def addition_hard(self):
        pointforhard = 100

        if time.time() < self.timeout:
            if (int(self.answer_place.text())) == int(self.a) + int(self.b):
                self.point += pointforhard
                self.point_place.setText("Your Point is {}".format(self.point))

                self.a = str(random.randint(1000, 99999))
                self.b = str(random.randint(1000, 99999))
                self.c = self.a + "+" + self.b
                self.label_text.setText(self.c)



            else:
                self.point -= pointforhard / 4
                self.point_place.setText("Your Point is {}".format(self.point))
                self.a = str(random.randint(1, 99))
                self.b = str(random.randint(1, 99))
                self.c = self.a + "+" + self.b
                self.label_text.setText(self.c)



        elif time.time() > self.timeout:
            self.point_place.setText("Your time is up and your point is{}".format(self.point))

            self.point = 0



    def addition_better_than_coder(self):
        pointforbetter_than_coder = 400

        if time.time() < self.timeout:
            if (int(self.answer_place.text())) == int(self.a) + int(self.b):
                self.point += pointforbetter_than_coder
                self.point_place.setText("Your Point is {}".format(self.point))

                self.a = str(random.randint(99999, 999999999))
                self.b = str(random.randint(99999, 999999999))
                self.c = self.a + "+" + self.b
                self.label_text.setText(self.c)



            else:
                self.point -= pointforbetter_than_coder / 4
                self.point_place.setText("Your Point is {}".format(self.point))
                self.a = str(random.randint(99999, 999999999))
                self.b = str(random.randint(99999, 999999999))
                self.c = self.a + "+" + self.b
                self.label_text.setText(self.c)



        elif time.time() > self.timeout:
            self.point_place.setText("Your time is up and your point is{}".format(self.point))

            self.point = 0




    def extraction_easy(self):


        pointforeasy = 10

        if time.time() < self.timeout:
            if (int(self.answer_place.text())) == int(self.a) - int(self.b):
                self.point += pointforeasy
                self.point_place.setText("Your Point is {}".format(self.point))

                self.a = str(random.randint(1, 99))
                self.b = str(random.randint(1, 99))
                self.c = self.a + "-" + self.b
                self.label_text.setText(self.c)



            else:
                self.point -= pointforeasy / 4
                self.point_place.setText("Your Point is {}".format(self.point))
                self.a = str(random.randint(1, 99))
                self.b = str(random.randint(1, 99))
                self.c = self.a + "-" + self.b
                self.label_text.setText(self.c)



        elif time.time() > self.timeout:
            self.point_place.setText("Your time is up and your point is{}".format(self.point))

            self.point = 0


    def extraction_normal(self):
        pointfornormal = 50

        if time.time() < self.timeout:
            if (int(self.answer_place.text())) == int(self.a) - int(self.b):
                self.point += pointfornormal
                self.point_place.setText("Your Point is {}".format(self.point))

                self.a = str(random.randint(99, 999))
                self.b = str(random.randint(99, 999))
                self.c = self.a + "-" + self.b
                self.label_text.setText(self.c)



            else:
                self.point -= pointfornormal / 4
                self.point_place.setText("Your Point is {}".format(self.point))
                self.a = str(random.randint(1, 99))
                self.b = str(random.randint(1, 99))
                self.c = self.a + "-" + self.b
                self.label_text.setText(self.c)



        elif time.time() > self.timeout:
            self.point_place.setText("Your time is up and your point is{}".format(self.point))

            self.point = 0

        def extraction_hard(self):

            pointforhard = 100

            if time.time() < self.timeout:
                if (int(self.answer_place.text())) == int(self.a) - int(self.b):
                    self.point += pointforhard
                    self.point_place.setText("Your Point is {}".format(self.point))

                    self.a = str(random.randint(1, 99))
                    self.b = str(random.randint(1, 99))
                    self.c = self.a + "-" + self.b
                    self.label_text.setText(self.c)



                else:
                    self.point -= pointforhard / 4
                    self.point_place.setText("Your Point is {}".format(self.point))
                    self.a = str(random.randint(999, 9999))
                    self.b = str(random.randint(999, 9999))
                    self.c = self.a + "-" + self.b
                    self.label_text.setText(self.c)



            elif time.time() > self.timeout:
                self.point_place.setText("Your time is up and your point is{}".format(self.point))

                self.point = 0

    def extraction_better_than_coder(self):

        pointforbetter_than_coder = 400

        if time.time() < self.timeout:
            if (int(self.answer_place.text())) == int(self.a) - int(self.b):
                self.point += pointforbetter_than_coder
                self.point_place.setText("Your Point is {}".format(self.point))

                self.a = str(random.randint(999, 999999))
                self.b = str(random.randint(999, 999999))
                self.c = self.a + "-" + self.b
                self.label_text.setText(self.c)



            else:
                self.point -= pointforbetter_than_coder / 4
                self.point_place.setText("Your Point is {}".format(self.point))
                self.a = str(random.randint(999, 999999))
                self.b = str(random.randint(999, 999999))
                self.c = self.a + "-" + self.b
                self.label_text.setText(self.c)



        elif time.time() > self.timeout:
            self.point_place.setText("Your time is up and your point is{}".format(self.point))

            self.point = 0


    def multiplication_easy(self):
        pointforeasy =  15

        if time.time() < self.timeout:
            if (int(self.answer_place.text())) == int(self.a) * int(self.b):
                self.point += pointforeasy
                self.point_place.setText("Your Point is {}".format(self.point))

                self.a = str(random.randint(1, 10))
                self.b = str(random.randint(1, 10))
                self.c = self.a + "*" + self.b
                self.label_text.setText(self.c)



            else:
                self.point -= pointforeasy / 4
                self.point_place.setText("Your Point is {}".format(self.point))
                self.a = str(random.randint(1, 10))
                self.b = str(random.randint(1, 10))
                self.c = self.a + "*" + self.b
                self.label_text.setText(self.c)



        elif time.time() > self.timeout:
            self.point_place.setText("Your time is up and your point is{}".format(self.point))

            self.point = 0

    def multiplication_normal(self):
        pointfornormal =  75

        if time.time() < self.timeout:
            if (int(self.answer_place.text())) == int(self.a) * int(self.b):
                self.point += pointfornormal
                self.point_place.setText("Your Point is {}".format(self.point))

                self.a = str(random.randint(5, 25))
                self.b = str(random.randint(5, 25))
                self.c = self.a + "*" + self.b
                self.label_text.setText(self.c)



            else:
                self.point -= pointfornormal / 4
                self.point_place.setText("Your Point is {}".format(self.point))
                self.a = str(random.randint(5, 25))
                self.b = str(random.randint(5, 25))
                self.c = self.a + "*" + self.b
                self.label_text.setText(self.c)



        elif time.time() > self.timeout:
            self.point_place.setText("Your time is up and your point is{}".format(self.point))

            self.point = 0



    def multiplication_hard(self):
        pointforhard =  200

        if time.time() < self.timeout:
            if (int(self.answer_place.text())) == int(self.a) * int(self.b):
                self.point += pointforhard
                self.point_place.setText("Your Point is {}".format(self.point))

                self.a = str(random.randint(15, 75))
                self.b = str(random.randint(15, 75))
                self.c = self.a + "*" + self.b
                self.label_text.setText(self.c)



            else:
                self.point -= pointforhard / 4
                self.point_place.setText("Your Point is {}".format(self.point))
                self.a = str(random.randint(15, 75))
                self.b = str(random.randint(15, 75))
                self.c = self.a + "*" + self.b
                self.label_text.setText(self.c)



        elif time.time() > self.timeout:
            self.point_place.setText("Your time is up and your point is{}".format(self.point))

            self.point = 0



    def multiplication_better_than_coder(self):
        pointforbetter_than_coder =  800

        if time.time() < self.timeout:
            if (int(self.answer_place.text())) == int(self.a) * int(self.b):
                self.point += pointforbetter_than_coder
                self.point_place.setText("Your Point is {}".format(self.point))

                self.a = str(random.randint(75, 150))
                self.b = str(random.randint(75, 150))
                self.c = self.a + "*" + self.b
                self.label_text.setText(self.c)



            else:
                self.point -= pointforbetter_than_coder / 4
                self.point_place.setText("Your Point is {}".format(self.point))
                self.a = str(random.randint(75, 150))
                self.b = str(random.randint(75, 150))
                self.c = self.a + "*" + self.b
                self.label_text.setText(self.c)



        elif time.time() > self.timeout:
            self.point_place.setText("Your time is up and your point is{}".format(self.point))

            self.point = 0





if __name__ == "__main__":
    app = QApplication([])
    pencere = Pencere()
    pencere.show()
    app.exec_()


