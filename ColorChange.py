import serial, webbrowser
Code = "<!DOCTYPE html><html><head><title>Potentiometer color changer</title></head><body><h1><font color='%s'>Color</font></h1></body></html>"
count = 0
#Something has to be connected to port.
while count<10:
	with serial.Serial('COM12', 9600) as data:
		color = int(data.readline())
		print color
		newCode = Code %hex(color)
		
	with open('ColorChange.html','w+') as HTMLfile:
		HTMLfile.seek(0,0)
		HTMLfile.write(newCode)
	webbrowser.open('C:\Users\Richard\Desktop\ColorChange\ColorChange.html',2,True)
	count+=1