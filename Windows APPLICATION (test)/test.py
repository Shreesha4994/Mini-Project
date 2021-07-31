from car_ui import*
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
def set_helo():
	#global ui
	ui.label_2.setText("helo")
set_helo()
sys.exit(app.exec_())