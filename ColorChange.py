import serial, webbrowser

# html code to be written to file
Code = "<!DOCTYPE html><html><head><title>Potentiometer color changer</title></head><body><h1><font color='%s'>Color</font></h1></body></html>"

#counter to limit number of changes
count = 0

while count<10:
	#Something has to be connected to port.
	with serial.Serial('COM12', 9600) as data:
		# color comes in as a str, convert to int, convert to hex
		color = hex(int(data.readline()))
		newCode = Code %color
		
	with open('ColorChange.html','w+') as HTMLfile:
		#got to beginning of file (go zero from zero)
		HTMLfile.seek(0,0)
		#erase contents/write newCode
		HTMLfile.write(newCode)

	#open new html file in browser
	webbrowser.open('C:\Users\Richard\Desktop\ColorChange\ColorChange.html',2,True)
	count+=1 #increment counter