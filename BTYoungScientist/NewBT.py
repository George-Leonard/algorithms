from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import sqlite3
import pandas as pd
import pathlib
import importlib.util

calculatorsLoaded = []
class Ui_MainWindow(object):

    def ImportClicked(self):
        print('Import MenuItem Clicked')

    def ExportClicked(self):
        print('Export MenuItem Clicked')

    def CalcErrorClicked(self):
        print('CalcErrorClicked MenuItem Clicked')
        msg = QMessageBox()
        msg.setWindowTitle('Calculator Loading Error')
        msg.setText('''
            - Ensure a function, 'calculate' is defined 
              in the python calculator

            - Check calculator for errors

            - Ensure compliant data transfer 
            (i.e equal frame sizes)
            ''')
        msg.exec_()
        
    def updateTable(self,df):
        print(df)
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setColumnCount(len(df.columns))
        self.tableWidget.setRowCount(len(df.index))
        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                self.tableWidget.setItem(i,j,QTableWidgetItem(str(df.iloc[i, j])))

        columns = []
        for column in df.columns:
            print(column)
            columns.append(column)
                
        self.tableWidget.setHorizontalHeaderLabels(columns)
        self.labelCalcLoaded.setText(_translate('MainWindow', str(calculatorsLoaded)))

    def linkClicked(self):

        print('Link MenuItem Clicked')

        #Open any calculator, and access classes and functions within //
        #standard function should ALWAYS be defined as calculate(filename)
        try:
            dlg = QtWidgets.QFileDialog
            path = dlg.getOpenFileName()
            calc = str(path[0])
                
            calcp = pathlib.PurePath(calc)
            program = calcp.name
            calculatorsLoaded.append(program)

            programname = program.replace('.py','')

            if 'py' in program and program.endswith('.py'):
                print(program)
            else:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Must be a .py calculator')
                error_dialog.exec_()

            spec = importlib.util.spec_from_file_location(str(program), str(calc))
            calculator = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(calculator)

        except Exception as e:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('No calculator selected')
            error_dialog.exec_()


        #Now a database from the provided database should be created
        #This database should only include the rows for the NULL values in the diabetes column,
        #and factors required by the calculator

        try:
            
            percentages = calculator.calculate(df)
            
            print(percentages)
            
        except Exception as e:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('No calculate function found in selected calculator')
            error_dialog.exec_()

        try:
            percentages = pd.Series(percentages)
            data = pd.DataFrame(data = df)
            data[str(programname)] = percentages
            self.updateTable(data)

        except Exception as e:
            print(e)
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('No database inputted')
            error_dialog.exec_()


    def loadData(self):

        print('Import PushButton Clicked')
        global df

        path = str(self.lineEdit_2.text())
        table = str(self.lineEdit.text())
        print(path,"+",table)


        try:
            conn = sqlite3.connect(path)
            query = "SELECT * FROM %s" %(table)
            result = conn.execute(query)

            
            df = pd.read_sql_query(query,conn)
            count = 0
            for i in df:
                count = count+1
            self.tableWidget.setColumnCount(count)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            columns = []
            
            for column in df.columns:
                print(column)
                columns.append(column)
                
            self.tableWidget.setHorizontalHeaderLabels(columns)

            conn.close()
        except Exception as e:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Cannot load database')
            error_dialog.exec_()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 761, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(92, 10, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 40, 281, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 40, 121, 21))
        self.pushButton.setObjectName("pushButton")
        try:
            self.pushButton.clicked.connect(lambda: self.loadData())
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Cannot load database')
            error_dialog.exec_()
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 51, 16))
        self.label_2.setObjectName("label_2")
        self.labelCalcLoaded = QtWidgets.QLabel(self.centralwidget)
        self.labelCalcLoaded.setGeometry(QtCore.QRect(601,10,150,50))
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        self.menuCalculators = QtWidgets.QMenu(self.menubar)
        self.menuCalculators.setObjectName("menuCalculators")
        
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.actionCalcError = QtWidgets.QAction(MainWindow)
        self.menuHelp.addAction(self.actionCalcError)
        self.actionCalcError.triggered.connect(self.CalcErrorClicked) 
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionImport_Database = QtWidgets.QAction(MainWindow)
        self.actionImport_Database.setObjectName("actionImport_Database")
        self.actionExport_Database = QtWidgets.QAction(MainWindow)
        self.actionExport_Database.setObjectName("actionExport_Database")
        
        self.actionLink = QtWidgets.QAction(MainWindow)
        self.actionLink.setObjectName("actionLink")

        self.menuFile.addAction(self.actionImport_Database)
        self.actionImport_Database.triggered.connect(self.ImportClicked)        

        
        self.menuFile.addAction(self.actionExport_Database)
        self.actionExport_Database.triggered.connect(self.ExportClicked)
        
        self.menuCalculators.addAction(self.actionLink)
        self.actionLink.triggered.connect(self.linkClicked)
        
        self.menuCalculators.addSeparator()
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCalculators.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Import"))
        self.label.setText(_translate("MainWindow", "SQL Table"))
        self.label_2.setText(_translate("MainWindow", "File Path"))
        self.labelCalcLoaded.setText(_translate('MainWindow', 'loaded: '+str(calculatorsLoaded)))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuCalculators.setTitle(_translate("MainWindow", "Calculators"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionCalcError.setText(_translate('MainWindow', 'Calculator loading error'))
        self.actionImport_Database.setText(_translate("MainWindow", "Import Database"))
        self.actionExport_Database.setText(_translate("MainWindow", "Export Database"))
        self.actionLink.setText(_translate("MainWindow", "Link..."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
