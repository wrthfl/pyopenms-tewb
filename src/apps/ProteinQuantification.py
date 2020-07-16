import sys, os
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow, \
     QDesktopWidget, QWidget, QTabWidget, QAction, QPushButton, QInputDialog, \
     QMessageBox
from PyQt5.QtCore import pyqtSlot
sys.path.append(os.getcwd()+'/../view')
from GUI_FastaViewer import GUI_FastaViewer
from ConfigView import ConfigView
from mzMLTableView import mzMLTableView
from SpecViewer import Specviewer
from mzTabLoadWidget import mzTabLoadWidget


class ProteinQuantification(QMainWindow):
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
        fview = GUI_FastaViewer()
        xview = mzTabLoadWidget()

        view.addTab(cview, 'XML-Viewer')
        view.addTab(tview, 'Experimental-Design')
        view.addTab(fview, 'Fasta-Viewer')
        view.addTab(sview, 'Spec-Viewer')
        view.addTab(xview, 'mzTabViewer')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        projectMenu = menubar.addMenu('Project')
        parametersMenu = menubar.addMenu('Parameters')
        saveAction = QAction("&Save project", self)
        runAction = QAction("&Run in Terminal", self)
        Threads = QAction("&Adjust the Threadnumber", self)
        FDR = QAction("&Adjust the protein FDR", self)

        saveAction.setDisabled(True)
        # runAction.setDisabled(True)

        projectMenu.addAction(runAction)
        projectMenu.addAction(saveAction)
        parametersMenu.addAction(Threads)
        parametersMenu.addAction(FDR)

        runAction.triggered.connect(self.runFunktion)
        FDR.triggered.connect(self.adjustFDR)
        Threads.triggered.connect(self.adjustThreads)

        self.initDefaultValues()

        self.setCentralWidget(view)
        self.resize(1280, 720)
        self.center()
        self.setWindowTitle('Protein Quantification')
        self.show()

    def center(self):
        """
        centers the widget to the screen
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initDefaultValues(self):
        self.threads = 1
        self.fdr = 0.3
        self.procdone = False

    def adjustFDR(self):
        newfdr, ok = QInputDialog.getDouble(
            self, "Adjust the value for the protein FDR",
            "Please specify a double as new FDR value")
        if ok:
            if newfdr > 0:
                if newfdr <= 1:
                    self.fdr = newfdr
                else:
                    QMessageBox.about(self, "Warning",
                                      "Please specify a value" +
                                      "between 0.0 and 1.0 for the FDR.")
            else:
                QMessageBox.about(self, "Warning",
                                  "Please specify a positive" +
                                  "value for the FDR.")

    def adjustThreads(self):
        newthreads, ok = QInputDialog.getInt(
            self, "Adjust the number of threads",
            "Please specify the number of threads for the processing")
        if ok:
            if newthreads > 0:
                self.threads = newthreads
            else:
                QMessageBox.about(self, "Warning",
                                  "Please specify a positive" +
                                  "number of threads.")

    def runFunktion(self):
        """
        runs the work from the GUI in a Terminal
        """
        self.procdone = False
        outfileprefix, ok = QInputDialog.getText(self,
                                                 "Prefix for outputfiles",
                                                 "Please specify a prefix " +
                                                 "for the outputfiles")
        if ok:
            projectfolder = "../data_ProtQuantification"
            mzMLfiles = ["BSA1_F1.mzML", "BSA1_F2.mzML", "BSA2_F1.mzML",
                         "BSA2_F2.mzML", "BSA3_F1.mzML", "BSA3_F2.mzML"]
            idXMLfiles = ["BSA1_F1.idXML", "BSA1_F2.idXML ", "BSA2_F1.idXML ",
                          "BSA2_F2.idXML ", "BSA3_F1.idXML ", "BSA3_F2.idXML "]
            expdesign = "BSA_design.tsv"
            dbfasta = "18Protein_SoCe_Tr_detergents_trace_target_decoy.fasta"
            inifile = "OpenPepXLLF_input2.ini"
            runcall = "ProteomicsLFQ "
            mzMLs = "-in " + " ".join(mzMLfiles)
            idXMLs = " -ids " + " ".join(idXMLfiles)
            design = "-design " + expdesign + " "
            refdb = "-fasta " + dbfasta + " "
            configini = "-ini " + inifile + " "
            threads = "-threads " + str(self.threads) + " "
            fdr = "-proteinFDR " + str(self.fdr) + " "
            out = ("-out_cxml " + outfileprefix + ".consensusXML.tmp " +
                   "-out_msstats " + outfileprefix + ".csv.tmp " +
                   "-out " + outfileprefix + ".mzTab.tmp")
            command = (runcall + mzMLs + idXMLs + design +
                       refdb + configini + threads + fdr + out)
            os.chdir(projectfolder)
            os.system(command)
            self.procdone = True
            QMessageBox.about(self, "Information", "Processing has been " +
                              "performed and outputfiles saved to " +
                              "projectfolder")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ProteinQuantification()
    sys.exit(app.exec_())
