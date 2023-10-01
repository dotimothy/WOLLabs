#!/usr/bin/env python3
import os
import getpass
import random
import time
import urllib.request
import socket

#wolp: Wake On Lan Console for Raspberry Pi
#Author: Timothy Do

exited = 0
def main():
        global exited
        #Getting External IP-Address
        external = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
        #DDNS of TheDoLab and Picoma
        try:
                sj = socket.gethostbyname('thedolab.ddns.net')
        except socket.gaierror:
                print("TheDoLab is Down")
        try:
                oc = socket.gethostbyname('picoma.ddns.net')
        except socket.gaierror:
                print("picoma is Down")
        #Home
        while(exited == 0):
                if(external == sj):
                        sanJose('thedolab.ddns.net')
                elif(external == oc):
                        orange('picoma.ddns.net')
                else:
                        guestDeny()
                        exited = 1

# For San Jose Computers
def sanJose(external):
        global exited
        username = getpass.getuser()
        if(username == "guest"):
                if(guestTest()):
                        guestSJ()
                else:
                        guestDeny()
        #Interface for Regular Users
        print("Please Select A Computer to Wake on Lan (" + external + "):")
        print("(1): SERVER-TD2020")
        print("(2): DESKTOP-HP2020")
        print("(3): DESKTOP-TD2015")
        print("(4): LAPTOP-TDMSI")
        print("(5): WORKSTATION-TD2020")
        print("(6): DESKTOP-SC2021")
        print("(7): WORKSTATION-TD2023")
        print("(8): TimMini")
        print("(9): All")
        print("(10) Switch to Picoma")
        print("(0): Exit")
        try:
                wol = int(input("Choice: "))
        except KeyboardInterrupt:
                sanJose(external)
        except Exception as e:
                exit()
        if(wol == 0):
                print("Goodbye.")
                exited = 1
        elif(wol == 1):
                print("Turning on SERVER-TD2020 via WOL")
                os.system("sudo etherwake -i eth0 18:03:73:BD:F7:BC")
        elif(wol == 2):
                print("Turning on DESKTOP-HP2020 via WOL")
                os.system("sudo etherwake -i eth0 2C:27:D7:1D:00:C5")
        elif(wol == 3):
                print("Turning on DESKTOP-TD2015 via WOL")
                os.system("sudo etherwake -i eth0 D8:CB:8A:3C:3A:FF")
        elif(wol == 4):
                print("Turning on LAPTOP-MSI via WOL")
                os.system("sudo etherwake -i eth0 00:D8:61:85:A0:6B")
        elif(wol == 5):
                print("Turning on WORKSTATION-TD2020 via WOL")
                os.system("sudo etherwake -i eth0 2C:F0:5D:71:EF:47")
        elif(wol == 6):
                print("Turning on DESKTOP-SC2021 via WOL")
                os.system("sudo etherwake -i eth0 04:42:1A:0E:06:93")
        elif(wol == 7):
                print("Turning on WORKSTATION-TD2023 via WOL")
                os.system("sudo etherwake -i eth0 04:42:1A:0B:2D:8D")
        elif(wol == 8):
                print("Turning on TimMini via WOL")
                os.system("sudo etherwake -i eth0 14:98:77:6F:B1:88")
        elif(wol == 9):
                print("Turning on All Computers via WOL")
                os.system("sudo etherwake -i eth0 00:D8:61:85:A0:6B")
                os.system("sudo etherwake -i eth0 D8:CB:8A:3C:3A:FF")
                os.system("sudo etherwake -i eth0 2C:27:D7:1D:00:C5")
                os.system("sudo etherwake -i eth0 18:03:73:BD:F7:BC")
                os.system("sudo etherwake -i eth0 2C:F0:5D:71:EF:47")
                os.system("sudo etherwake -i eth0 04:42:1A:0E:06:93")
                os.system("sudo etherwake -i eth0 14:98:77:6F:B1:88")
        elif(wol == 10):
                print("Switch to picoma")
                os.system("ssh wol@dorm.thedocraft.me -p 32880")
                exited = 1
        else:
                print("Try Again")
                main()

