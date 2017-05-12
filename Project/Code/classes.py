import sys, sqlite3, pickle, gc, datetime, test, atexit
from PyQt5 import QtCore, QtWidgets, QtSql, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtChart import QChart, QLineSeries, QChartView, QValueAxis


class Ui_Fec_Chooser(QtWidgets.QWidget):
    def __init__(self, info, userId):
        self.info = info
        self.userId = userId
        self.fecData = {}
        super().__init__()
        self.loadLists()
        self.setupUi(self)
        self.createButtons(self.info)
        self.retranslateUi(self)

    def loadLists(self):
        fh = 'fecNames' + str(self.userId) + '.pickle'
        try:
            with open(fh, 'rb') as names:
                self.info = pickle.load(names)
        except:
            pass


    def setupUi(self, Fec_Chooser):
        Fec_Chooser.setObjectName("Fec_Chooser")
        Fec_Chooser.resize(1086, 838)
        Fec_Chooser.setMinimumSize(QtCore.QSize(1001, 0))
        Fec_Chooser.setWindowOpacity(1.0)
        Fec_Chooser.setStyleSheet("background-color : rgb(200, 200, 200);\n"
"color : black")
        self.gridLayout = QtWidgets.QGridLayout(Fec_Chooser)
        self.gridLayout.setObjectName("gridLayout")
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(16)
        spacerItem = QtWidgets.QSpacerItem(331, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(331, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 6, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Fec_Chooser)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 4)

        QtCore.QMetaObject.connectSlotsByName(Fec_Chooser)

    def retranslateUi(self, Fec_Chooser):
        _translate = QtCore.QCoreApplication.translate
        Fec_Chooser.setWindowTitle(_translate("Fec_Chooser", "FEC Manager"))
        self.createNewFec.setText('+Create New Fec')
        self.createNewFec.clicked.connect(self.newFec)
        self.textBrowser.setHtml(_translate("Fec_Chooser", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Quicksand\'; font-size:48pt;\">Choose an FEC</span></p></body></html>"))
        QtCore.QMetaObject.connectSlotsByName(Fec_Chooser)


    def createButtons(self, fecData):
        print(fecData)
        for fec in fecData:
            try:
                button = getattr(self, fec)
                del button
            except:
                pass
        try:
            self.createNewFec.hide()
        except:
            pass
        x = 2
        for fec in fecData:
            setattr(self, fec, QtWidgets.QPushButton(self))
            button = getattr(self, fec)
            button.setText(fec)
            self.gridLayout.addWidget(button, x, 1, 1, 1)
            x += 1
            print(x)
        for fec in fecData:
            button = getattr(self, fec)
            button.clicked.connect(lambda : self.loadUserInfo(fec))

        self.createNewFec = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createNewFec.sizePolicy().hasHeightForWidth())
        self.createNewFec.setSizePolicy(sizePolicy)
        self.createNewFec.setObjectName("createNewFec")
        self.gridLayout.addWidget(self.createNewFec, x, 1, 1, 1)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.retranslateUi(self)

    def newFec(self):
        flags = QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint
        text, ok = QtWidgets.QInputDialog.getText(QtWidgets.QWidget(), 'New FEC', 'Enter FEC Name:', QtWidgets.QLineEdit.Normal, None, flags)
        if ok:
            self.info.append(text)
            with open('fecNames' + str(self.userId) + '.pickle' , 'wb') as names:
                pickle.dump(self.info, names, -1)
            self.createButtons(self.info)

    def loadUserInfo(self, fec):
        global spreadSheet
        spreadSheet = Ui_FEC(fec)
        spreadSheet.show()


class Ui_FEC(QMainWindow):
    '''This is the main class which contains all the code that creates the main window'''

    #The initial function calls the inherited init and then the main method
    def __init__(self, fec):
        super().__init__()
        self.fec = fec
        self.checkDatabase(self.fec)
        #Makes several data structures for use later on
        self.tabNameDict_E = {}
        self.tabNameDict_C = {}
        self.data = []
        #Stores the models and view widgets used to make the employee tab
        self.employeeModels = {}
        self.employeeViews = {}

        #Stores the models and view widgets used to make the customer tab
        self.customerModels = {}
        self.customerViews = {}

        #Stores the models and view widgets used to make the schedule tab
        self.scheduleModels = {}
        self.scheduleViews = {}

        empSelect = 'SELECT list_id FROM Employee'
        self.idList_E = []
        #Adds list_ids from the Employee table to idList_E
        self.genIdList(self.idList_E, empSelect)

        custSelect = 'SELECT list_id FROM Customer'
        self.idList_C = []

        #Adds list_ids from the Customer table to isList_C
        self.genIdList(self.idList_C, custSelect)
        self.loadLists(self.fec)
        atexit.register(self.collect)
        atexit.register(self.uponEnd)
        self.setupUi(self)

    #Function that populates the tabNameDicts from pickle file
    def loadLists(self, name):
        try:
            #open the pickle file
            with open(name + '.pickle', 'rb') as inputFile:
                #load the dicts from the file
                self.tabNameDict_E = pickle.load(inputFile)
                self.tabNameDict_C = pickle.load(inputFile)
        #If pickle file is empty, skip
        except:
            print('failed')

    #Create the idList data structures
    def genIdList(self, list, select):
        #The cursor can only move forward in its list of selections
        self.cur.setForwardOnly(True)
        #Executes the select statement in the argument
        self.cur.exec_(select)
        #Scrolls through all values of the select
        while self.cur.next():
            #Checks to see if the current value is already in the list
            if self.cur.value(0) in list:
                continue
            #Adds value to list if it isnt't in there
            list.append(self.cur.value(0))

    def checkDatabase(self, name):
        #Add a database, connect to it, and read all of the data for use later on
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(name + '.db3')
        db.open()
        #Create a query for executing SQL commands
        self.cur = QtSql.QSqlQuery()
        #Create an alternate cursor for executing SQL commands with variables in them
        self.conn = sqlite3.connect(name + '.db3')
        self.cursor = self.conn.cursor()
        #Create and Employee table if it doesn't exist yet
        self.cur.exec_('''
        CREATE TABLE IF NOT EXISTS Employee (
            name TEXT,
            email TEXT,
            age INTEGER,
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            list_id INTEGER,
            monday TEXT,
            tuesday TEXT,
            wednesday TEXT,
            thursday TEXT,
            friday TEXT,
            saturday TEXT,
            sunday TEXT
            )''')

            #Create a Customer table if it doesn't exist yet
        self.cur.exec_('''
            CREATE TABLE IF NOT EXISTS Customer (
            name TEXT,
            age INTEGER,
            email TEXT,
            arrival_time TEXT,
            arrival_date TEXT,
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            list_id INTEGER
        )''')

    #The method that creates all of the objects and widgets to be displayed in the gui
    def setupUi(self, FEC):
        '''This method creates all of the objects in the view and displays them in a window'''

        #Create the window object and name it FEC
        FEC.setObjectName('FEC')
        #Set the intial size of the window
        FEC.resize(1096, 884)

        #Set the main widget as the window
        self.centralwidget = QtWidgets.QWidget(FEC)
        #Name the main widget centralwidget
        self.centralwidget.setObjectName('centralwidget')

        #Create a vertical layout in the gui and name it
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName('verticalLayout')

        #Create a horizontal layout in the gui and name it
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName('horizontalLayout')

        #Make a button called btn_AddRow, add it to the horizontal layout, and then center it
        self.btn_AddRow = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.btn_AddRow.setObjectName('btn_AddRow')
        self.horizontalLayout.addWidget(self.btn_AddRow, 0, QtCore.Qt.AlignHCenter)

        #Make a button called btn_EditRow, add it to the horizontal layout, and then center it
        self.btn_Update = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.btn_Update.setObjectName('btn_Update')
        self.horizontalLayout.addWidget(self.btn_Update, 0, QtCore.Qt.AlignHCenter)

        #Make a buttom called btn_DeleteRow, add it to the horizontal layout, and center it
        self.btn_DeleteRow = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.btn_DeleteRow.setObjectName('btn_DeleteRow')
        self.horizontalLayout.addWidget(self.btn_DeleteRow, 0, QtCore.Qt.AlignHCenter)

        #add the horizontalLayout to the verical layout
        self.verticalLayout.addLayout(self.horizontalLayout)

        #Create a tab widget, and set the tabs nonclosable and non movable
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName('tabWidget')

        #Create a tab and another tab widget for inside the tab
        self.tab_Employee = QtWidgets.QWidget()
        self.tab_Employee.setObjectName('tab_Employee')
        self.employeeTabWidget = QtWidgets.QTabWidget()
        self.employeeTabWidget.setObjectName('employeeTabWidget')

        #Make a layout for inside the tab, and add the new tab widget to the layout.

        self.altLayout_E = QtWidgets.QVBoxLayout()
        self.altLayout_E.setObjectName('altLayout_E')
        self.employeeTabWidget.setMovable(False)
        self.altLayout_E.addWidget(self.employeeTabWidget)
        #Set the layout of the employee tab to the one with the employee tab widget
        self.tab_Employee.setLayout(self.altLayout_E)

        #add the employee tab to the original tab widget and call the employee tab function
        self.tabWidget.addTab(self.tab_Employee, 'Employee List')
        self.employeeTabUi()

        #create the customer tab and the tab widget for inside it
        self.tab_Customer = QtWidgets.QWidget()
        self.tab_Customer.setObjectName('tab_Customer')
        self.customerTabWidget = QtWidgets.QTabWidget()
        self.customerTabWidget.setObjectName('customerTabWidget')

        #create the tab layout, and add the customer tab widget to the layout
        self.altLayout_C = QtWidgets.QVBoxLayout()
        self.altLayout_C.setObjectName('altLayout_C')
        self.customerTabWidget.setMovable(False)
        self.altLayout_C.addWidget(self.customerTabWidget)
        #add the customer tab widget to the customer tab
        self.tab_Customer.setLayout(self.altLayout_C)

        #add the customer tab to the original tab widget and call the customer ui function
        self.tabWidget.addTab(self.tab_Customer, 'Customer List')
        self.customerTabUi()

        #create a schedule tab and a tab widget
        self.tab_Schedule = QtWidgets.QWidget()
        self.tab_Schedule.setObjectName('tab_Schedule')
        self.scheduleTabWidget = QtWidgets.QTabWidget()
        self.scheduleTabWidget.setObjectName('scheduleTabWidget')

        #create a layout for the tab widget
        self.altLayout_S = QtWidgets.QVBoxLayout()
        self.altLayout_S.setObjectName('altLayout_S')
        self.scheduleTabWidget.setMovable(False)
        self.altLayout_S.addWidget(self.scheduleTabWidget)
        #add the schedule tab widget to the schedule tab
        self.tab_Schedule.setLayout(self.altLayout_S)

        #Add the schedule tab to the original tab widget and call the schedule ui function
        self.tabWidget.addTab(self.tab_Schedule, 'Employee Schedule')
        self.scheduleTabUi()

        #create the attendance tab and the tab widget inseide it
        self.tab_Attendance = QtWidgets.QWidget()
        self.tab_Attendance.setObjectName('tab_Attendance')
        self.attendanceTabWidget = QtWidgets.QTabWidget()
        self.attendanceTabWidget.setObjectName('attendanceTabWidget')

        #make the layout to hold the tab widget
        self.altLayout_A = QtWidgets.QVBoxLayout()
        self.altLayout_A.setObjectName('altLayout_A')
        self.attendanceTabWidget.setMovable(False)
        self.altLayout_A.addWidget(self.attendanceTabWidget)
        #add the tab widget to the tab
        self.tab_Attendance.setLayout(self.altLayout_A)

        #Add the attendance tab to the original tab widget and call the attendance ui function
        self.tabWidget.addTab(self.tab_Attendance, 'Customer Attendance')
        self.attendanceTabUi()

        #add the original tab widget to the vertical layout
        self.verticalLayout.addWidget(self.tabWidget)

        #set the main widget of the window to itself
        FEC.setCentralWidget(self.centralwidget)

        #make a menubar for the window
        self.menubar = QtWidgets.QMenuBar(FEC)
        #set the size of the menubar
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1096, 26))
        self.menubar.setObjectName("menubar")
        #make a tab in the menubar called menuEmployee
        self.menuEmployee = QtWidgets.QMenu(self.menubar)
        self.menuEmployee.setObjectName("menuEmployee")
        #make a tab in the menubar called menuCustomer
        self.menuCustomer = QtWidgets.QMenu(self.menubar)
        self.menuCustomer.setObjectName("menuCustomer")
        #make a tab in the menubar called menuSchedule
        self.menuSchedule = QtWidgets.QMenu(self.menubar)
        self.menuSchedule.setObjectName("menuSchedule")
        #make a tab in the menubar called menuHelp
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName('menuHelp')
        #Set the windows menubar to the one just made
        FEC.setMenuBar(self.menubar)
        #Create the dropdown menus for the menubars
        self.statusbar = QtWidgets.QStatusBar(FEC)
        self.statusbar.setObjectName("statusbar")
        #add the dropdown menus to the window
        FEC.setStatusBar(self.statusbar)
        #add an option to the employee menu called new employee
        self.actionNewEmployee = QtWidgets.QAction(FEC)
        self.actionNewEmployee.setObjectName("actionNewEmployee")
        #add an option to the employee menu called delete employee
        self.actionDeleteEmployee = QtWidgets.QAction(FEC)
        self.actionDeleteEmployee.setObjectName("actionDeleteEmployee")
        #add an option to the customer menu called new customer
        self.actionNewCustomer = QtWidgets.QAction(FEC)
        self.actionNewCustomer.setObjectName("actionNewCustomer")
        #add an option to the customer menu called delete customer
        self.actionDeleteCustomer = QtWidgets.QAction(FEC)
        self.actionDeleteCustomer.setObjectName("actionDeleteCustomer")
        #add an option to the schedule menu that will generate a schedule report
        self.actionGenerate_Schedule_From_List = QtWidgets.QAction(FEC)
        self.actionGenerate_Schedule_From_List.setObjectName("actionGenerate_Schedule_From_List")
        #make an option in the customer menu that will generate an attendance report
        self.actionGenerate_Attendance_Report = QtWidgets.QAction(FEC)
        self.actionGenerate_Attendance_Report.setObjectName("actionGenerate_Attendance_Report")
        #add a help option to the help menu
        self.helpFunc = QtWidgets.QAction(FEC)
        self.helpFunc.setObjectName('helpFunc')
        #the following section adds the buttons to their respective menubar options
        self.menuEmployee.addAction(self.actionNewEmployee)
        self.menuEmployee.addSeparator()
        self.menuEmployee.addAction(self.actionDeleteEmployee)
        self.menuCustomer.addAction(self.actionNewCustomer)
        self.menuCustomer.addSeparator()
        self.menuCustomer.addAction(self.actionDeleteCustomer)
        self.menuCustomer.addSeparator()
        self.menuCustomer.addAction(self.actionGenerate_Attendance_Report)
        self.menuSchedule.addAction(self.actionGenerate_Schedule_From_List)
        self.menuHelp.addAction(self.helpFunc)
        self.menubar.addAction(self.menuEmployee.menuAction())
        self.menubar.addAction(self.menuCustomer.menuAction())
        self.menubar.addAction(self.menuSchedule.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        #sets the window icon to the file flame.png in the app directory
        self.setWindowIcon(QIcon('flame.png'))

        #call the retranslateUi function
        self.retranslateUi(FEC)
        #start on the first tab upon startup
        self.tabWidget.setCurrentIndex(0)
        #connect all buttons to their functions through the signals and slots method
        QtCore.QMetaObject.connectSlotsByName(FEC)

    def retranslateUi(self, FEC):
        '''This method connects all the signals and slots for the buttons and the methods'''

        #define the _translate variable as the translate method which makes strings into UTF-8
        _translate = QtCore.QCoreApplication.translate
        #Sets the title bar text as 'FEC Manager'
        FEC.setWindowTitle(_translate('FEC', 'FEC Manager'))

        #Add text to the add row button
        self.btn_AddRow.setText(_translate('FEC', 'Add Row'))
        #when the button is clicked call the addRow function
        self.btn_AddRow.clicked.connect(self.addRow)

        #Add text to the update row button
        self.btn_Update.setText(_translate('FEC', 'Update Tab'))
        #When the button is clicked call the updateRow function
        self.btn_Update.clicked.connect(self.updateRow)

        #add text to the delete row button
        self.btn_DeleteRow.setText(_translate('FEC', 'Delete Selected Row'))
        #when the button is clicked call the delete row function
        self.btn_DeleteRow.clicked.connect(self.deleteRow)

        #Set the text for the menubar tabs
        self.menuEmployee.setTitle(_translate('FEC', 'Employee'))
        self.menuCustomer.setTitle(_translate('FEC', 'Customer'))
        self.menuSchedule.setTitle(_translate('FEC', 'Schedule'))
        self.menuHelp.setTitle(_translate('FEC', 'Help'))

        #set the text of the option in the Employee menu to 'Create new'
        self.actionNewEmployee.setText(_translate('FEC', 'Create New'))
        #When its clicked call the newEmpList function
        self.actionNewEmployee.triggered.connect(self.newEmpList)

        #set the text of the 2nd option in the employee menu to 'Delete List'
        self.actionDeleteEmployee.setText(_translate('FEC', 'Delete List'))
        #when clicked call the remEmpList function
        self.actionDeleteEmployee.triggered.connect(self.remEmpList)

        #set the text of the first option in the customer menu to 'Create New'
        self.actionNewCustomer.setText(_translate('FEC', 'Create New'))
        #when clicked call the newCustList function
        self.actionNewCustomer.triggered.connect(self.newCustList)

        #set the text of the 2nd option in the customer menu to 'Delete List'
        self.actionDeleteCustomer.setText(_translate('FEC', 'Delete List'))
        #When clicked call the remCustList function
        self.actionDeleteCustomer.triggered.connect(self.remCustList)

        #set the text of the option in the schedule tab to 'Generate Schedule From List'
        self.actionGenerate_Schedule_From_List.setText(_translate('FEC', 'Generate Schedule From List'))
        #When clicked call the genSched function
        self.actionGenerate_Schedule_From_List.triggered.connect(self.genSched)

        #set the text of the 3rd option in the customer menu to 'Generate Attendance Report'
        self.actionGenerate_Attendance_Report.setText(_translate('FEC', 'Generate Attendance Report'))
        #When clicked call the genAtten function
        self.actionGenerate_Attendance_Report.triggered.connect(self.genAtten)

        #Set the text of the help menu to 'Open Help menu'
        self.helpFunc.setText(_translate('FEC', 'Open Help Window'))
        #When clicked call the helpMe function
        self.helpFunc.triggered.connect(self.helpMe)

#####################################################ALL OF THE VIEW FUNCTIONS#####################################################################
    def tabUi(self, dictionary, tabWidget, modelDict, viewDict, table, header, hide, resize):
        '''This is the general tabUi function for creating the tabs'''

        #Clear all used data structures to inizialize the function and reset it
        tabWidget.clear()
        modelDict.clear()
        viewDict.clear()

        #Create a counter variable to keep track of the index of the current tab
        n = 0
        #For every key in the tabNameDict provided, create a tab
        for key in dictionary:
            #Make a database model
            model = QtSql.QSqlTableModel()
            #Set its table to the database table passed in as an argument
            model.setTable(table)
            #Set the edit strategy so that it saves to the database immediately
            model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            #Show only the rows in the model that have the same list id as the current id in tabNameDict
            model.setFilter('list_id = %d' % (key, ) )
            #select the model to populate it with data
            model.select()
            #for every column id and name in the header dictionary, run the loop
            for num, title in header.items():
                #set the data for the headers of the column to the items in the header dictionary
                model.setHeaderData(num, QtCore.Qt.Horizontal, title)
            #Make a view widget for displaying the info in the model and making it visible and editable
            view = QtWidgets.QTableView()
            #Set the model of the view to the model created before
            view.setModel(model)
            #Create a tab to hold the view widget
            tab = QtWidgets.QWidget()
            #Add the tab to the given tab widget in the  arguments and set the text to the current value in the tabNameDict
            tabWidget.addTab(tab, dictionary[key])
            #Hide the columns in the hide tuple
            for item in hide:
                view.hideColumn(item)
            #resize the rows and their columns to fit the contents
            view.resizeRowsToContents()
            view.resizeColumnsToContents()
            #For each column id in the resize tuple, stretch it out to fit the available space
            for item in resize:
                view.horizontalHeader().setSectionResizeMode(item, QtWidgets.QHeaderView.Stretch)
            #create a layout to hold the view
            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(view)
            #set the layout of the tab to hold the view
            tab.setLayout(layout)
            #add the model to this dictionary with the current tab index as the key
            modelDict[n] = model
            #add the view to this dictionary with the current tab index as the key
            viewDict[n] = view
            #increment n by 1 to represent another tab being made
            n += 1

    def employeeTabUi(self):
        '''Creates the interactive spreadsheet in the Employee tab'''

        #names the table for use in the model
        table = 'Employee'
        #Dictionary that stores the column id and names
        header = {
            0 : 'Name',
            1 : 'Email',
            2 : 'Age',
            3 : 'id',
            4 : 'list_id',
            5 : 'monday',
            6 : 'tuesday',
            7 : 'wednesday',
            8 : 'thursday',
            9 : 'friday',
            10 : 'saturday',
            11 : 'sunday'
        }
        #Stores the ids of the columns that will be hidden
        hide = (3, 4, 5, 6, 7, 8, 9, 10, 11)
        #stores the ids of the columns that will be resized
        resize = (0, 1)
        #call thetabUi function, using tabNameDict_E to get tab names, using the employeeTabWidget created above, the dicts to store the model and view widget
        self.tabUi(self.tabNameDict_E, self.employeeTabWidget, self.employeeModels, self.employeeViews, table, header, hide, resize)

    def customerTabUi(self):
        '''Creates the interactive spreadsheet in the Customer tab'''

        #Which table to use for the model
        table = 'Customer'
        #dictionary for storing column ids and names
        header = {
            0 : 'Name',
            1 : 'Age',
            2 : 'Email',
            3 : 'Arrival Time',
            4 : 'Arrival Date',
            5 : 'id',
            6 : 'list_id'
        }
        #which column ids are to be hidden
        hide = (5, 6)
        #Which columns are to be resized
        resize = (0, 2, 3, 4)
        #call the tabUi function with the tabNameDict_C for tab names, customerTabWidget created above, and the dicts for storing the models and views
        self.tabUi(self.tabNameDict_C, self.customerTabWidget, self.customerModels, self.customerViews, table, header, hide, resize)

    def scheduleTabUi(self):
        '''Creates a schedule for each employee that is editable'''

        #which table to use for the model
        table = 'Employee'
        #Stores the column ids and the names
        header = {
            0 : 'Name',
            1 : 'Email',
            2 : 'Age',
            3 : 'id',
            4 : 'list_id',
            5 : 'Monday',
            6 : 'Tuesday',
            7 : 'Wednesday',
            8 : 'Thursday',
            9 : 'Friday',
            10 : 'Saturday',
            11 : 'Sunday'
        }
        #Which columns are to be hidden
        hide = (1, 2, 3, 4)
        #Which columns are to be resized
        resize = (0, 5, 6, 7, 8, 9, 10, 11)
        #Call the tab Ui function with tabNameDict_E to parallel tab names with employee tab, put it in the schedule tab widget, and use the dicts to store
        #the model and views used
        self.tabUi(self.tabNameDict_E, self.scheduleTabWidget, self.scheduleModels, self.scheduleViews, table, header, hide, resize)

    def attendanceTabUi(self):
        '''Creates a report that shows attendance by time of day'''

        #clear the tab to repopulate it
        self.attendanceTabWidget.clear()

        #Can only go one way through the list of values retrieved
        self.cur.setForwardOnly(True)
        #Select all the dates from Customer table
        self.cur.exec_('SELECT arrival_date FROM Customer')
        #A set can only contain unique items
        date = set()
        #Add the retrieved values to the set, but do nothing if already in set
        while self.cur.next():
            date.add(self.cur.value(0))
        #A dictionary to store x, y coordinates as key, value pairs
        coor = {}
        #Will scroll through the date set and create a graph for each date
        for i in sorted(date):
            #Clear the coordinates for the previous graphs
            coor.clear()
            #Select all the times that correspond with the current date
            self.cursor.execute('SELECT arrival_time FROM Customer WHERE arrival_date = ?', (i, ))
            #initialize population variable to 0
            pop = 0
            #initialize list of times to be empty
            times = []
            #Create a list of all the times previously retrieved
            temp = self.cursor.fetchall()
            #This for loop takes the times and converts them into decimals for graphing
            for item in temp:
                t = item[0].split()
                if t[1].upper() == 'AM' or int(t[0].split(':')[0]) == 12:
                    hour = float(t[0].split(':')[0])
                    minutes = float(t[0].split(':')[1])/60
                elif t[1].upper() == 'PM':
                    hour = float(t[0].split(':')[0]) + 12
                    minutes = float(t[0].split(':')[1])/60
                #Add the decimal to the times
                times.append(hour + minutes)
            #This for loop adds 1 to the population everytime a time is in the list
            for time in sorted(times):
                pop += 1
                #adds x, y coordinates to the coor dict as time, population pairs
                coor[time] = pop
            #adds a point at closing time
            coor[23.0] = pop
            #Create a tab for current graph
            tab = QtWidgets.QWidget()
            #add tab to attendanceTabWidget with the title as the current date
            self.attendanceTabWidget.addTab(tab, i)
            #make a layout that holds the graph
            layout = QtWidgets.QVBoxLayout()
            #add the layout to the tab
            tab.setLayout(layout)
            #Create a new series, which is a line that you add points to
            series = QLineSeries()
            #Add the coordinates from the coor dict to the series
            for x in sorted(coor):
                series.append(x, coor[x])
            #Create a chart to hold the graph
            chart = QChart()
            #make a chartview widget to dsiplay the chart
            chartView = QChartView(chart)
            #Use Antialiasing to accelerate graph rendering
            chartView.setRenderHint(QPainter.Antialiasing)
            #Add the line to the graph
            chart.addSeries(series)
            #create the x axis
            axisX = QValueAxis()
            #the domain of the function is from 8:00 to 11:00 PM
            axisX.setRange(8, 23)
            #there will be one tick per hour
            axisX.setTickCount(16)
            #The label of the axis is time
            axisX.setTitleText('Time')
            #Add the axis to the bottom of the chart
            chart.addAxis(axisX, QtCore.Qt.AlignBottom)
            #syncs the line and the axis
            series.attachAxis(axisX)
            #Create the Y axis
            axisY = QValueAxis()
            #Have only 5 ticks on the y axis
            axisY.setTickCount(5)
            #Set the label format to include numbers
            axisY.setLabelFormat('%i')
            #axis label is set to 'Population'
            axisY.setTitleText('Population')
            #Add the axis to the left of the graphs
            chart.addAxis(axisY, QtCore.Qt.AlignLeft)
            #syncs the line with the axis
            series.attachAxis(axisY)
            #hide the legend
            chart.legend().hide()
            #set the title of the graph
            chart.setTitle('Attendance Per Hour')
            #Add the chartview widget to the layout of the tab
            layout.addWidget(chartView)
            #use the global variable data

            #create a local list to hold the coordinates
            inner = []
            #scrol through the coords
            for time, population in coor.items():
                #Add a tuple of each coordinate to the inner list
                inner.append((time, population))
            #add the list of tuples to the data list
            self.data.append(inner)
###########################################################ALL OF THE MENUBAR FUNCTIONS#####################################################################################
    def newList(self, title, idlist, dictionary):
        '''General function for making a new list'''
        #a line edit is a way to gather user input in text format
        le = QtWidgets.QLineEdit()
        #These decide the buttons on the title bar of the new window
        flags = QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint
        #Gathers user data by opening a dialog that prompts for a title
        text, ok = QtWidgets.QInputDialog.getText(QWidget(), title, 'Enter List Name:', le.Normal, None, flags)
        #if the user pressed ok
        if ok:
            #add a value to idlist if it isnt empty
            try:
                idlist.append(max(idlist) + 1)
            #if the list is empty, add 1
            except:
                idlist.append(1)
            #add the title to the dictionary using the new idlist value
            dictionary[max(idlist)] = text

    def remList(self, idlist, dictionary):
        '''General function for deleting a list'''
        #decides what options appear on title bar of new window
        flags = QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint
        #list of tab available for deletion
        options = []
        #text that appears in the title
        text = 'Choose Which Tab to Delete.'
        #scrolls through the tabtitles in the tabnamedict
        for key, value in dictionary.items():
            #adds the titles to the options list
            options.append(value)
        #makes a modal dialog that has a dropdown menu for choosing which list to delete
        item, ok = QtWidgets.QInputDialog.getItem(QWidget(), text, 'Tab Name:', options, 0, False, flags)
        #if ok was pressed
        if ok:
            #create a copy of the tabnamedict
            copy = dictionary.copy()
            #Scroll through the copy and delete the selected tab from the original dict
            for key, value in  copy.items():
                if item == value:
                    del(dictionary[key])
                    try:
                        #remove tab id from idlist
                        idlist.remove(key)
                    except:
                        pass
    #function for creating a new employee list
    def newEmpList(self):
        self.newList('New Employee List', self.idList_E, self.tabNameDict_E)
        #update the two tabs
        self.employeeTabUi()
        self.scheduleTabUi()

    #function for deleting employee tab
    def remEmpList(self):
        self.remList(self.idList_E, self.tabNameDict_E)
        #update the two tabs
        self.employeeTabUi()
        self.scheduleTabUi()

    #Function for adding new customer list
    def newCustList(self):
        self.newList('New Customer List', self.idList_C, self.tabNameDict_C)
        #Update tabs
        self.customerTabUi()
        self.attendanceTabUi()

    #function for removing cutomer tabs
    def remCustList(self):
        self.remList(self.idList_C, self.tabNameDict_C)
        #update tabs
        self.customerTabUi()
        self.attendanceTabUi()

    #function for creating a pdf report of employee schedule
    def genSched(self):
        #import _sched function from report.py
        from report import _Sched
        #flags used for file selection dialog
        flags = QtWidgets.QFileDialog.ShowDirsOnly
        #launch dialog for selecting a directory
        directory = QtWidgets.QFileDialog.getSaveFileName(None, 'Choose Directory', '', '', '', flags)
        #if cancel was pressed, stop function
        if directory[0] == '':
            return
        #select the directory text only
        directory = directory[0]
        #add pdf file extension if not included
        if '.pdf' not in directory:
            directory = directory + '.pdf'
        #select all schedule data from database
        self.cursor.execute('SELECT UPPER(name), monday, tuesday, wednesday, thursday, friday, saturday, sunday FROM Employee ORDER BY UPPER(name)')
        data = self.cursor.fetchall()
        #run the generation function to make pdf
        try:
            _Sched(directory, data)
        except:
            pass

    #function for making attendance report
    def genAtten(self):
        #use global variable data
        global data
        #import attendance generation function from report.py
        from report import _Atten
        #flags for file dialog
        flags = QtWidgets.QFileDialog.ShowDirsOnly
        #dialog for choosing directory to put pdf file
        directory = QtWidgets.QFileDialog.getSaveFileName(None, 'Choose Directory', '', '', '', flags)
        #if cancel is pressed stop function
        if directory[0] == '':
            return
        #select only the directory text
        directory = directory[0]
        #append pdf file extension if not there
        if '.pdf' not in directory:
            directory = directory + '.pdf'
        #call pdf generation function
        _Atten(directory, data)

    def helpMe(self):
        #import help class window from help.py
        from help import Ui_Help
        #make variable global so window doesn't close immediately
        global win
        #create an instance of help window
        win = Ui_Help()
        #show it
        win.show()

########################################THE THREE MAIN USER FUNCTIONS########################################################################################################
    def addRow(self):

        #Error message function if something goes wrong
        def msgFunc(text):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText(text)
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.setWindowTitle('Error')
            msgBox.exec_()

        #finds current index of original tab widget
        index = self.tabWidget.currentIndex()
        #adds row based on current tab index and which tab the user is currently in
        if index == 0:
            try:
                self.cursor.execute('INSERT INTO Employee (name, email, age, list_id) VALUES ("", "", "", ?)', (self.idList_E[self.employeeTabWidget.currentIndex()], ) )
                self.conn.commit()
                self.employeeModels[self.employeeTabWidget.currentIndex()].select()
                self.scheduleModels[self.employeeTabWidget.currentIndex()].select()
            except:
                text = 'Please create a new list in the Employee menu before adding a row.'
                msgFunc(text)

        elif index == 1:
            try:
                #This inserts current datetime into table automatically
                dt = str(datetime.datetime.now())
                dt = dt.split()
                t = dt[1].split(':')
                t.remove(t[2])
                if int(t[0]) > 12:
                    t[0] = str(int(t[0]) - 12)
                    t[1] = t[1] + ' PM'
                else:
                    t[1] = t[1] + ' AM'

                curtime = t[0] + ':' + t[1]
                self.cursor.execute('INSERT INTO Customer (name, age, email, arrival_time, arrival_date, list_id) VALUES ("", "", "", ?, ?, ?)', (curtime, dt[0], self.idList_C[self.customerTabWidget.currentIndex()],) )
                self.conn.commit()
                self.customerModels[self.customerTabWidget.currentIndex()].select()
                self.attendanceTabUi()
            except:
                text = 'Please create a new list in the Customer menu before adding a row.'
                msgFunc(text)

        elif index == 2:
            try:
                self.cursor.execute('INSERT INTO Employee (name, email, age, list_id) VALUES ("", "", "", ?)', (self.idList_E[self.scheduleTabWidget.currentIndex()], ))
                self.conn.commit()
                self.employeeModels[self.scheduleTabWidget.currentIndex()].select()
                self.scheduleModels[self.scheduleTabWidget.currentIndex()].select()
            except:
                text = 'Please create a new list in the Employee menu before adding a row.'
                msgFunc(text)

    #this function just calls the corresponding ui function to update the tab based on current index
    def updateRow(self):
        index = self.tabWidget.currentIndex()
        if index == 0:
            self.employeeTabUi()
        elif index == 1:
            self.customerTabUi()
        elif index == 2:
            self.scheduleTabUi()
        elif index == 3:
            self.attendanceTabUi()
#This function deletes the current row
    def deleteRow(self):

        #General deletion function for each tab
        def anyIndex(viewDict, modelDict, tabWidget):
            selectModel = viewDict[tabWidget.currentIndex()].selectionModel()
            currentSelect = selectModel.selectedIndexes()
            modelDict[tabWidget.currentIndex()].removeRows(currentSelect[0].row(), len(currentSelect))
            modelDict[tabWidget.currentIndex()].select()

        #applies deletion function based on current index
        index = self.tabWidget.currentIndex()
        if index == 0:
            try:
                anyIndex(self.employeeViews, self.employeeModels, self.employeeTabWidget)
            except:
                pass
        elif index == 1:
            try:
                anyIndex(self.customerViews, self.customerModels, self.customerTabWidget)
            except:
                pass
        elif index == 2:
            try:
                anyIndex(self.scheduleViews, self.scheduleModels, self.scheduleTabWidget)
            except:
                pass

#saves tab titles to pickle file
    def uponEnd(self):
        with open(self.fec + '.pickle', 'wb') as outputFile:
            pickle.dump(self.tabNameDict_E, outputFile, -1)
            pickle.dump(self.tabNameDict_C, outputFile, -1)

#garbage collect function
    def collect(self):
        gc.collect()
