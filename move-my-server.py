#!/usr/bin/python3

# Imports
import sys
import platform

# Static Variables
distro = platform.linux_distribution()[0]
os = platform.system()
import os
user = os.getlogin()
uid = os.getuid()
exceptions = [ "/boot", "/proc", "/sys", "/tmp", "/dev", "/var/lock", "/etc/fstab", "/etc/mtab", "/etc/resolv.conf", "/etc/conf.d/net", "/etc/network/interfaces", "/etc/networks", "/etc/sysconfig/network*", "/etc/sysconfig/hwconf", "/etc/sysconfig/ip6tables-config", "/etc/sysconfig/kernel", "/etc/hostname", "/etc/HOSTNAME", "/etc/hosts", "/etc/modprobe*", "/etc/modules", "/net", "/lib/modules", "/etc/rc.conf" ]



#check_root
print ("You are logged in as %s" % user)
if os.getuid() != 0:
    exit("You are not logged in as root. This script contains commands that must be run as root, please restart using sudo or run this script as root")
print ("we detect you are running %s" % distro)
# Checking for Windows or OS X
if os == 'Darwin' or 'Windows':
    print ("You will need to install and add Rsync to your path by yourself for this script to run")
    print ("If you have not installed Rsync and added it to your path then this will fail. If you are on OS X, Ports or Homebrew should be able to help you with this. Or you can manually install if you. like")

#Checking dependancies
print ("")
print ("Checking for missing dependencies")
if os.access("/usr/bin/rsync", os.R_OK) or os.access("/bin/rsync", os.R_OK):
    print ("rsync is installed, moving on")
else:
    print ("We will need to install rsync to continue")
    if distro == "CentOS Linux":
        os.system('yum install -y rsync')
    if distro == "debian":
        os.system('apt-get install -y rsync')
    if distro == "openSUSE":
        os.system('zypper in -y rsync')
    if distro == "Ubuntu":
        os.system('apt install -y rsync')
    if distro == "Fedora":
        os.system('dnf install -y rsync')

#Create exceptionf file
print ("Creating exceptions file(s)")
open("./exclusion", "w")
with open("./exclusion", "w") as exclusion:
    for item in exceptions:
        exclusion.write("%s\n" % item)
exclusion.close()
exclusion = str("./exclusion")

#Set up SSH destination
print ("Next we will set the destination, please enter the details.")
print ("")
login_user = input("Enter the user you are logging in as: ")
if len(login_user) < 1:
    exit("You need to specify a user")
server = input("Please enter the server you would like to back up to: ")
if len(server) < 1:
    exit("You need to specify a remote server or localhost")
destination_folder = input("Enter the directory on target server: (default is the remote home directory) ")
if len(destination_folder) < 1:
    destination = os.path.expanduser('~')
ssh = input("Do you need to set a custom ssh port? ")
if ssh == "Yes" or "yes" or "y":
    ssh = input("Enter your ssh port: ")
else:
    ssh = 22
if len(ssh) < 1:
    ssh = 22
print ("")
print ("Performing transfer over ssh")
os.system('rsync -e "ssh -p %s" -azPxvh --progress --delete-after --ignore-errors --exclude-from=%s / %s@%s:%s' % (ssh, exclusion, login_user, server, destination_folder))
