#simple one time pad helper for hand written messages
#plan is to eventually have encode, decode, and generate pads

#legal characters
#this can be changed, but for now i feel that numbers, 
#a single case of characters, and the question mark are enough
#maybe this should be loaded from a config file later?
alphabet = "0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
alphabet_chars = []
for c in alphabet:
	alphabet_chars.append(c)
	
#temporary hardcoded message and key
message = "This is the Message!!!!! What time should we meeT? 12:30?"
key = "One thing that you will get to know about programming, is that programmers like to be lazy. If something has been done before, why should you do it again?"


#takes a string and
#returns a character list with illegal characters removed
def clean(s):

	chars = []
	
	for c in s:
		if c.upper() in alphabet:
			chars.append(c.upper())
		
	return chars
	
	
#encrypt a single character
#this is probably not neccesary
#but im going for readability
def encrypt_char(m, k):
	m_int = alphabet.index(m)
	#print("m = "+m+" , "+str(m_int))
	k_int = alphabet.index(k)
	#print("k = "+k+" , "+str(k_int))
	c_int = (m_int + k_int) % len(alphabet)
	#print("("+str(m_int)+" + "+str(k_int)+") % "+str(len(alphabet))+" = "+str(c_int))
	return alphabet_chars[c_int]

#takes a message and a key (strings)
#returns encrypted message (string)
def encrypt(m, k):
	
	#clean the input
	m_chars = clean(m)
	k_chars = clean(k)

	#holding area for encrypted message
	c_chars = []
	
	for i in range(0, len(m_chars)):
		c_chars.append(encrypt_char(m_chars[i], k_chars[i]))
	
	return "".join(c_chars)
	
	
#encrypt a single character
#this is probably not neccesary
#but im going for readability
def decrypt_char(m, k):
	m_int = alphabet.index(m)
	#print("m = "+m+" , "+str(m_int))
	k_int = alphabet.index(k)
	#print("k = "+k+" , "+str(k_int))
	c_int = (m_int - k_int) % len(alphabet)
	#print("("+str(m_int)+" - "+str(k_int)+") % "+str(len(alphabet))+" = "+str(c_int))
	return alphabet_chars[c_int]
	
#takes a message and a key (strings)
#returns encrypted message (string)
def decrypt(m, k):
	
	#clean the input
	m_chars = clean(m)
	k_chars = clean(k)

	#holding area for encrypted message
	c_chars = []
	
	for i in range(0, len(m_chars)):
		c_chars.append(decrypt_char(m_chars[i], k_chars[i]))
	
	return "".join(c_chars)
	
