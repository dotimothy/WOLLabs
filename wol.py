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
			elif(prompt <= len(data)):
				print(f'Turning On {data[prompt]["Name"]} via WOL (MAC: {data[prompt]["MacAddress"]})')
				send_magic_packet(data[prompt]["MacAddress"])
			else:
				print("Invalid Input (Out of Range). Try Again")
		except Exception as e: 
			print("Invalid Input (Not a Number). Try Again")
		print()

if __name__ == "__main__":
	csvFile = open('Devices.csv',newline='')
	promptUser(csvToDict(csvFile,'SJ'))