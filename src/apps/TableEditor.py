import sys, os
import timeit
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QMessageBox
from PyQt5.QtCore import Qt
sys.path.append(os.getcwd()+'/../view')
from mzMLTableView import mzMLTableView


class TableEditor(QMainWindow):

    def __init__(self):
        self.testForTime = False
        if self.testForTime:
            starttime = timeit.default_timer()
            print("Starttime of overall Initiation : ", starttime)
        QMainWindow.__init__(self)
        self.initUI()
        self.setAcceptDrops(True)

    def initUI(self):
        '''
        sets the window with all applications and widgets
        '''
        view = mzMLTableView(self)

        self.setCentralWidget(view)

        self.resize(1280, 720)
        self.center()
        self.setWindowTitle('ExperimentalDesign')
        self.show()

    def center(self):
        """
        centers the widget to the screen
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def dragEnterEvent(self, event):
        e = event
        data = e.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == "file":
            e.acceptProposedAction()
        else:
            e.ignore() 
        

    def dragMoveEvent(self, event):
        e = event
        data = e.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == "file":
            e.acceptProposedAction()
        else:
            e.ignore() 

    def dropEvent(self, event):
        e = event
        data = e.mimeData()
        urls = data.urls()
        #self.df = mzMLTableView.df
        if urls and urls[0].scheme() == "file":
            filepath = str(urls[0].path())[1:]
            if filepath[-4:] == "mzML":
                mzMLTableView.loadFile(self,filepath)
            else:
                dialog = QMessageBox()
                dialog.setWindowTitle("Error: Invalid File")
                dialog.setText("Please only use .mzML files")
                dialog.setIcon(QMessageBox.Warning)
                dialog.exec_()
        else:
            e.ignore() 


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = TableEditor()
    sys.exit(app.exec_())
