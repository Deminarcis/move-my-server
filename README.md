### Move My Server

Move My Server is a small script that allows users to easily move a server from one hypervisor to a backup server. It can probably do other stuff, but this is what i made it for.

I hope you find it useful!

#### Requirements

You will only need Python to begin with but in the spirit of transparency this script will make sure the following are installed:

- Python (2.7 should work, but it is set up to use python3)
- rsync

If you dont have rsync installed then the script will get it from your package manager.

#### Supported / Tested on:

- Debian 8 (Jessie)
- CentOS 7 (1511 build)
- OpenSUSE Tumbleweed
- Fedora 24
- Ubuntu 14.04 and 16.04.1

#### Installation
unzip and run.

### Issues / Bug Reporting

All bugs can be submitted over at [The Github Issues page for this project](https://github.com/Deminarcis/move-my-server/issues)


#### TODO

- Create a better default exclusions list
- make some switches for quick arguments / scripting
