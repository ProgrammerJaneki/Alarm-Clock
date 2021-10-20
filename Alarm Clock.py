#Alarm Clock with Python using datetime and playsound library

from datetime import datetime
from playsound import playsound

#-The program will ask for time of the alarm in a format of 
#-Hour:Minute:Seconds:Period
#-Input will be read as a string not a integer. 
#-In order to get the values, we need to use string slicing 
#-for the for alarm_ variables

alarm_time = input("Enter the time of alarm to be set: HH:MM:SS:PM/AM\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")

#-strftime() is a function used to convert date and time objects 
#-to their string representation
#-To set up the current time, we declared the "now = datetime.now()"
#-We are getting the current time by using the strftime() function
#-and storing the values on the current_ variables
#-If the current time is equal to the alarm set, the playsound
#-function will play the ringtone set and break off the loop


while True:
	now = datetime.now()
	current_hour = now.strftime("%I")
	curret_minute = now.strftime("%M")
	current_seconds = now.strftime("%S")
	current_period = now.strftime("%p")
	if alarm_period == current_period:
		if alarm_hour == current_hour:
			if alarm_minute == curret_minute:
				if alarm_seconds == current_seconds:
					print("Wake up!!")
					playsound('my_alarm.wav')
					break 


