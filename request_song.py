#!/usr/bin/env/Python3
import schedule
import webbrowser
import os
import time

def play_song():
	#Cutting last song requested
	os.system('cat /home/ubuntu/WakeUpPi/web-side/links.db | tail -n 1 > /home/ubuntu/WakeUpPi/backend-request-song/TBP.txt')
	#Process the song
	os.system('cut -c 10- /home/ubuntu/WakeUpPi/backend-request-song/TBP.txt | cut -f1 -d\'"\' > /home/ubuntu/WakeUpPi/backend-request-song/song.txt')
	with open ('/home/ubuntu/WakeUpPi/backend-request-song/song.txt', 'rt') as myfile:  # Open lorem.txt for reading text
		url = myfile.read()              # Read the entire file into a string
	controller = webbrowser.get()
	controller.open(url,new=1)

schedule.every().day.at("06:00").do(play_song)
#schedule.every().minute.at(":05").do(play_song)

while True:
    schedule.run_pending()
    time.sleep(1)
