import sys
from PyQt5 import QtWidgets
from qt测试.untitled import Ui_MainWindow

class MyPyQT_Form(QtWidgets.QWidget,Ui_MainWindow):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())