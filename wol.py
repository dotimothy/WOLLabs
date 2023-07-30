import csv
from wakeonlan import send_magic_packet

def csvToDict(csvFile,site):
	reader = csv.DictReader(csvFile)
	counter = 0
	data = {}
	for row in reader:
		if(row['Site'] == site):
			counter = counter + 1
			data[counter] = {}
			data[counter]["Name"] = row["Name"]
			data[counter]["MacAddress"] = row["MacAddress"]
	return data


def promptUser(data):
	done = False
	prompt = 0
	while(not(done)):
		print("Choose a Computer to Wake on LAN (WOL):")
		for num,entry in data.items():
			print(f'({num}): {entry["Name"]}')
		print('(0): Exit')
		try:
			prompt = int(input("Choice: "))
			if(prompt == 0):
				done = True
				print('Goodbye.')
			else:
				print(f'Turning On {entry["Name"]} via WOL (MAC: {entry["MacAddress"]})')
				send_magic_packet(entry["MacAddress"])
		except Exception as e: 
			print("Invalid Input. Try Again")
		print()

if __name__ == "__main__":
	csvFile = open('Devices.csv',newline='')
	promptUser(csvToDict(csvFile,'SJ'))