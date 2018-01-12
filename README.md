
rest-server-rpm
=========


CentOS/RHEL/Fedora/Amazon RPMs for Rest Server <https://github.com/restic/rest-server>

Tested on x64 Fedora 26

Benefits of this rpm
--------

- Binary built for specic target (COPR)
- Systemd
- Firewalld service
- User/group (restsvr) added for daemon

Install
--------

RPMs are built on COPR

sudo dnf copr enable copart/restic

sudo dnf install rest-server

