from texttable import Texttable
from os import system,remove
import ipaddress as ip

#Colors Here
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED   = '\033[91m'
print('\033[1m')#<--- For Make Font BOLD 


#Logo
def logo():
    system("clear")
    print('\033[91m'+'''
     +------------------------------------------------------+
     |	  _____  ___                                        |
     |	  \_   \/ _ \   /\/\   __ _ _ __  _ __   ___ _ __   |
     |	   / /\/ /_)/  /    \ / _` | '_ \| '_ \ / _ \ '__|  |
     |	/\/ /_/ ___/  / /\/\ \ (_| | |_) | |_) |  __/ |     |
     |	\____/\/      \/    \/\__,_| .__/| .__/ \___|_|     |
     |		                   |_|   |_|                |
     +------------------------------------------------------+
                			 Twitter: @YasserREED
    ''')

logo()


#Enter Your ip address
CLASS_C_ADDR = input('\033[96m'"[+] Enter IP Address (Ex: 192.168.20.0) : ")

#While Configration its True!
Configure_state = True
while Configure_state:
	
	#Enter Prefix
	prefix = int(input("[+] Enter Prefix Bettween (8/32) : "))
	
	#Set Your SubnetMask
	if prefix not in range(8,33):
		print('\033[91m'+"\n[+] Plaese write between (8/32) : ")
		exit()
		
	#Show IP/SubnetMask
	Net_Addr = CLASS_C_ADDR + '/' + str(prefix)
	print('\033[92m'+f"\n[+] Network Address : {Net_Addr}")

	#Can you make IP/SM ?
	try:
		network = ip.ip_network(Net_Addr)
	except:
		print('\033[91m'+"\nSorry, Failed To Create Network IP [ IP / (SM) not Make Sense!]")
		exit()
			
	#Show Ho many IP's	
	n = ( int(network.num_addresses) - 2 )
	print('\033[92m'+f"[+] Avialble IP's   : {n} ")
	
	#Show Configuretion
	print('\033[92m'+f"\n\t[+] Subnet Mask  : {str(network.netmask)}")
	
	#Create N-ID && B-ID
	First_ip = network.network_address
	Last_ip  = network.broadcast_address
	print('\033[92m'+f"\n\t[+] Network ID   : {First_ip}")
	print('\033[92m'+f"\t[+] Broadcast ID : {Last_ip}")	
	
	#Do you Want this Configuration?
	status = input("\n[+] This configuration okay? [Y/n] : ")
	status = status.lower()
	
	if status.strip() == 'y':
		Configure_state= False
		
#show ALl Availble IP Address
A_Hosts = input("[+] Do you want see all available hosts and save it? [Y/n] : ")
A_Hosts = A_Hosts.lower()
print("\n")

#Print All IP's
if A_Hosts.strip() == 'y':

	host = str(list(network.hosts()))
	ipArray = host.split(",")
	ipTable = Texttable()
	numbers = 0
	
	for ip in ipArray:
		pureIp = ip.split("('")
		pureIp = pureIp [1].split("')")
		pureIp = pureIp [0]
		ipTable.add_row([numbers, pureIp])
		numbers = numbers + 1
		
	# import to ips.txt	
	fileIp = open ("ips.txt","w")
	fileIp.write(ipTable.draw())
			
	print(GREEN+ipTable.draw())
