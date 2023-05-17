# PeopleDetectionWithVideoSurveillance
This program is used to activate a people recognition alarm system.
Send a message via telegram if it has found a person and a siren sounds, again from telegram it is possible to run/stop the program and activate/deactivate the people recognition system and the alarm


REQUIREMENTS:

  It is requirest create a bot python and insert in the file configurazione.txt the keys
  and the URL for connects at the videocapture in the browser(always on file configurazione.txt)
  Create an virtual enviroment
  install and check if the chromedriver version is the same version of google chrome


TO RUN:
  run tele.py,if this not work,before to run tele.py, run the virtual enviroment and then run tele.py on this virtual enviroment
  from telegram it is possibile to manage the video camera.
  The messages are:
  "help" -> the bot return the actual situation of the alarm
  "start" -> the bot run the program
  "stop" -> the bot stop the program
  "on" -> the bot active the alarm
  "off" -> the bot deactive the alarm
  "ok" -> the bot block the sirena


TO INSTALL:

   Command(to run):
   	  sudo apt-get install ffmpeg

   Files(to import):
	  yolov3.cfg
	  yolov3.weights
	  coco.names
	  chromedriver(must be present in this directory)
   Libraries(to install):
  	  telebot
  	  selenium
  	  cv2
  	  PIL
  	  numpy
  	  pydub
  	  


  
