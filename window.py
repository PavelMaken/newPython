from PyQt6.QtGui import QIcon
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QListWidgetItem, QMainWindow, QWidget

import logic
from edit_window import Ui_EditWindow
from list_view import PartnerItemWidget
from repository import get_partners


class Ui_MainWindow(object):
    def setupUi(self, MainWindow : QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Подмодуль партнёры")
        MainWindow.resize(800, 600)
        MainWindow.setWindowIcon(QIcon('res/icon.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.edit_window = QWidget()
        self.edit_window_ui = Ui_EditWindow()
        self.edit_window_ui.setupUi(self.edit_window)
        self.edit_window_ui.back_button.clicked.connect(get_new_partner_data)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 10, 781, 551))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 520, 141, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.create_new_partner)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_new_partner(self):
        self.edit_window_ui.fill_partner()
        self.edit_window.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def add_item(self, partner):
        item = QListWidgetItem()
        item.setSizeHint(QSize(300, 150))
        self.listView.addItem(item)

        widget = PartnerItemWidget()
        widget.setupUi(self.edit_window, self.edit_window_ui, partner)

        self.listView.setItemWidget(item, widget)

    def clear_list(self):
        self.listView.clear()


ui = Ui_MainWindow()

def setupUI(partners):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui.setupUi(MainWindow)

    for partner in partners:
        ui.add_item(partner)

    MainWindow.show()
    app.exec()
    sys.exit(app.exec())

def get_new_partner_data():
    ui.clear_list()
    partner_data = get_partners()

    for partner in partner_data:
        logic.calculate_discount(partner)
        ui.add_item(partner)