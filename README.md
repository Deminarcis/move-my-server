#### Next-Release branch

Welcome the the next release branch.
Please be aware that this branch is an "in progress" branch and should be treated as if it has not been tested at all and probably broken.
There is the chance that it may work fine and even better than the latest stable release.

Consider this a beta, and like all beta builds it will have its bugs.

It is very possible for this to be completely broken

### Move My Server

Move My Server is a small script that is designed to allow users to easily move a server from one hypervisor to another. This script aims to handle everything but the destination by itself.

Currently this script has been tested against and written for CentOS 7 and Debian 9 and OpenSUSE Tumbleweed.

I hope you find it useful!

#### Requirements

This script relies on
- Python (2.7 or better should work just fine)
- rsync

#### Installation

No installation required , just put it in a directory and run as sudo/root

### Issues / Bug Reporting

All bugs can be submitted over at [The Github Issues page for this project](https://github.com/Deminarcis/move-my-server/issues)

#### GOALS FOR NEXT RELEASE
- Add support for specifying destination's port
- Allow the use of arguments/options to specify:
    - Destination
    - User
    - Server
    - Port
