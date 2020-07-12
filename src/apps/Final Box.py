import sys, os
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow, \
     QDesktopWidget, QWidget, QTabWidget, QAction, QPushButton
from PyQt5.QtCore import pyqtSlot
sys.path.append(os.getcwd()+'/../view')
from FastaViewer import FastaViewer
from ConfigView import ConfigView
from mzMLTableView import mzMLTableView
from SpecViewer import Specviewer


class FinalBox(QMainWindow):
    """
    Application to use different Widgets in one Window
    """

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        '''
        sets the window with all applications and widgets
        '''
        view = QTabWidget()
        cview = ConfigView()
        tview = mzMLTableView()
        sview = Specviewer()
        fview = FastaViewer()
        # xview = ()

        view.addTab(cview, 'XML-Viewer')
        view.addTab(tview, 'Experimental-Design')
        view.addTab(fview, 'Fasta-Viewer')
        view.addTab(sview, 'Spec-Viewer')
        # view.addTab(xView, 'Viewer')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        runMenu = menubar.addMenu('&Run')
        saveAction = QAction("&Save File", self)
        loadAction = QAction("&Load File", self)
        runAction = QAction("&Run in Terminal", self)

        saveAction.setDisabled(True)
        loadAction.setDisabled(True)

        fileMenu.addAction(loadAction)
        fileMenu.addAction(saveAction)
        runMenu.addAction(runAction)

        '''
        Hier muss noch vlt ein conditional hin sodass
        die connections sich für das aktuelle tab jeweils
        ändern
        '''
        # loadAction.triggered.connect(cview.openXML)
        # saveAction.triggered.connect(cview.saveFile)
        runAction.triggered.connect(self.runFunktion)

        self.setCentralWidget(view)
        self.resize(1280, 720)
        self.center()
        self.setWindowTitle('Final Box')
        self.show()

    def center(self):
        """
        centers the widget to the screen
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def runFunktion(self):
        """
        runs the work from the GUI in a Terminal
        """
        c1 = "ProteomicsLFQ -in "
        c2 = "BSA1_F1.mzML "
        c3 = "BSA1_F2.mzML "
        c4 = "BSA2_F1.mzML "
        c5 = "BSA2_F2.mzML "
        c6 = "BSA3_F1.mzML "
        c7 = "BSA3_F2.mzML "
        c8 = "-ids "
        c9 = "BSA1_F1.idXML "
        c10 = "BSA1_F2.idXML "
        c11 = "BSA2_F1.idXML "
        c12 = "BSA2_F2.idXML "
        c13 = "BSA3_F1.idXML "
        c14 = "BSA3_F2.idXML "
        c15 = "-design BSA_design.tsv "
        c16 = "-fasta 18Protein_SoCe_Tr_detergents_trace_target_decoy.fasta "
        c17 = "-Alignment:max_rt_shift 0 "
        c18 = "-targeted_only true "
        c19 = "-transfer_ids false "
        c20 = "-mass_recalibration false "
        c21 = "-out_cxml BSA.consensusXML.tmp "
        c22 = "-out_msstats BSA.csv.tmp "
        c23 = "-out BSA.mzTab.tmp "
        c24 = "-threads 1 "
        c25 = "-proteinFDR 0.3"
        l15 = c1 + c2 + c3 + c4 + c5
        l610 = c6 + c7 + c8 + c9 + c10
        l1115 = c11 + c12 + c13 + c14 + c15
        l1620 = c16 + c17 + c18 + c19 + c20
        l2125 = c21 + c22 + c23 + c24 + c25
        command = l15 + l610 + l1115 + l1620 + l2125
        # command1 = "ping google.com"
        os.system(command)
        print("All has been executed!")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = FinalBox()
    sys.exit(app.exec_())
