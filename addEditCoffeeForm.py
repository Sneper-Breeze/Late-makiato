# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Coffee_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(227, 185)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vert = QtWidgets.QVBoxLayout()
        self.vert.setObjectName("vert")
        self.hor_1 = QtWidgets.QHBoxLayout()
        self.hor_1.setObjectName("hor_1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.hor_1.addWidget(self.label)
        self.title = QtWidgets.QLineEdit(Form)
        self.title.setObjectName("title")
        self.hor_1.addWidget(self.title)
        self.vert.addLayout(self.hor_1)
        self.hor_2 = QtWidgets.QHBoxLayout()
        self.hor_2.setObjectName("hor_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.hor_2.addWidget(self.label_2)
        self.level = QtWidgets.QLineEdit(Form)
        self.level.setObjectName("level")
        self.hor_2.addWidget(self.level)
        self.vert.addLayout(self.hor_2)
        self.hor_3 = QtWidgets.QHBoxLayout()
        self.hor_3.setObjectName("hor_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.hor_3.addWidget(self.label_3)
        self.in_seeds = QtWidgets.QLineEdit(Form)
        self.in_seeds.setObjectName("in_seeds")
        self.hor_3.addWidget(self.in_seeds)
        self.vert.addLayout(self.hor_3)
        self.hor_4 = QtWidgets.QHBoxLayout()
        self.hor_4.setObjectName("hor_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.hor_4.addWidget(self.label_4)
        self.cost = QtWidgets.QLineEdit(Form)
        self.cost.setObjectName("cost")
        self.hor_4.addWidget(self.cost)
        self.vert.addLayout(self.hor_4)
        self.hor_5 = QtWidgets.QHBoxLayout()
        self.hor_5.setObjectName("hor_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.hor_5.addWidget(self.label_5)
        self.volume = QtWidgets.QLineEdit(Form)
        self.volume.setObjectName("volume")
        self.hor_5.addWidget(self.volume)
        self.vert.addLayout(self.hor_5)
        self.hor = QtWidgets.QHBoxLayout()
        self.hor.setObjectName("hor")
        self.text = QtWidgets.QLabel(Form)
        self.text.setText("")
        self.text.setObjectName("text")
        self.hor.addWidget(self.text)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.hor.addWidget(self.buttonBox)
        self.vert.addLayout(self.hor)
        self.verticalLayout.addLayout(self.vert)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление элемента"))
        self.label.setText(_translate("Form", "Название:"))
        self.label_2.setText(_translate("Form", "Степень прожарки:"))
        self.label_3.setText(_translate("Form", "В зернах/молотый:"))
        self.label_4.setText(_translate("Form", "Цена:"))
        self.label_5.setText(_translate("Form", "Размер упаковки:"))
