### Move My Server

Move My Server is a small script that is designed to allow users to easily move a server from one hypervisor to another. This script aims to handle everything but the destination by itself.

Currently this script has been tested against and written for CentOS 7 and Debian 9.

I hope you find it useful!

#### Requirements

This script relies on
- Python (2.7 or better should work just fine)
- rsync

#### Installation

No installation required , just put it in a directory and run as sudo/root

### Issues / Bug Reporting

All bugs can be submitted over at [The Github Issues page for this project](https://github.com/Deminarcis/move-my-server/issues)

#### TODO
- Add OpenSUSE support for all features
- Add support for specifying destination's port (we don't all use port 22 for SSH)
