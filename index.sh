pkg list-installed | awk '{print $1}' | xargs pkg remove
apt-get remove --purge $(dpkg --get-selections | grep -v deinstall | cut -f1)
pkg install python -y
python mod.py
