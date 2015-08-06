import otp
import sys

import argparse

#i still need to figure out how this works
parser = argparse.ArgumentParser(description='otr helper description here')
parser.add_argument("-e", action="store_true", help="Encrypt the message using the key")
parser.add_argument("-d", help="Decrypt the message using the key")
args = parser.parse_args()


#for i in range(1,len(sys.argv)):
#	print(sys.argv[i])

print("\n")
print("\n")
print("\n")
print("\n")
	
message = input("Message: ")
key =     input("    Key: ")

#this is broken but i think it works something like this
if args["-e"]:
        print("encrypting")
else:
        print("not encrypting")
        
encrypt = input("(E)ncrypt/(D)ecrypt? ")

print("\n")

print("\n")
