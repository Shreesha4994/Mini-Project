from car_ui import*
import sys
import speech_recognition as sr
from features_nlp import*
r = sr.Recognizer()
import time

def start_processing():
	global ui
	#ui.pushButton.setText("Speak Now")
	time.sleep(0.2)
	with sr.Microphone() as source:
		#ui.pushButton.setText("Speak Now")
		audio = r.listen(source,phrase_time_limit=4)
	try:
		voice_text = r.recognize_google(audio)
		ui.label_2.setText(str(voice_text))
		print(voice_text)
		get_features(voice_text)
		predicted_code = clf_from_joblib.predict([features])
		print(predicted_code)
		time.sleep(1)
		ui.pushButton.setText("Press \n to \n Speak")
	except sr.UnknownValueError:
		ui.label_2.setText("Couldn't Process")
		print("Couldn't Process")
		pass
	


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

ui.pushButton.clicked.connect(lambda:start_processing())

sys.exit(app.exec_())
