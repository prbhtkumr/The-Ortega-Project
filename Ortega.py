
#Author : Prabhat
#Description : This is an interactive research assistant, for computational purposes;
#Note : Although, Knowledge/Information gathering can be done using the tool, you're not suggested to totally relay on the tool (*sigh* or, you'll face some bugs and glitches) '''

import os
import time
import pyttsx3
import colorama
import wolframalpha
import speech_recognition as sr
import random
import sys
import wikipedia
from colorama import Fore,Back,Style
import base64
os.system("cls")
#初期化
r = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')                           
engine.setProperty('rate', 150)
engine = pyttsx3.init()

os.system("cls")
print(Style.RESET_ALL)

#定義
engine.say("What do you want the input method to be?")
print("\n\n\nWhat do you want the input method to be?\n\n   [1] Type\n   [2] Speech")
engine.runAndWait()
mode = input()


os.system("cls")
print(Fore.GREEN+Style.BRIGHT)
print( '\t'*7+'                     .                          ')
print( '\t'*7+'     Legalize        M                          ')
print( '\t'*7+'          Cannabis  dM                          ')
print( '\t'*7+'                    MMr                         ')
print( '\t'*7+'                   4MMML                  .     ')
print( '\t'*7+'                   MMMMM.                xf     ')
print( '\t'*7+'   .              "MMMMM               .MM-     ')
print( '\t'*7+'    Mh..          +MMMMMM            .MMMM      ')
print( '\t'*7+'    .MMM.         .MMMMML.          MMMMMh      ')
print( '\t'*7+'     )MMMh.        MMMMMM         MMMMMMM       ')
print( '\t'*7+'      3MMMMx.     \'MMMMMMf      xnMMMMMM"       ')
print( '\t'*7+'      \'*MMMMM      MMMMMM.     nMMMMMMP"        ')
print( '\t'*7+'        *MMMMMx    "MMMMM\\    .MMMMMMM=        ') 
print( '\t'*7+'         *MMMMMh   "MMMMM"   JMMMMMMP           ')
print( '\t'*7+'           MMMMMM   3MMMM.  dMMMMMM            .')
print( '\t'*7+'            MMMMMM  "MMMM  .MMMMM(        .nnMP"')
print( '\t'*7+'=..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*  ')
print( '\t'*7+'  "MMn...     \'MMMMr \'MM   MMM"   .nMMMMMMM*"   ')
print( '\t'*7+'   "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""     ')
print( '\t'*7+'     ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"        ')
print( '\t'*7+'        *PMMMMMMhn. *x > M  .MMMM**""           ')
print( '\t'*7+'           ""**MMMMhx/.h/ .=*"                  ')
print( '\t'*7+'                    .3P"%....                   ')
print( '\t'*7+'                  nP"     "*MMnx         Prabhat')
time.sleep(3)
print(Style.RESET_ALL)

#あいさつ

def exit():
	os.system('cls')
	engine.say("Alright .. Exiting!")
	engine.runAndWait()

def say(var):
	engine.say(var)
	engine.runAndWait()

def name():
	say("My name is Ortega, atleast that's what \"he\" (my creator) calls me!")
	print("My name is Ortega")
	print("Atleast that's what \"He\" (My Creator) calls me.")
	print("\n\t\t\t\t\t :)")
	time.sleep(2)

def creator():
	say("Prabhat is my creator.")
	print("Prabhat is my creator.")
	rate = engine.getProperty('rate')                           
	engine.setProperty('rate', 205)     
	say("Waahi haai saarva shaakti shaaali bhaagwaaan, aasvaatthhaaamaa.")
	print("Wahi hai saarva shakti-shaali bhagwaan, Asvathama!")
	time.sleep(2)
	say("He also is my doctor, whenever I get a bug, he solves it with ease. caring he is.! ")

def god():
	say("Praabhaaat. Wahi haai saarva shaakti shaaali bhaagwaaan, aasvaatthhaaamaa!")
	print("Prabhat")
	print("Wahi hai saarva shakti-shaali bhagwaan, Asvathama!")

def wait():
	os.system("cls")
	say("Alright .. Waiting ... Press any key to End.")
	print("\n\n\nAlright \n..Waiting \n...Press any key to End")
	for i in range(10):
		for cursor in '\\|/-':
			time.sleep(0.1)
			sys.stdout.write('\r{}'.format(cursor))
			sys.stdout.flush()
	os.system("cls")
	input("\n\n\nAlright \n..Waiting \n...Press any key to End")
def wiki():
	engine.say("let me ask Wichishiki")
	print("Let me ask Wichishiki :)")
	engine.runAndWait()
	engine.say("What do you want to know about?")
	print("\n\n\n\n\t\t\t\tWhat do you want to know about?\n\n")
	engine.runAndWait()
	request = input("\n\t\t\t\t>?=")
	response = wikipedia.summary(request)
	engine.say(response)
	print(response)
	engine.runAndWait() 
	input()
