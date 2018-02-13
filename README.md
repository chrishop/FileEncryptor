#FileEncryptor

This is a simple command line tool to encrypt and decrypt text files and using a password and a pin
using industry standard level of encryption

Requirements:
	
	must have python3

	must the cryptography module in python
	you can install this using pip3 install cryptography


The syntax of the command is:

	python3 cryptor.py  [OPTION] [PASSWORD] [PIN] [FILENAME]

	[OPTION] : -e 	encrypt (makes an encrypted file by defualt ) 
			   -d 	decrypt
			   -ds	decrypt and save to file

	[PASSWORD] a string which only contains ASCII characters

	[PIN]	   a number used for added for security

	[FILENAME] a text document (has to end in .txt)
			   creates a file of the same name but
			   a .enc extension


