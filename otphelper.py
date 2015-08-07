import otp
import sys
import argparse

#i still need to figure out how this works
parser = argparse.ArgumentParser(
        description="otr helper description here",
        epilog="All arguments are optional. You will be prompted for required information that is not passed as an arguement.")
parser.add_argument("-e", action="store_true", help="encrypt the message using the key")
parser.add_argument("-d", action="store_true", help="decrypt the message using the key")
parser.add_argument("-m", metavar="message", help="plaintext or cyphertext to encrypt or decrypt")
parser.add_argument("-k", metavar="key", help="key used to encrypt or decrypt the message")
args = parser.parse_args()



#message is required, if no message was passed prompt for it

if args.m == None:
        message = input("Message: ")
else:
        message = args.m

if args.k == None:
        key = input("    Key: ")
else:
        key = args.k



### NEED TO CHECK IF THE KEY IS >= the length of the message



#if user didnt specify encrypt or decrypt ask
choice_encrypt=False
choice_decrypt=False
        
if not args.e and not args.d:
        
        choice_ok=False

        
        while not choice_ok:
                
                action_choice = input("(E)ncrypt/(D)ecrypt? ")
                
                if action_choice == "E" or action_choice == "e":
                        choice_ok=True
                        choice_encrypt=True
                        
                elif action_choice == "D" or action_choice == "d":
                        choice_ok=True
                        choice_decrypt=True

                else:
                        print("invalid selection")

else:
        if args.e:
                choice_encrypt=True

        if args.d:
                choice_decrypt=True
                
print("\n")

if choice_encrypt:
        print("ENCRYPTED: "+otp.encrypt(message, key)+"\n")

if choice_decrypt:
        print("DECRYPTED: "+otp.decrypt(message, key)+"\n")

