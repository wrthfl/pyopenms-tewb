from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QFileDialog,\
    QPushButton, QHBoxLayout, QDesktopWidget, QMainWindow, QPlainTextEdit, QCheckBox
from PyQt5.QtCore import Qt
import xml.etree.ElementTree as ET


class ConfigView(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        self.tree = ET.ElementTree
        self.header = ['name', 'value', 'type', 'restrictions']
        self.descriptions = {}

        self.treeWidget = QTreeWidget(self)
        self.treeWidget.setHeaderLabels(self.header)

        btns = QWidget(self)
        lower = QWidget(self)
        loadbtn = QPushButton('Load')
        savebtn = QPushButton('Save')
        loadbtn.clicked.connect(self.openXML)
        savebtn.clicked.connect(self.saveFile)
        self.checkbox = QCheckBox('Show advanced parameters')
        self.checkbox.setChecked(True)
        self.checkbox.stateChanged.connect(self.drawTree)

        self.textbox = QPlainTextEdit(self)
        self.textbox.setReadOnly(True)

        btnlayout = QVBoxLayout()
        lowerlayout = QHBoxLayout()
        layout = QVBoxLayout()

        btnlayout.addWidget(loadbtn)
        btnlayout.addWidget(savebtn)
        btnlayout.addWidget(self.checkbox)
        btns.setLayout(btnlayout)

        lowerlayout.addWidget(btns, 1)
        lowerlayout.addWidget(self.textbox, 9)
        lower.setLayout(lowerlayout)
        layout.addWidget(self.treeWidget, 3)
        layout.addWidget(lower, 1)

        self.setLayout(layout)
        self.resize(500, 720)

    def openXML(self):
        '''
        cancel lässt die app crashen
        '''
        file, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "",
            "All Files (*);;xml (*.xml)")
        self.tree = ET.parse(file)
        self.drawTree()

    def generateTreeWidgetItem(self, item):
        treeitem = QTreeWidgetItem()
        try:
            treeitem.setText(0, item.attrib['name'])
        except KeyError:
            pass
        try:
            treeitem.setText(1, item.attrib['value'])
        except KeyError:
            pass
        try:
            treeitem.setText(2, item.attrib['type'])
        except KeyError:
            pass
        try:
            treeitem.setText(3, item.attrib['restrictions'])
        except KeyError:
            pass
        try:
            self.descriptions[item.attrib['name']] = item.attrib['description']
        except KeyError:
            pass

        return treeitem

    def drawTree(self):
        try:
            self.treeWidget.clear()
            root = self.tree.getroot()
            for child in root:
                childitem = self.generateTreeWidgetItem(child)
                self.treeWidget.addTopLevelItem(childitem)
                for sub1child in child:
                    if self.checkbox.isChecked:
                        sub1childitem = self.generateTreeWidgetItem(sub1child)
                        childitem.addChild(sub1childitem)
                    else:
                        if sub1child.attrib['advanced'] == 'false':
                            sub1childitem = self.generateTreeWidgetItem(sub1child)
                            childitem.addChild(sub1childitem)

                    for sub2child in sub1child:
                        if self.checkbox.isChecked:
                            sub2childitem = self.generateTreeWidgetItem(sub2child)
                            sub1childitem.addChild(sub2childitem)
                        else:
                            if sub2child.attrib['advanced'] == 'false':
                                sub2childitem = (
                                    self.generateTreeWidgetItem(sub2child))
                                sub1childitem.addChild(sub2childitem)

                        for sub3child in sub2child:
                            if self.checkbox.isChecked:
                                sub3childitem = (
                                    self.generateTreeWidgetItem(sub3child))
                                sub2childitem.addChild(sub3childitem)
                            else:
                                if sub3child.attrib['advanced'] == 'false':
                                    sub3childitem = (
                                        self.generateTreeWidgetItem(sub3child))
                                    sub2childitem.addChild(sub3childitem)

                            for sub4child in sub3child:
                                if self.checkbox.isChecked:
                                    sub4childitem = (
                                        self.generateTreeWidgetItem(sub4child))
                                    sub3childitem.addChild(sub4childitem)
                                else:
                                    if sub4child.attrib['advanced'] == 'false':
                                        sub4childitem = (
                                            self.generateTreeWidgetItem(sub4child))
                                        sub3childitem.addChild(sub4childitem)
        except TypeError:
            pass

    def loadDescription(self):
        getSelected = self.treeWidget.selectedItems()
        if getSelected:
            try:
                node = getSelected[0].text(0)
                self.textbox.setPlainText(self.descriptions[node])
            except KeyError:
                node = getSelected[0].parent().text(0)
                self.textbox.setPlainText(self.descriptions[node])

    def saveFile(self):
        print('sollte noch speichern')
