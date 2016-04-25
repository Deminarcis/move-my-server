#!/usr/bin/python

# Imports
import os
import sys
import platform

# Static Variables
distro = platform.linux_distribution()[0]
user = os.getuid()
ssh_port = 22
exceptions = [ "/boot", "/proc", "/sys", "/tmp", "/dev", "/var/lock", "/etc/fstab", "/etc/mtab", "/etc/resolv.conf", "/etc/conf.d/net", "/etc/network/interfaces", "/etc/networks", "/etc/sysconfig/network*", "/etc/sysconfig/hwconf", "/etc/sysconfig/ip6tables-config", "/etc/sysconfig/kernel", "/etc/hostname", "/etc/HOSTNAME", "/etc/hosts", "/etc/modprobe*", "/etc/modules", "/net", "/lib/modules", "/etc/rc.conf" ]


#check_root
print "you are logged in as %s" % user
if user != 0:
    raise EnvironmentError, "You are not logged in as root. This script contains commands that must be run as root, please restart using sudo or run this script as root"
    exit()
print ""
print "we detect you are running %s" % distro
#Checking dependancies
print "Checking for missing dependancies"
print ""
if os.access("/usr/bin/rsync", os.R_OK) or os.access("/bin/rsync", os.R_OK):
    print "rsync is installed, moving on"
else:
    print "We will need to install rsync to continue"
    if distro == "CentOS Linux":
        os.system('yum install -y rsync')
    if distro == "debian":
        os.system('apt-get install -y rsync')
    if distro == "openSUSE":
        os.system('zypper in rsync')
    if distro == "Ubuntu"
        os.system('apt install -y rsync')

#Create exceptionf file
print "Creating exceptions file(s)"
open("./exclusion", "w")
with open("./exclusion", "w") as exclusion:
    for item in exceptions:
        exclusion.write("%s\n" % item)
exclusion.close()
exclusion = str("./exclusion")

#Set up SSH destination
print "Next we will set the destination, please enter the details when prompted when. Note: The user you are logging in as will need read/write access to the directory."
print ""
login_user = str(raw_input("Enter the user you are logging in as: "))
server = str(raw_input("Please enter the server you would like to back up to: "))
destination_folder = str(raw_input("Enter the directory on target server: "))
print ""
print "Performing transfer over ssh"
os.system('rsync -e "ssh -p %s" -azPxvh --progress --delete-after --ignore-errors --exclude-from=%s / %s@%s:%s' % (ssh_port, exclusion, login_user, server, destination_folder))
