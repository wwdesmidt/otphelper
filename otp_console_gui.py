import otp
import sys

def printUsage():
	print("usage: [-edh] [message [key]]")
	print("\n")
	print("options:")
	print("         -e")
	print("         -d")
	print("         -h")

#for i in range(1,len(sys.argv)):
#	print(sys.argv[i])

printUsage()
print("\n")
print("\n")
print("\n")
print("\n")
	
message = input("Message: ")
key =     input("    Key: ")

if "-e" not in sys.argv and "-d" not in sys.argv:
	encrypt = input("(E)ncrypt/(D)ecrypt? ")

print("\n")

print("\n")