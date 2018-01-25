import speech_recognition
import pyttsx
from os import system
system('say Hello world!')



recognizer = speech_recognition.Recognizer()
keyphrase = "none"
response = "Good afternoon sir"

def weather():
	print("blah")

def speak(text):
	system('say ' + text)
keywords = ["hi", "bye", "weather"]
def hi():
	global response
	response = "hello sir"

def bye():
	global response
	response = "goodbye sir"
	global keyphrase
	keyphrase = "stop"

def keyword(text) :
	for phrase in keywords:
		if phrase in text:
			globals()[phrase]()


def listen():
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	try:
		message = recognizer.recognize_google(audio)
		global keyphrase
		keyphrase = message
		#print(keyphrase)
		keyword(keyphrase)
		return message
	except speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))

	return ""
while (keyphrase != "stop"):
	speak(response)
	listen()
	print(keyphrase)

	#speak("I heard you say " + listen())
