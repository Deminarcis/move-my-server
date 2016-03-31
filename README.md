### Move My Server

Move My Server is a small script that is designed to allow users to easily move a server from one hypervisor to another. This script aims to handle everything but the destination by itself.

Currently this script is written to work with CentOS 6 and 7. If i get enough use from it i may expand this later.

I hope you find it useful!

#### Requirements

This script relies on
- Python (2.7 or better should work just fine)
- rsync
- A distro that uses Yum

#### Installation

No installation required , just put it in a directory and run as sudo/root

### Issues / Bug Reporting

All bugs can be submitted over at [The Github Issues page for this project](https://github.com/Deminarcis/move-my-server/issues)

#### TODO
- Add support for more than just systems using Yum starting with its successor DNF
- Add OpenSUSE and Debian (Potentially Ubuntu by extension) Support for all features
- Add support for specifying port
- Support preserving Systemd unit files (currently we assume you are using upstart)
