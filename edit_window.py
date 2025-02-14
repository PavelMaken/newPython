from PyQt6.QtWidgets import QMessageBox, QErrorMessage
from PyQt6.QtWidgets import QWidget
from PyQt6 import QtCore, QtWidgets

import repository
from partner_types import Partner


class Ui_EditWindow(object):
    def setupUi(self, edit_window : QWidget):
        edit_window.setObjectName("EditWindow")
        edit_window.resize(800, 600)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=edit_window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 371, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.name_view = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.name_view.setObjectName("name_view")
        self.verticalLayout.addWidget(self.name_view)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.type_combo_box = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.type_combo_box.setObjectName("type_combo_box")
        self.verticalLayout.addWidget(self.type_combo_box)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.rating_view = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.rating_view.setObjectName("rating_view")
        self.verticalLayout.addWidget(self.rating_view)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.address_view = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.address_view.setObjectName("address_view")
        self.verticalLayout.addWidget(self.address_view)
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.second_name_view = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.second_name_view.setObjectName("second_name_view")
        self.verticalLayout.addWidget(self.second_name_view)
        self.label_8 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.first_name_view = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.first_name_view.setObjectName("first_name_view")
        self.verticalLayout.addWidget(self.first_name_view)
        self.label_9 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.sur_name_view = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.sur_name_view.setObjectName("sur_name_view")
        self.verticalLayout.addWidget(self.sur_name_view)
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.phone_view = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.phone_view.setObjectName("phone_view")
        self.verticalLayout.addWidget(self.phone_view)
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.email_view = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.email_view.setObjectName("email_view")
        self.verticalLayout.addWidget(self.email_view)
        self.back_button = QtWidgets.QPushButton(parent=edit_window)
        self.back_button.setGeometry(QtCore.QRect(610, 510, 75, 31))
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(edit_window.close)
        self.save_button = QtWidgets.QPushButton(parent=edit_window)
        self.save_button.setGeometry(QtCore.QRect(700, 510, 75, 31))
        self.save_button.setObjectName("save_button")

        self.retranslateUi(edit_window)


    def fill_partner(self, partner : Partner=None):

        if partner:
            self.partner = partner
            self.name_view.setText(partner.partner_name)
            try:
                self.first_name_view.setText(partner.partner_director.split()[1])
            except:
                self.first_name_view.setText('')
            try:
                self.second_name_view.setText(partner.partner_director.split()[0])
            except:
                self.second_name_view.setText('')
            try:
                self.sur_name_view.setText(partner.partner_director.split()[2])
            except:
                self.sur_name_view.setText('')
            self.rating_view.setText(str(partner.partner_rating))
            self.address_view.setText(partner.partner_address)
            self.email_view.setText(partner.partner_address)
            self.address_view.setText(partner.partner_address)
            self.address_view.setText(partner.partner_address)
            self.type_combo_box.setCurrentText(partner.partner_type)
            self.phone_view.setText(partner.partner_phone)
            self.save_button.clicked.connect(self.update_partner)
        else:
            self.name_view.setText('')
            self.first_name_view.setText('')
            self.second_name_view.setText('')
            self.sur_name_view.setText('')
            self.rating_view.setText('')
            self.address_view.setText('')
            self.email_view.setText('')
            self.address_view.setText('')
            self.address_view.setText('')
            self.type_combo_box.setCurrentText('')
            self.phone_view.setText('')
            self.save_button.clicked.connect(self.create_partner)


    def retranslateUi(self, EditWindow):
        _translate = QtCore.QCoreApplication.translate
        EditWindow.setWindowTitle(_translate("EditWindow", "Добавление/Редактирование партнёра"))
        self.label.setText(_translate("EditWindow", "Наименование"))
        self.label_2.setText(_translate("EditWindow", "Тип партнёра"))
        self.label_3.setText(_translate("EditWindow", "Рейтинг"))
        self.label_4.setText(_translate("EditWindow", "Адрес"))
        self.label_7.setText(_translate("EditWindow", "Фамилия директора"))
        self.label_8.setText(_translate("EditWindow", "Имя директора"))
        self.label_9.setText(_translate("EditWindow", "Отчество директора"))
        self.label_5.setText(_translate("EditWindow", "Телефон"))
        self.label_6.setText(_translate("EditWindow", "Email"))
        self.back_button.setText(_translate("EditWindow", "Назад"))
        self.save_button.setText(_translate("EditWindow", "Сохранить"))
        self.type_combo_box.addItems(['OOO', 'ЗАО', 'ОАО', 'ПАО'])

    def update_partner(self):
        try:
            repository.update_partner(
                self.partner.partner_id,
                self.type_combo_box.currentText(),
                self.name_view.text(),
                self.first_name_view.text(),
                self.second_name_view.text(),
                self.sur_name_view.text(),
                self.email_view.text(),
                self.phone_view.text(),
                self.address_view.text(),
                self.rating_view.text()
            )
            self.back_button.click()
        except:
            QMessageBox().critical(None, "wrong address input", 'Неправильный формат адреса')

    def create_partner(self):
        try:
            repository.create_new_partner(
                self.type_combo_box.currentText(),
                self.name_view.text(),
                self.first_name_view.text(),
                self.second_name_view.text(),
                self.sur_name_view.text(),
                self.email_view.text(),
                self.phone_view.text(),
                self.address_view.text(),
                self.rating_view.text()
            )
            self.back_button.click()
        except :
            QMessageBox().critical(None, "wrong address input", 'Неправильный формат адреса')