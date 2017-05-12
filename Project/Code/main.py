import sys, pickle, bcrypt, classes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPainter


class Ui_Fec_manager(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.salt = b'$2b$12$W1QJvsf.dEmkplYv2FY3Qu'
        self.credentials = {}
        self.data = {}
        self.loadLists()
        self.setupUi(self)


    def loadLists(self):
        try:
            with open('main.pickle', 'rb') as info:
                self.data = pickle.load(info)
                self.credentials = pickle.load(info)
        except:
            pass

    def setupUi(self, Fec_manager):
        Fec_manager.setObjectName("Fec_manager")
        Fec_manager.resize(1025, 828)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Fec_manager.sizePolicy().hasHeightForWidth())
        Fec_manager.setSizePolicy(sizePolicy)
        stylesheet = open('main.qss', 'r').read()
        Fec_manager.setStyleSheet(stylesheet)
        self.verticalLayout = QtWidgets.QVBoxLayout(Fec_manager)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Fec_layout = QtWidgets.QVBoxLayout()
        self.Fec_layout.setObjectName("Fec_layout")
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setObjectName("stackedWidget")
        self.login_layout = QtWidgets.QWidget(Fec_manager)
        self.login_layout.setObjectName("login_layout")
        self.gridLayout = QtWidgets.QGridLayout(self.login_layout)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.login_btn = QtWidgets.QPushButton(self.login_layout)
        self.login_btn.setStyleSheet("font: 25 20pt \"Quicksand-Bold\";\n"
"border: 2px solid black;")
        self.login_btn.setIconSize(QtCore.QSize(40, 40))
        self.login_btn.setAutoDefault(True)
        self.login_btn.setFlat(True)
        self.login_btn.setObjectName("login_btn")
        self.gridLayout.addWidget(self.login_btn, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 2, 1, 1)
        self.new_user_btn = QtWidgets.QPushButton(self.login_layout)
        self.new_user_btn.setAutoDefault(True)
        self.new_user_btn.setFlat(True)
        self.new_user_btn.setObjectName("new_user_btn")
        self.gridLayout.addWidget(self.new_user_btn, 6, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.login_layout)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 7, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 2, 1, 1)
        self.password_le = QtWidgets.QLineEdit(self.login_layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_le.sizePolicy().hasHeightForWidth())
        self.password_le.setSizePolicy(sizePolicy)
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_le.setClearButtonEnabled(True)
        self.password_le.setObjectName("password_le")
        self.gridLayout.addWidget(self.password_le, 2, 2, 1, 1)
        self.username_le = QtWidgets.QLineEdit(self.login_layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_le.sizePolicy().hasHeightForWidth())
        self.username_le.setSizePolicy(sizePolicy)
        self.username_le.setText("")
        self.username_le.setClearButtonEnabled(True)
        self.username_le.setObjectName("username_le")
        self.gridLayout.addWidget(self.username_le, 1, 2, 1, 1)
        self.stackedWidget.addWidget(self.login_layout)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 5, 4, 1, 1)
        self.create_user_btn = QtWidgets.QPushButton(self.page_2)
        self.create_user_btn.setAutoDefault(True)
        self.create_user_btn.setFlat(True)
        self.create_user_btn.setObjectName("create_user_btn")
        self.gridLayout_2.addWidget(self.create_user_btn, 9, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 5, 0, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_2.addWidget(self.textBrowser_2, 4, 0, 1, 5)
        self.new_username_le = QtWidgets.QLineEdit(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_username_le.sizePolicy().hasHeightForWidth())
        self.new_username_le.setSizePolicy(sizePolicy)
        self.new_username_le.setClearButtonEnabled(True)
        self.new_username_le.setObjectName("new_username_le")
        self.gridLayout_2.addWidget(self.new_username_le, 5, 2, 1, 1)
        self.new_pass_le = QtWidgets.QLineEdit(self.page_2)
        self.new_pass_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pass_le.setClearButtonEnabled(True)
        self.new_pass_le.setObjectName("new_pass_le")
        self.gridLayout_2.addWidget(self.new_pass_le, 7, 2, 1, 1)
        self.confirm_pass_le = QtWidgets.QLineEdit(self.page_2)
        self.confirm_pass_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_pass_le.setClearButtonEnabled(True)
        self.confirm_pass_le.setObjectName("confirm_pass_le")
        self.gridLayout_2.addWidget(self.confirm_pass_le, 8, 2, 1, 1)
        self.cancel_btn = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_btn.sizePolicy().hasHeightForWidth())
        self.cancel_btn.setSizePolicy(sizePolicy)
        self.cancel_btn.setStyleSheet("border : 0px solid white")
        self.cancel_btn.setAutoDefault(True)
        self.cancel_btn.setFlat(True)
        self.cancel_btn.setObjectName("cancel_btn")
        self.gridLayout_2.addWidget(self.cancel_btn, 3, 0, 1, 1)
        self.email_le = QtWidgets.QLineEdit(self.page_2)
        self.email_le.setClearButtonEnabled(True)
        self.email_le.setObjectName("email_le")
        self.gridLayout_2.addWidget(self.email_le, 6, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.stackedWidget.addWidget(self.page_2)
        self.Fec_layout.addWidget(self.stackedWidget)
        self.verticalLayout.addLayout(self.Fec_layout)
        self.setWindowIcon(QIcon('flame.png'))
        self.retranslateUi(Fec_manager)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Fec_manager)

    def retranslateUi(self, Fec_manager):
        _translate = QtCore.QCoreApplication.translate
        Fec_manager.setWindowTitle(_translate("Fec_manager", "FEC Manager"))
        self.login_btn.setText(_translate("Fec_manager", "Login"))
        self.new_user_btn.setText(_translate("Fec_manager", "New Account"))
        self.textBrowser.setHtml(_translate("Fec_manager", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Quicksand\'; font-size:12pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:56; font: 25 48pt \"Quicksand-Bold\";\">FEC Manager</span></p></body></html>"))
        self.password_le.setPlaceholderText(_translate("Fec_manager", "PASSWORD"))
        self.username_le.setPlaceholderText(_translate("Fec_manager", "USERNAME"))
        self.create_user_btn.setText(_translate('Fec_manager', 'Create User'))
        self.textBrowser_2.setHtml(_translate("Fec_manager", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Quicksand-Bold\'; font-size:12pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Create a new user</span></p></body></html>"))
        self.new_username_le.setPlaceholderText(_translate("Fec_manager", "USERNAME"))
        self.new_pass_le.setPlaceholderText(_translate("Fec_manager", "PASSWORD"))
        self.confirm_pass_le.setPlaceholderText(_translate("Fec_manager", "CONFIRM PASSWORD"))
        self.cancel_btn.setText(_translate("Fec_manager", "Go Back"))
        self.email_le.setPlaceholderText(_translate("Fec_manager", "EMAIL ADDRESS"))
        self.login_btn.clicked.connect(self.login)

    #@QtCore.pyqtSlot(name = 'on_login_btn_clicked')
    def login(self):
        username = self.username_le.text()
        password = self.password_le.text()
        password = str.encode(password)
        password = bcrypt.hashpw(password, self.salt)
        userId = self.credentials.get((username, password))
        if userId == None:
            msg = QtWidgets.QMessageBox.warning(self, 'Error', 'Invalid username or password.', QtWidgets.QMessageBox.Ok)
            return
        info = self.data.get(userId[0])
        chooseWidget = classes.Ui_Fec_Chooser(info, userId[0])
        self.stackedWidget.addWidget(chooseWidget)
        self.stackedWidget.setCurrentIndex(2)


    @QtCore.pyqtSlot(name = 'on_new_user_btn_clicked')
    def newUser(self):
        self.stackedWidget.setCurrentIndex(1)

    @QtCore.pyqtSlot(name = 'on_create_user_btn_clicked')
    def createNewUser(self):
        username = self.new_username_le.text()
        email = self.email_le.text()
        if self.new_pass_le.text() == self.confirm_pass_le.text():
            password = self.new_pass_le.text()
            password = str.encode(password)
            password = bcrypt.hashpw(password, self.salt)
            self.credentials[(username, password)] = (len(self.credentials), email)
            self.data[len(self.credentials) - 1] = []

            with open('main.pickle', 'wb') as info:
                pickle.dump(self.data, info, -1)
                pickle.dump(self.credentials, info, -1)

            success = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'Success', 'User Created Successfully!', QtWidgets.QMessageBox.Ok, self)
            success.exec_()
            self.stackedWidget.setCurrentIndex(0)
        else:
            msg = QtWidgets.QMessageBox.warning(self, 'Error', 'Invalid username or password.', QtWidgets.QMessageBox.Ok)

    @QtCore.pyqtSlot(name = 'on_cancel_btn_clicked')
    def cancel(self):
        self.stackedWidget.setCurrentIndex(0)

app = QtWidgets.QApplication(sys.argv)
win = Ui_Fec_manager()
if __name__ == '__main__':

    win.show()
    sys.exit(app.exec_())
