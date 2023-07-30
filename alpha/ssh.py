#!/usr/bin/env python
import os

def main():
	ssh = "\0"
	host = "\0"
	user = "\0"
	print("Please Select A Computer to SSH Into:")
	print("(1): SERVER-TD2020")
	print("(2): DESKTOP-HP2020")
	print("(3): DESKTOP-TD2015")
	print("(4): LAPTOP-TDMSI")
	print("(5): WORKSTATION-TD2020")
	print("(6): TDoPi4")
	print("(7): TDoZeroW")
	print("(8): TDole")
	print("(9): TDoPi3")
	print("(0): Exit")
	try:
		ssh = int(input("Choice: "))
	except ValueError:
		ssh = 99
	if(ssh == 0):
		print("Goodbye.")
		exit = input("Thanks for Using ssh.py")
		exit()
	elif(ssh == 1):
	    print("SSH into SERVER-TD2020")
	    os.system("ssh SERVER-TD2020@SERVER1-TD2020.local")
	elif(ssh == 2):
	  	print("SSH into DESKTOP-HP2020")
	  	os.system("ssh HP-TD2020@DESKTOP-HP2020.local")
	elif(ssh == 3):
	    print("SSH into DESKTOP-TD2015")
	    os.system("ssh \"Timothy Do\"@DESKTOP-TD2015.local")
	elif(ssh == 4):
		print("SSH into LAPTOP-TDMSI")
		os.system("ssh MSI_TD1@LAPTOP-TDMSI.local")
	elif(ssh == 5):
		print("SSH into WORKSTATION-TD2020")
		os.system("ssh \"Timothy Do\"@WORKSTATION-TD2020.local")
	elif(ssh == 6):
		mode = int(input("Internal (0) or External (1): "))
		if(mode == 0):
			print("SSH into TDoPi4 (Internal)")
			os.system("ssh Tim@TDoPi4.local -X")
		else:
			print("SSH into TDoPi4 (External)")
			os.system("ssh Tim@thedolab.ddns.net -p 32766 -X")
	elif(ssh == 7):
                mode = int(input("Internal (0) or External (1): "))
                if(mode == 0):
                        print("SSH into TDZeroW (Internal)")
                        os.system("ssh Tim@TDZeroW.local -X")
                else:
                        print("SSH into TDZeroW (External)")
                        os.system("ssh Tim@thedolab.ddns.net -p 32765 -X")
	elif(ssh == 8):
		print("SSH into TDole")
		os.system("ssh pi@TDole.local -X")
	elif(ssh == 9):
	    mode = int(input("Internal (0) or External (1): "))
	    if(mode == 0):
	            print("SSH into TDoPi3 (Internal)")
	            os.system("ssh Tim@TDoPi3.local -X")
	    else:
	            print("SSH into TDoPi3 (External)")
	            os.system("ssh Tim@thedolab.ddns.net -p 32767 -X")
	elif(ssh == 10):
		print("Other SSH")
		host = str(input("Please Input Host: "))
		user = str(input("Please Input User: "))
		os.system("ssh -X " + user + "@" + host)
	else:
	    print("Try Again")
	    main()

while(1):
	try:
		main()
	except KeyboardInterrupt:
		print("Try Again!")

