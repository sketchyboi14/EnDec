import os
import time
import subprocess

try:
	print ("[+]Thank you for using my program. To report bugs, go to https://github.com/sketchyboi14/EnDec/issues.)
	time.sleep(5)

	subprocess.call(["clear"])

	print ("""

		[1] Generate a key with password
		[2] Generate a random key
		[3] Encrypt text
		[4] Encrypt a file
		[5] Decrypt text
		[6] Decrypt a file

		""")
	Choice = raw_input("Select what you want to do: ")

	if Choice == "1":
		subprocess.call(["clear"])
		import Generate_Key_With_Pwd
	elif Choice == "2":
		subprocess.call(["clear"])
		import Generate_Random_Key
	elif Choice == "3":
		subprocess.call(["clear"])
		import Encrypt_String
	elif Choice == "4":
		subprocess.call(["clear"])
		import Encrypt_File
	elif Choice == "5":
		subprocess.call(["clear"])
		import Decrypt_String.py
	elif Choice == "6":
		subprocess.call(["clear"])
		import Decrypt_File
except:
	KeyboardInterrupt()
	time.sleep(1)
	
	print "\n\nWould you like to go back to the main menu?"
	time.sleep(2)
	Choice = raw_input("[Y]es or [N]o: ")

	if Choice == "y" or Choice == "Y":
		subprocess.call(["python2", "EnDec.py"])
	elif Choice == "n" or Choice == "N":
		time.sleep(1)
		print"\nExiting script...Go to https://github.com/sketchyboi14/EnDec/issues to report issues."
		time.sleep(3)
		quit()
