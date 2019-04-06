from PyQt5 import QtCore, QtGui, QtWidgets
import img_gui
import qt_gui

class GUIForm(Ui_MainWindow):
    def __init__(self, parent=None):
        Ui_MainWindow.__init__(self, parent)
        self.threadData()

    def closeEvent(self, event):
        print "User has clicked the red x on the main window"
        event.accept()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = GUIForm(qt_gui.Ui_MainWindow)
    myapp.show()
    ret = app.exec_()
    sys.exit(ret)
