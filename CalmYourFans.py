#
#   _____      _       __     __              ______              
#  / ____|    | |      \ \   / /             |  ____|             
# | |     __ _| |_ __ __\ \_/ /__  _   _ _ __| |__ __ _ _ __  ___ 
# | |    / _` | | '_ ` _ \   / _ \| | | | '__|  __/ _` | '_ \/ __|
# | |___| (_| | | | | | | | | (_) | |_| | |  | | | (_| | | | \__ \
#  \_____\__,_|_|_| |_| |_|_|\___/ \__,_|_|  |_|  \__,_|_| |_|___/
																 
# 
import socket


def DataInput():
	iDRACIP=input("Enter iDRAC IP address: ")
	try:
		socket.inet_aton(iDRACIP)
		
	except socket.error:
		print("Address IP format not respected. [X.X.X.X]")
		DataInput()

	print("root will be used as IPMI user")
	iDracPw= input("Enter iDRAC password [calvin]: ")

	FanSpeed= input("Enter the desired fan speed in percentage [25]: ")
	try:
		if(FanSpeed.isnumeric() ==False):
			raise SyntaxError()
	except:
		print("Fan speed must be a numerical value between 25 and 100")
		DataInput()

	try:
		if(int(FanSpeed)<25):
			 
			raise SyntaxError()
	except:
		print("Fan speed must be higher than 24% or iDRAC will generate an error ") 
		DataInput()

	print("EndOfCode")
 
DataInput()