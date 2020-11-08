import math
import numpy as np
import random
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtGui, QtWidgets

from earth import Earth
from tempImg import BuildTempsImage


class Ui_MainWindow(object):
    DEFAULT_CELL_NUMBERS = 121
    DEFAULT_ALBEDO_CLOUD = 0.2
    DEFAULT_GREEN_HOUSE = 0.2
    DEFAULT_INITIAL_TEMP = 273

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 650)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grpInitialParameters = QtWidgets.QGroupBox(self.centralwidget)
        self.grpInitialParameters.setGeometry(QtCore.QRect(10, 10, 191, 181))
        self.grpInitialParameters.setObjectName("grpInitialParameters")
        self.txtNbCell = QtWidgets.QTextEdit(self.grpInitialParameters)
        self.txtNbCell.setGeometry(QtCore.QRect(130, 20, 51, 20))
        self.txtNbCell.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtNbCell.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.txtNbCell.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtNbCell.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtNbCell.setObjectName("txtNbCell")
        self.txtTempInit = QtWidgets.QTextEdit(self.grpInitialParameters)
        self.txtTempInit.setGeometry(QtCore.QRect(130, 110, 51, 20))
        self.txtTempInit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtTempInit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.txtTempInit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtTempInit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtTempInit.setTabChangesFocus(False)
        self.txtTempInit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.txtTempInit.setObjectName("txtTempInit")
        self.lblAlbedoCloud = QtWidgets.QLabel(self.grpInitialParameters)
        self.lblAlbedoCloud.setGeometry(QtCore.QRect(10, 50, 91, 20))
        self.lblAlbedoCloud.setObjectName("lblAlbedoCloud")
        self.txtAlbedo = QtWidgets.QTextEdit(self.grpInitialParameters)
        self.txtAlbedo.setGeometry(QtCore.QRect(130, 50, 51, 20))
        self.txtAlbedo.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtAlbedo.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.txtAlbedo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtAlbedo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtAlbedo.setObjectName("txtAlbedo")
        self.lblNbCell = QtWidgets.QLabel(self.grpInitialParameters)
        self.lblNbCell.setGeometry(QtCore.QRect(10, 20, 81, 20))
        self.lblNbCell.setObjectName("lblNbCell")
        self.lblGreenHouse = QtWidgets.QLabel(self.grpInitialParameters)
        self.lblGreenHouse.setGeometry(QtCore.QRect(10, 80, 121, 21))
        self.lblGreenHouse.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblGreenHouse.setAutoFillBackground(False)
        self.lblGreenHouse.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblGreenHouse.setTextFormat(QtCore.Qt.AutoText)
        self.lblGreenHouse.setIndent(1)
        self.lblGreenHouse.setObjectName("lblGreenHouse")
        self.txtGreenHouse = QtWidgets.QTextEdit(self.grpInitialParameters)
        self.txtGreenHouse.setGeometry(QtCore.QRect(130, 80, 51, 20))
        self.txtGreenHouse.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtGreenHouse.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.txtGreenHouse.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtGreenHouse.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtGreenHouse.setObjectName("txtGreenHouse")
        self.btnStart = QtWidgets.QPushButton(self.grpInitialParameters)
        self.btnStart.setGeometry(QtCore.QRect(50, 140, 91, 31))
        self.btnStart.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnStart.setObjectName("btnStart")
        self.lblTempInit = QtWidgets.QLabel(self.grpInitialParameters)
        self.lblTempInit.setGeometry(QtCore.QRect(10, 110, 121, 21))
        self.lblTempInit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTempInit.setAutoFillBackground(False)
        self.lblTempInit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblTempInit.setTextFormat(QtCore.Qt.AutoText)
        self.lblTempInit.setIndent(1)
        self.lblTempInit.setObjectName("lblTempInit")
        self.grpIterCtrl = QtWidgets.QGroupBox(self.centralwidget)
        self.grpIterCtrl.setGeometry(QtCore.QRect(220, 10, 331, 51))
        self.grpIterCtrl.setObjectName("grpIterCtrl")
        self.btnPlusOneIter = QtWidgets.QPushButton(self.grpIterCtrl)
        self.btnPlusOneIter.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.btnPlusOneIter.setObjectName("btnPlusOneIter")
        self.btnPlusFiveIter = QtWidgets.QPushButton(self.grpIterCtrl)
        self.btnPlusFiveIter.setGeometry(QtCore.QRect(90, 20, 75, 23))
        self.btnPlusFiveIter.setObjectName("btnPlusFiveIter")
        self.btnPlusTenIter = QtWidgets.QPushButton(self.grpIterCtrl)
        self.btnPlusTenIter.setGeometry(QtCore.QRect(170, 20, 75, 23))
        self.btnPlusTenIter.setObjectName("btnPlusTenIter")
        self.btnPlusHundredIter = QtWidgets.QPushButton(self.grpIterCtrl)
        self.btnPlusHundredIter.setGeometry(QtCore.QRect(250, 20, 75, 23))
        self.btnPlusHundredIter.setObjectName("btnPlusHundredIter")
        self.grpCurrentIter = QtWidgets.QGroupBox(self.centralwidget)
        self.grpCurrentIter.setGeometry(QtCore.QRect(220, 80, 331, 111))
        self.grpCurrentIter.setObjectName("grpCurrentIter")
        self.graphCurrent = DynamicMplCanvas(self.centralwidget)
        self.graphCurrent.setGeometry(QtCore.QRect(10, 200, 500, 200))
        self.graphCurrent.setObjectName("graphCurrent")
        self.graphOverall = DynamicMplCanvas(self.centralwidget)
        self.graphOverall.setGeometry(QtCore.QRect(10, 420, 500, 200))
        self.graphOverall.setObjectName("graphOverall")
        self.graphCurrent.axes.set_title('Current temperature in Kelvin depending on the zone')
        self.graphOverall.axes.set_title('Overall temperature in Kelvin depending on the zone')
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.currGraphImage = QtWidgets.QLabel(self.centralwidget)
        self.currGraphImage.setScaledContents(True)
        #self.currGraphImage.rotate(-90)

        # Initial values
        self.txtNbCell.setText(str(self.DEFAULT_CELL_NUMBERS))
        self.txtAlbedo.setText(str(self.DEFAULT_ALBEDO_CLOUD))
        self.txtGreenHouse.setText(str(self.DEFAULT_GREEN_HOUSE))
        self.txtTempInit.setText(str(self.DEFAULT_INITIAL_TEMP))

        self.grpIterCtrl.setEnabled(False)
        self.grpCurrentIter.setEnabled(False)
        self.graphCurrent.hide()
        self.graphOverall.hide()

        # Events
        self.btnStart.clicked.connect(self.startSimulation)
        self.btnPlusOneIter.clicked.connect(self.handlerBtnPlusOne)
        self.btnPlusFiveIter.clicked.connect(self.handlerBtnPlusFive)
        self.btnPlusTenIter.clicked.connect(self.handlerBtnPlusTen)
        self.btnPlusHundredIter.clicked.connect(self.handlerBtnPlusHundred)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Snowball Earth Theorem"))
        self.grpInitialParameters.setTitle(_translate("MainWindow", "Initial parameters"))
        self.lblAlbedoCloud.setText(_translate("MainWindow", "Albedo Constant:"))
        self.lblNbCell.setText(_translate("MainWindow", "Number of cells:"))
        self.lblGreenHouse.setText(_translate("MainWindow", "Green House Constant:"))
        self.btnStart.setText(_translate("MainWindow", "Start  simulation"))
        self.lblTempInit.setText(_translate("MainWindow", "Initial temperature:"))
        self.grpIterCtrl.setTitle(_translate("MainWindow", "Iteration control"))
        self.btnPlusOneIter.setText(_translate("MainWindow", "+ 1"))
        self.btnPlusFiveIter.setText(_translate("MainWindow", "+ 5"))
        self.btnPlusTenIter.setText(_translate("MainWindow", "+ 10"))
        self.btnPlusHundredIter.setText(_translate("MainWindow", "+ 100"))
        self.grpCurrentIter.setTitle(_translate("MainWindow", "Current iteration"))

    def startSimulation(self):
        nbCells = int(self.txtNbCell.toPlainText())
        albedoCloud = float(self.txtAlbedo.toPlainText())
        greenHouse = float(self.txtGreenHouse.toPlainText())
        fTempInit = float(self.txtTempInit.toPlainText())

        matSize = int(math.sqrt(nbCells))
        tempInit = np.zeros((matSize, matSize))
        tempInit.fill(fTempInit)

        self.grpInitialParameters.setEnabled(False)
        self.grpIterCtrl.setEnabled(True)
        self.grpCurrentIter.setEnabled(True)

        # Creating the Earth object
        self.earth = Earth(nbCells, albedoCloud, greenHouse, tempInit)

        self.matOverall = np.zeros(1)
        matAvgPerZone = self.earth.getAvgPerZone()
        self.matOverall[0] = self.computeOverallAvg(matAvgPerZone)

        self.graphCurrent.show()
        self.graphCurrent.update_figure(0, matAvgPerZone)
        self.graphOverall.show()
        self.graphOverall.update_figure(1, self.matOverall)

    def iterate(self):
        matAvgPerZone = np.zeros(1)

        while self.nbIter > 0:
            self.earth.iterate()
            self.nbIter -= 1

            matAvgPerZone = self.earth.getAvgPerZone()
            self.matOverall = np.append(self.matOverall, self.computeOverallAvg(matAvgPerZone))

        # Current iteration graph
        self.graphCurrent.update_figure(0, matAvgPerZone)

        # Overall graph
        self.graphOverall.update_figure(1, self.matOverall)

        graphWidth = self.centralwidget.width() - 20
        graphHeight = (int)((self.centralwidget.height() - (self.graphCurrent.x() + 200)) / 2)
        
        self.graphCurrent.setGeometry(QtCore.QRect(10, 200, (int)((graphWidth / 3) * 2) - 5, graphHeight))
        self.graphOverall.setGeometry(QtCore.QRect(10, 200 + self.graphCurrent.height() + 15, graphWidth, graphHeight))

        imgWidth = (int)(graphWidth / 3) - 5
        imgPosX = (int)(self.graphCurrent.x() + ((graphWidth / 3) * 2)) + 5
        self.currGraphImage.setGeometry(imgPosX, self.graphCurrent.y(), imgWidth, graphHeight)
        
        BuildTempsImage(self.earth.getMatTemp(), min(matAvgPerZone), max(matAvgPerZone))

        pixmap = QtGui.QPixmap('temperatureImage.png')
        transform = QtGui.QTransform().rotate(90)
        pixmap = pixmap.transformed(transform)
        self.currGraphImage.setPixmap(pixmap)

    def handlerBtnPlusOne(self):
        self.nbIter = 1
        self.iterate()

    def handlerBtnPlusFive(self):
        self.nbIter = 5
        self.iterate()

    def handlerBtnPlusTen(self):
        self.nbIter = 10
        self.iterate()

    def handlerBtnPlusHundred(self):
        self.nbIter = 100
        self.iterate()

    def computeOverallAvg(self, mat):
        arrayWidth = mat.shape[0]
        lineAvgTemp = 0
        for i in range(arrayWidth):
            lineAvgTemp += mat[i]
        
        return lineAvgTemp / arrayWidth


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