def lyrics():
	print("Prabhat")
	print("----------------------------------")
	inp=input("enter name of artist and name of song separated by / :   ").lower().replace(" ", '')or"edsheeran/eraser";inp=inp.split('/') if '/' in inp and inp.count('/') == 1 else 'you need to seperate the artist name from his/her title using /' if not '/' in inp or inp.count('/') > 1 else 'Invalid input....\nplease check the top comment of this code';artist,title = inp[0],inp[1]
	print('Artist: {}\nTitle: {}\n{}'.format(artist.title(),title.title(),'-'*25))
	import re
	from urllib.request import urlopen; from html.parser import HTMLParser
	link = urlopen("https://www.azlyrics.com/lyrics/{}/{}.html".format(artist,title)).read()
	link = str(link)
	class MyHTMLParser(HTMLParser):
	    def __init__(self):
	        super().__init__()
	        self.p=False
	        self.pbuf=[]
	    def handle_starttag(self, tag, attrs):
	        attrs = dict(attrs)
	        if tag=="div" and not attrs:
	            self.p=True
	            self.pbuf=[]
	    def handle_endtag(self, tag):
	        if tag=="div" and self.p:
	            self.p=False
	            print("\n".join(self.pbuf),flush=1)
	            self.pbuf =[]
	    def handle_data(self, data):
	        if(self.p):
	            data=data.replace("\\n","\n")
	            data=data.replace("\\","")
	            data = re.sub(r'\br\b', '', data)
	            self.pbuf.append(data.strip())
	parser = MyHTMLParser()
	parser.feed(link)
	print('\n\nPrabhat')
def cmd():
	os.system('start')


#知識源
while True:
	os.system("cls")
	engine.say("What's you Query?")
	print("\n\n\n\nWhat's your Query?: ")
	engine.runAndWait()


	#Setting the Input Method
	if int(mode)==1:
		inpt = input("")

	elif int(mode)==2:
		with sr.Microphone() as source:
					inpt = r.listen(source)
					try:
						inpt = r.recognize_google(inpt)
					except:
						engine.say("Sorry could not recognize your voice, try again")
						engine.runAndWait()
						print("Sorry could not recognize your voice :/")
						print("Try again")
						engine.runAndWait()
						with sr.Microphone() as source:
							inpt = r.listen(source)
							try:
								inpt = r.recognize_google(inpt)
							except:
								engine.say("Sorry could not recognize your voice, ... Exiting")
								engine.runAndWait()
								print("Sorry could not recognize your voice:/")
								print("Exiting")
		
	#Computation
	if inpt=="quit":
		exit()
		break
	elif inpt=="exit":
		exit()
		break
	elif inpt=="leave me alone":
		exit()
		break
	elif inpt=="just shut the fuck up":
		exit()
		break
	elif inpt=="shut up":
		wait()
		break
	elif inpt=="close":
		exit()
		break
	elif inpt=="how do i quit":
		exit()
		break
	elif inpt=="what is your name":
		name()
		continue
	elif inpt=="what's your name":
		name()
		continue
	elif inpt=="your name":
		name()
		continue
	elif inpt=="who are you":
		name()
		continue
	elif inpt=="who made you":
		creator()
		continue
	elif inpt=="change mode":
		mode()
		continue
	elif inpt=="who created you":
		creator()
		continue
	elif inpt=="start speaking":
		mode()
		continue
	elif inpt=="change input method":
		mode()
		continue
	elif inpt=="change input mode":
		mode()
		continue	
	elif inpt=="who's your creator":
		creator()
		continue
	elif inpt=="who is your creator":
		creator()
		continue
	elif inpt=="who is you god":
		god()
		continue
	elif inpt=="who's your god":
		god()
		continue
	elif inpt=="bhagwaan mein maante ho":
		god()
		continue
	elif inpt=="wait":
		wait()
		continue
	elif inpt=="just wait for some time":
		wait()
		continue
	elif inpt=="will you wait":
		wait()
		continue
	elif inpt=="hold on":
		wait()
		continue
	elif inpt=="hang on":
		wait()
		continue
	elif inpt=="halt":
		wait()
		continue
	elif inpt=="stay":
		wait()
		continue
	elif inpt=="pause":
		wait()
		continue
	elif inpt=="let me see":
		wait()
		continue
	elif inpt=="bare with me":
		wait()
		continue
	elif "wiki" in inpt:
		wiki()
		continue
	elif inpt=="open wikipedia":
		wiki()
		continue
	elif inpt=="wikipedia":
		wiki()
		continue
	elif inpt=="search wikipedia":
		wiki()
		continue
	elif "search wikipedia for" in inpt:
		wiki(inpt.replace("search wikipedia for",""))
		continue
	elif inpt=="launch wikipedia":
		wiki()
		continue
	elif inpt=="wichishiki":
		wiki()
		continue
	elif inpt=="launch wichishiki":
		wiki()
		continue
	elif "search wichishiki" in inpt:
		wiki()
		continue
	elif "search wichishiki for" in inpt:
		wiki(inpt.replace("search wichishiki for",""))
		continue
	elif inpt=="launch command prompt":
		cmd()
		input("")
		continue
	elif inpt=="launch terminal":
		cmd()
		input("")
		continue
	elif inpt=="launch shell":
		cmd()
		input("")
		continue
	elif inpt=="open terminal":
		cmd()
		input("")
		continue
	elif inpt=="open command prompt":
		cmd()
		input("")
		continue
	elif inpt=="open shell":
		cmd()
		input("")
		continue
	elif "lyrics" in inpt:
		lyrics()
		input("")
		continue
	elif inpt=="":
		engine.say("Didn't recieve any input, try again")
		print("Didn't recieve any input,\t:\\\n\t\tTry Again")
		engine.runAndWait()
		continue


	#Sending the Request to Computational Service
	app_id = "R5K5G6-QWQ5RT2VLA"
	client = wolframalpha.Client(app_id)

	rate = engine.getProperty('rate')                           
	engine.setProperty('rate', 160)     

	res = client.query(inpt)
	try:

		try:
			answer = next(res.results).text
			
			print("You said: \n\t"+inpt+"\n\n")
			
		
		except:
			print("")

		engine.say(answer)
		print(answer)
		engine.runAndWait()
	except:
		engine.say("I'm afraid an Error occured.")
		print("I'm afraid, an Error occured.\t\t:/")
		engine.runAndWait()

	time.sleep(2)
