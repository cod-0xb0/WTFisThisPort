import pyfiglet
import os
import sys
from termcolor import colored, cprint


#Welcome 
scrtitle = pyfiglet.figlet_format("WTFISTHISPORT")
print(scrtitle)
print('\n 1-Single Fucking Port Info')
print('\n 2-Multiple Fucking Ports Info')

#error message
unknownport = "\n The fucking port is not existed in our fucking database, you can fucking contribute and help to add it or close the fucking script"
wronginput = "\n Input is not correct"

#USer Options
UserChooice = input('\n Choose one of the fucking options: ')

#a fucking function to Get the Fucking info for a fucking single port
def SinglePort (portno): 
    #read the fucking default txt file containts fucking common ports and description
    with open(r"db.txt", 'r') as fp:
        #print fucking title
        print(scrtitle)
        #fucking for loop to search the fucking port in the fucking txt file
        for l_no, line in enumerate(fp):
            #if fucking port found then print the fucking info and exit
            if portno in line:
                print (colored('Port Information: ', 'green'), colored(line, 'green'))
                break

#a fucking function to Get the Fucking info for a fucking multiple port
def MultiplePorts (portslist): 
    #print the fucking title
    print(scrtitle)
    #Fucking splitter by comma to seperate the fucking ports
    fucking_list = portslist.split(',')
    #looping the fucking list
    for i in range(len(fucking_list)):
    # convert each fucking item to fucking int type
        fucking_list[i] = int(fucking_list[i])
        #convert fucking ports to string
        fuckingports=(str(fucking_list[i]))
        #read the fucking default txt file containts fucking common ports and description
        with open(r"db.txt", 'r') as fp:
        #fucking for loop to search the fucking ports in the fucking txt file
            for l_no, line in enumerate(fp):
                 #if fucking port found then print the fucking info
                if fuckingports in line:
                    print (colored('Port Information: ', 'green'), colored(line, 'green'))
                    

#Fucking user inputs
if (UserChooice == "1"):
    portno = input ("\n Enter the port No.: ")
    SinglePort(portno)
elif(UserChooice == "2"):
    portslist = input('\n Enter ports seperated by comma ex: 21,22,52: ')
    MultiplePorts(portslist)
else:
    print (colored(wronginput,'red'))