class DynamicMplCanvas(MplCanvas):
    def __init__(self, *args, **kwargs):
        MplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        self.axes.plot()

    def update_figure(self, id, mat):
        arrayWidth = mat.shape[0]

        self.axes.cla()
        self.axes.set_xlabel('Zone')
        self.axes.set_ylabel('Temperature (k)')

        if id == 0:
             self.axes.set_title('Current temperature in Kelvin depending on the zone')
        else:
             self.axes.set_title('Overall temperature in Kelvin depending on the zone')
       
        if (arrayWidth < 150):
            self.axes.plot(np.arange(arrayWidth), mat, 'or-')
        else:
            self.axes.plot(np.arange(arrayWidth), mat, 'r-')

        if arrayWidth <= 11:
            self.axes.xaxis.set_ticks(np.arange(0, arrayWidth, 1))
        elif arrayWidth < 31:
            self.axes.xaxis.set_ticks(np.arange(0, arrayWidth, 2))
        elif arrayWidth < 61:
            self.axes.xaxis.set_ticks(np.arange(0, arrayWidth, 4))
        elif arrayWidth < 101:
            self.axes.xaxis.set_ticks(np.arange(0, arrayWidth, 6))

        start, end = self.axes.get_ylim()
        step = (int)((end - start) / 10)

        if step < 5:
            self.axes.yaxis.set_ticks(np.arange(start, end, 5))
        elif step < 10:
            self.axes.yaxis.set_ticks(np.arange(start, end, 10))
        elif step < 15:
            self.axes.yaxis.set_ticks(np.arange(start, end, 15))

        self.draw()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
