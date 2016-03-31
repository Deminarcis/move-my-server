#!/usr/bin/python

# Imports .... I may have too many or some that arent going to be used
import os
import glob
from subprocess import call

# Variables
user = os.getuid()
exceptions = [ "/boot", "/proc", "/sys", "/tmp", "/dev", "/var/lock", "/etc/fstab", "/etc/mtab", "/etc/resolv.conf", "/etc/conf.d/net", "/etc/network/interfaces", "/etc/networks", "/etc/sysconfig/network*", "/etc/sysconfig/hwconf", "/etc/sysconfig/ip6tables-config", "/etc/sysconfig/kernel", "/etc/hostname", "/etc/HOSTNAME", "/etc/hosts", "/etc/modprobe*", "/etc/modules", "/net", "/lib/modules", "/etc/rc.conf" ]


#check_root
print "you are logged in as %s" % user
if user != 0:
    raise EnvironmentError, "Warning: you are not logged in as root. This script contains commands that must be run as root, please restart using sudo or run this script as root"
    exit()

#checking dependancies
print "Checking for missing dependancies"
if os.access("/usr/bin/rsync", os.R_OK) or os.access("/bin/rsync", os.R_OK):
    print "rsync is installed, moving on"
else:
    print "We will need to install rsync to continue"
    os.system('yum install -y rsync ')


#Create exceptionf file
print "Creating exceptions file(s)"
open("./exclusion", "w")
with open("./exclusion", "w") as exclusion:
    for item in exceptions:
        exclusion.write("%s\n" % item)
exclusion.close()
exclusion = str("./exclusion")

#Set up SSH destination
print "Next we will set the destination, please enter the Server IP, user and port when promtped. Note that the user you are logging in as will need read/write access to the directory. Alternatively you can use root."
login_user = str(raw_input("Enter the user you are logging in as: "))
server = str(raw_input("Please enter the server you would like to back up to: "))
#port = str(raw_input("Please enter the port of the server (default is 22): "))
destination_folder = str(raw_input("Enter the directory on the new server you will be copying to: "))

print "Performing transfer over ssh"
os.system('rsync -e ssh -azPxv --delete-after --exclude-from=%s / %s@%s:%s' % (exclusion, login_user, server, destination_folder))