#Orange Computers
def orange(external):
        global exited
        username = getpass.getuser()
        if(username == "guest"):
                if(guestTest()):
                        guestOC()
                else:
                        guestDeny()
        #Interface for Regular Users
        print("Please Select A Computer to Wake on Lan (" + external + "):")
        print("(1): DESKTOP-SC2021")
        print("(2): LAPTOP-MSI")
        print("(3): DESKTOP-SC2022")
        print("(4): All")
        print("(10): Switch to TheDoLab")
        print("(0): Exit")
        try:
                wol = int(input("Choice: "))
        except KeyboardInterrupt:
                orange(external)
        if(wol == 0):
                print("Goodbye.")
                exited = 1
        elif(wol == 1):
                print("Turning on DESKTOP-SC2021 via WOL")
                os.system("sudo etherwake -i eth0 04:42:1A:0E:06:93")
        elif(wol == 2):
                print("Turning on LAPTOP-MSI via WOL")
                os.system("sudo etherwake -i eth0 00:D8:61:85:A0:6B")
        elif(wol == 3):
                print("Turning on DESKTOP-SC2022 via WOL")
                os.system("sudo etherwake -i eth0 F0:2F:74:F3:5E:95")
        elif(wol == 4):
                print("Turning on All Computers via WOL")
                os.system("sudo etherwake -i eth0 00:D8:61:85:A0:6B")
                os.system("sudo etherwake -i eth0 04:42:1A:0E:06:93")
                os.system("sudo etherwake -i eth0 F0:2F:74:F3:5E:95")
        elif(wol == 10):
                print("Switching to TheDoLab")
                os.system("ssh wol@dorm.thedocraft.me -p 32766")
                exited = 1
        else:
                print("Try Again")
                main()

#guest for SJ
def guestSJ():
        print("Please Select A Computer to Wake on Lan (guest):")
        print("(1): DESKTOP-HP2020")
        print("(2): DESKTOP-TD2015")
        print("(0): Exit")
        wol = int(input("Choice: "))
        if(wol == 0):
                print("Goodbye.")
                exit()
        elif(wol == 1):
                print("Turning on DESKTOP-HP2020 via WOL")
                os.system("sudo etherwake -i eth0 2C:27:D7:1D:00:C5")
        elif(wol == 2):
                print("Turning on DESKTOP-TD2015 via WOL")
                os.system("sudo etherwake -i eth0 D8:CB:8A:3C:3A:FF")
        else:
                print("Try Again")
                main()
        if(wol == 1 or wol == 2):
                print("Be Sure to Turn on Parsec to Connect.")

#Guest Function for Orange
def guestOC():
        print("Please Select A Computer to Wake on Lan (guest):")
        print("(1): DESKTOP-SC2022")
        print("(0): Exit")
        wol = int(input("Choice: "))
        if(wol == 0):
                print("Goodbye.")
                exit()
        elif(wol == 1):
                print("Turning on DESKTOP-SC2022 via WOL")
                os.system("sudo etherwake -i eth0 F0:2F:74:F3:5E:95")
        else:
                print("Try Again")
                main()
        if(wol == 1):
                print("Be Sure to Turn on Parsec to Connect.")


#Math Test for Guest
def guestTest():
        opRand = random.randint(1,5)
        a = random.randint(1,100)
        b = random.randint(1,100)
        result = 0
        correct = 1
        #Addition Test
        if(opRand == 1):
                result = a + b
                answer = int(input("What Is " + str(a) + " + " + str(b) + "?\nEnter Response: "))
                if(answer != result):
                        correct = 0
        #Subtraction Test
        elif(opRand == 2):
                result = a - b
                answer = int(input("What Is " + str(a) + " - " + str(b) + "?\nEnter Response: "))
                if(answer != result):
                        correct = 0
        #Multiplication Test
        elif(opRand == 3):
                result = a * b
                answer = int(input("What Is " + str(a) + " * " + str(b) + "?\nEnter Response: "))
                if(answer != result):
                        correct = 0
        #Division Test
        elif(opRand == 4):
                while(a % b != 0 and b != 0):
                        a = random.randint(1,100)
                        b = random.randint(1,100)
                result = a / b
                answer = int(input("What Is " + str(a) + " / " + str(b) + "?\nEnter Response: "))
                if(answer != result):
                        correct = 0
        #Remainder Test
        elif(opRand == 5):
                while(a <= b and b != 0):
                        a = random.randint(1,100)
                        b = random.randint(1,100)
                result = a % b
                answer = int(input("What Is the Remainder of " + str(a) + " / " + str(b) + "?\nEnter Response: "))
                if(answer != result):
                        correct = 0
        #Prompt Correct or Incorrect
        if(correct == 1):
                print("Correct Answer!")
        else:
                print("Incorrect Answer. The Correct Answer Was " + str(result) + ".")
        return correct


def guestDeny():
        try:
                input("Guest WOL for TheDoLab is Not Avaliable: \n")
        except SyntaxError:
                exit()
        except NameError:
                exit()
        except KeyboardInterrupt:
                exit()
        exit()

main()
time.sleep(0.25)