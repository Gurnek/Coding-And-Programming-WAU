from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
'''class for creating the help menu window with text that describes how to use the app'''
class Ui_Help(QtWidgets.QWidget):
    #call the init of the super class and run setupUi
    def __init__(self):
        super().__init__()
        self.setupUi(self)
#function that creates a window with a scrollable text dialog in the middle
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(679, 603)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.setWindowIcon(QIcon('flame.png'))
#call the retranslateui function to populate the text dialog with HTML
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        #create the function variable for translating text to utf8
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Help Menu", "Help Menu"))
        #add HTML to 
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">The Heat Database Application</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">This is the help menu where you can find instructions on how the different tabs work and what each of them does.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Employee Tab:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">The employee tab is used for storing data about each of the employees. To start, create a new list from the employee menu in the upper left corner. You will be prompted for a name for this list and after you submit it, a new tab will be formed.  The add rows button will add blank spaces for new employees. The delete list option from the employee menu will delete the selected tab and all the data in it.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Customer Tab:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">The customer tab is used for storing data about customers who come to the FEC. Creating a new list is done the same way, except from the customer menu instead of the employee menu. The add row button will function the same way in this tab and will add space for info about each customer. In the arrival time column, time is expressed in military and decimal format. So for 1:30 PM, you would enter 13.5. The delete list option in the customer menu will delete the selected tab and all the data in it. The generate attendance report option in the menu opens a dialog that will prompt for a directory to create a pdf file with a report on customer attendance.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Schedule Tab:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">The schedule tab is used to create the weekly schedules for the employees. When a row is added to the employee tab, it is automatically added to the schedule tab too, but if it doesn\'t show, pressing the update tab button should fix it. The lists in the schedule tab are based on the lists from the employee tab, so the two are linked. The format of the schedule blocks can be in any format. The generate schedule report option in the menu will open a dialog that prompts for a directory to create a pdf file with a schedule for every employee.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Attendance Tab:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">The attendance tab creates a graph of the population as a function of time. Different tabs are created for different days in the arrival date column in the customer tab. The add row and delete row buttons do not do anything in this tab. Update tab will be used to update the graphs when a new date is added to the customer tab. </span></p></body></html>"))
