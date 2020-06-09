import os
import sys
import pandas as pd
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QVBoxLayout, QCheckBox
sys.path.append(os.getcwd() + '/../controller')
from filehandler import FileHandler as fh
sys.path.append(os.getcwd() + '/../model')
from tableDataFrame import TableDataFrame as Tdf


class OverallView(QWidget):
    
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        buttonlayout = QVBoxLayout()
        layout = QHBoxLayout()
        self.tdf = Tdf
        buttons = QWidget()
        self.table = QTableWidget()
        self.df = pd.DataFrame()
        # Buttons
        ImportBtn = QPushButton('Import')
        ExportBtn = QPushButton('Export')
        LoadBtn = QPushButton('Load')
        SaveBtn = QPushButton('Save')
        LabelBtn = QPushButton('Label')
        GroupBtn = QPushButton('Group')
        SearchBtn = QPushButton('Search')
        LoadFileBtn = QPushButton('AddFile')

        buttonlayout.addWidget(LoadBtn)
        buttonlayout.addWidget(SaveBtn)
        buttonlayout.addWidget(LabelBtn)
        buttonlayout.addWidget(GroupBtn)
        buttonlayout.addWidget(SearchBtn)
        buttonlayout.addWidget(LoadFileBtn)
        buttonlayout.addWidget(ImportBtn)
        buttonlayout.addWidget(ExportBtn)

        buttons.setLayout(buttonlayout)

        buttons.resize(200, 690)

        # Buttonconnections
        LoadBtn.clicked.connect(self.loadBtnFn)
        LoadFileBtn.clicked.connect(self.loadFile)
        ImportBtn.clicked.connect(self.importBtn)
        ExportBtn.clicked.connect(self.exportBtn)

        # Table
        self.table.setRowCount(10)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['', 'Fraction_Group', 'Fraction', 'Filename',
                'Label', 'Sample', ''])

        # Fügt zu jeder Zeile einen Edit Button hinzu
        #for index in range(self.table.rowCount()):
        #    editBtn = QPushButton('Edit')
        #    self.table.setCellWidget(index, 6, editBtn)
        # test textwindow:



        # Fügt zu jeder Zeile eine Checkbox hinzu
        for index in range(self.table.rowCount()):
            CHBX = QCheckBox()
            self.table.setCellWidget(index, 0, CHBX)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)

        # setzte die Widgets ins gewünschte layout rein
        layout.addWidget(self.table)
        layout.addWidget(buttons)

        self.setLayout(layout)

        self.resize(1280, 720)
    def initUI(self):
        """
        initializes Ui Elements
        """
    def setButtonLayout(self):
        """
        sets layout for buttons
        """
    def setTableLayout(self):
        """
        sets table layout
        """



    def drawTable(self,tabledf,filePath):
        """
        draws a table witha given dataframe and filepath
        """
        rowSize = len(tabledf.index)
        columSize = len(tabledf.columns)
        for i in range(rowSize):
            for j in range(columSize):
                if j == 2:
                    name = str(tabledf.iloc[i, j])[len(filePath):]
                    self.table.setItem(i, j+1, QTableWidgetItem(name))
                else:
                    self.table.setItem(i, j+1, QTableWidgetItem(tabledf.iloc[i, j]))

    def importBtn(self):
        """
        import button handler
        """
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;tsv (*.tsv);; csv (*.csv)", options=options)
        df = fh.importTable(self, file)
        Tdf.setTable(self,df)
        self.drawTable(df,file)

    def exportBtn(self):
        """
        export button handler
        """
        options = QFileDialog.Options()
        file, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()", "","All Files (*);;tsv (*.tsv);; csv (*.csv)", options=options)
        df = Tdf.getTable(self)
        
        temp = file.split("/")
        fileName = temp[len(temp)-1] 
        ftype = fileName.split(".")[1]
        fh.exportTable(self,df, fileName, ftype)

    def loadBtnFn(self):
        """
        provides a dialog to get the path for a directory
        """
        dlg = QFileDialog(self)
        filePath = dlg.getExistingDirectory()
        Files = fh.getFiles(self, filePath)
        delimiters = ["_"]
        preparedFiles = fh.tagfiles(self, Files, delimiters[0])
        rawTable = fh.createRawTable(self, preparedFiles, filePath)
        self.drawTable(rawTable,filePath)
        Tdf.setTable(self,rawTable)
        

    def loadFile(self):
        """
        provides a filedialog to load an additional file to the dataframe
        """
        ftype = "*.mzML"
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;mzML Files (*.mzML)", options=options)
        cdf = Tdf.getTable(self)
        filelist =[]
        filePath = file.rsplit("/",1)[0]
        temp = file.split("/")
        fileName = temp[len(temp)-1] 
        if file:
            #print(file)
            filelist.append(fileName)
            tagged_file = fh.tagfiles(self, filelist)
            df =fh.createRawTable(self,tagged_file, filePath)
            
            ndf= cdf.append(df)

            Tdf.setTable(self,ndf)
            self.drawTable(ndf, filePath)
        else: 
            return False



        # print(len(rawTable.columns))
        # print(len(rawTable.index))
        # print('Fraction_Group' + str(rawTable.iloc[1, 0]))
        # print('Fraction' + str(rawTable.iloc[1, 1]))
        # print('Filename' + name)
        # print('Label' + str(rawTable.iloc[1, 3]))
        # print('Sample' + str(rawTable.iloc[1, 4]))
        # print(rawTable)
