#!/usr/bin/python

check_non_root () {
    if [ "$(id -u)" != "0" ]; then
        fatal "\
This script uses commands which need root. Please run this script as root or with sudo.  Aborting."
    fi
}

install_dependancies () {
    if ! rpm -q rsync > /dev/null; then
        echo -e"Rsync is not installed. Installing Rsync so this script can complete. \n
        Please note that this will fail if you have no internet connection"
        yum -y install rsync
    fi
}

create_exceptions () {

}
