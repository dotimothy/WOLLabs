#Wake On LAN Python CLI Client

import csv
from wakeonlan import send_magic_packet
import socket
import urllib.request

def csvToDict(deviceCSVName,site):
	deviceCSV = open('Devices.csv',newline='')
	reader = csv.DictReader(deviceCSV)
	counter = 0
	data = {}
	for row in reader:
		if(row['Site'] == site and row['WOL'] == 'Yes'):
			counter = counter + 1
			data[counter] = {}
			data[counter]["Name"] = row["Name"]
			data[counter]["MacAddress"] = row["MacAddress"]
	deviceCSV.close()
	return data

def wakeComputer(mac): 
	for i in range(25):
		send_magic_packet(mac)

def updateSiteIP(siteCSVName): 
	siteCSV = open('Sites.csv','r',newline='',)
	reader = csv.DictReader(siteCSV)
	data = {}
	for row in reader: 
		data[row['Site']] = {}
		if(row['Domain'] != ''):
			data[row['Site']]['Domain'] = row['Domain']
			data[row['Site']]['LastKnownIP'] = socket.gethostbyname(row['Domain'])
		else: 
			data[row['Site']]['Domain'] = ''
			data[row['Site']]['LastKnownIP'] = ''
	siteCSV.close() 
	siteCSV = open('Sites.csv','w',newline='',)
	writer = csv.writer(siteCSV)
	writer.writerow(['Site','Domain','LastKnownIP'])
	for site,info in data.items():
		writer.writerow([site,info['Domain'],info['LastKnownIP']])
	siteCSV.close()

def getSite(siteCSVName):
	siteCSV = open('Sites.csv','r',newline='',)
	reader = csv.DictReader(siteCSV)
	hostIP = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
	for row in reader: 
		if(row['LastKnownIP'] == hostIP):
			return row['Site']

def promptUser(data,site='SJ'):
	done = False
	prompt = 0
	while(not(done)):
		print(f"WOLLabs - Choose a Computer to Wake on LAN ({site} Site):")
		for num,entry in data.items():
			print(f'({num}): {entry["Name"]}')
		print('(0): Exit')
		try:
			prompt = int(input("Choice: "))
			if(prompt == 0):
				done = True
				print('Goodbye.')
			elif(prompt <= len(data)):
				print(f'Turning On {data[prompt]["Name"]} via WOL (MAC: {data[prompt]["MacAddress"]})')
				wakeComputer(data[prompt]["MacAddress"])
			else:
				print("Invalid Input (Out of Range). Try Again")
		except Exception as e: 
			print("Invalid Input (Not a Number). Try Again")
		print()

if __name__ == "__main__":
	updateSiteIP('Sites.csv')
	site = getSite('Sites.csv')
	if site is not None:
		promptUser(csvToDict('Devices.csv',site),site)
	else:
		print(f'You are Not at a Valid Site to WOL. (IP: {socket.gethostbyname(socket.gethostname())})')
