from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
dlg = uic.loadUI('C:\\Users\\Alex\\Game_And_Tech\\QuestCalculatorClass\\QCGUI\\mainwindow.ui')

dlg.show()
app.exec()
