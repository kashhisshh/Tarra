from difflib import get_close_matches
import json
from random import choice
import datetime
from googletrans import Translator, LANGUAGES

class DateTime:
	def currentTime(self):
		time = datetime.datetime.now()
		x = " A.M."
		if time.hour>12: x = " P.M."
		time = str(time)
		time = time[11:16] + x
		return time

	def currentDate(self):
		now = datetime.datetime.now()
		day = now.strftime('%A')
		date = str(now)[8:10]
		month = now.strftime('%B')
		year = str(now.year)
		result = f'{day}, {date} {month}, {year}'
		return result
	
def wishMe():
	now = datetime.datetime.now()
	hr = now.hour
	if hr<12:
		wish="Good Morning"
	elif hr>=12 and hr<16:
		wish="Good Afternoon"
	else:
		wish="Good Evening"
	return wish


def isContain(text, lst):
	for word in lst:
		if word in text:
			return True
	return False

def chat(text):
	dt = DateTime()
	result = ""
	if isContain(text, ['good']):
		result = wishMe()		
	elif isContain(text, ['time']):
		result = "Current Time is: " + dt.currentTime()
	elif isContain(text, ['date','today','day','month']):
		result = dt.currentDate()

	return result

data = json.load(open('extrafiles/NormalChat.json', encoding='utf-8'))

def reply(text):
	if text in data:
		response =  data[text]
		return choice(response)
	else:
		return "None"

def lang_translate(text,language):
	if language in LANGUAGES.values():
		translator = Translator()
		print(language)
		result = translator.translate(text, src='en', dest=language)
		return result
	else:
		return "None"

