# Wake On LAN Server Implemented in Python Flask

# Libraries 
from flask import Flask, redirect, url_for, render_template, request, send_file
import os 
import wol
from wakeonlan import send_magic_packet


# Creating the app 
app = Flask(__name__)
deviceFile = open('Devices.csv',newline='')
site = wol.getSite('Sites.csv')
devices = wol.csvToDict(deviceFile,site)
deviceFile.close()

def updateDevice(): 
	global deviceFile
	global devices
	global site
	deviceFile = open('Devices.csv',newline='')
	devices = wol.csvToDict(deviceFile,site)
	deviceFile.close()

# Landing Page
@app.route("/")
def home():
	updateDevice()
	html = '<html>\n\t<head>\n\t\t<title>TheDoLab WOL Server</title>\n\t</head>\n\n'
	html += '\t<style>\n\t\t* { \n\t\t\tfont-family: Courier;\n\t\t\tbackground-color: black;\n\t\t}\n\t\th1,h2,label,input, button { \n\t\t\tcolor: white;\n\t\t}\n\t\th2,label,input, button { \n\t\t\tfont-size:1.5em;\n\t\t}\n\t</style>\n\n'
	html += '\t<script>\n\n\t\tvar checked = False;\n\t\tfunction checkAll() {\n\t\t\tchecked = !checked;\n\t\t\tvar checkboxes = document.getElementsByName("Number");\n\t\t\tfor(var i = 0; i < checkboxes.length; i++) {\n\t\t\t\tcheckboxes[i].checked = checked;\n\t\t\t}\n\t\t}\n\n\t</script>\n\n'
	html += '\t<body>\n\n'
	html += '\t\t<h1>TheDoLab\'s Wake On Lan Web Server</h1>\n\t\t<h2>Choose Devices to WOL:</h2>\n\n'
	html += '\t\t<button onClick="checkAll()">Check All</button><br><br>\n'
	html += '\t\t<form action="/upload" method="post" enctype="multipart-form-data">\n\t\t\n'
	for key in devices.keys():
		html += f'\t\t\t<input type="checkbox" id=\"{key}\" name="Number" value=\"{key}\">\n'
		html += f'\t\t\t<label for=\"{key}\">{key}. {devices[key]["Name"]} ({devices[key]["MacAddress"]})</label><br>\n\n'
	html += '\t\t\t<br><input type="submit" value="Submit"/><br>'

	html += '\n\t</body>\n'
	html += '\n\n</html>'
	return html

@app.route("/upload",methods=["POST","GET"])
def upload():
	if request.method == "POST": 
		wols = [int(wol) for wol in request.form.getlist('Number')]
		if(len(wols) != 0):
			html = '<script>\n\t'
			wolStr = 'Woke Up the Following Computers:\\n\\n'
			for wolPC in wols: 
				wolStr += f'{wolPC}. {devices[wolPC]["Name"]} ({devices[wolPC]["MacAddress"]})\\n'
				wol.wakeComputer(devices[wolPC]['MacAddress'])
			html += f'alert(\"{wolStr}\");\n\twindow.location.replace("");\n\t</script>';
		else: 
			html = '<script>\n\talert("Nothing Selected. Try Again.");\n\twindow.location.replace("");\n</script>'
		return html
	else:
		return redirect(url_for('home'))

		
# Debug if the same file as run
if __name__ == "__main__":
	port = int(input('Choose a Port to Host the WOL Server: '))
	app.run(debug=False,host='0.0.0.0',port=port)
