# Junos playground

This repository automatically provision four VMs. 
One Debian Linux and three VMs with Juniper Junos (vSRX). 

## install required software
- install [virtualbox] (https://www.virtualbox.org/wiki/Downloads)
    - make sure you install extension pack for virtualbox!!
- install [Vagrant 1.7+] (https://www.vagrantup.com/downloads.html)
- install vagrant plugins
    - `vagrant plugin install vagrant-host-shell`
    - `vagrant plugin install vagrant-junos`
- install [git] (http://git-scm.com/download) or [download](https://github.com/sergzin/juniper-play/archive/master.zip) source code
    - clone repository in your work folder
        - `git clone https://github.com/sergzin/juniper-play.git`
 
## start/stop VMs
- execute from work folder `vagrant up`
- after provisioning finished execute `vagrant ssh linux`
    - on windows use ssh client of your choice to connect to linux VM
    - use ssh key or the following credentials 
        login:`vagrant` password:`vagrant` 
- to stop VMs execute `vagrant halt` in working folder

## login to junos VMs
- connect to R1,R2,R3 from Linux VM: `ssh root@R1` use password `Juniper`
- alternatively you can can connect with `vagrant ssh R1` command

## topology

```
                            +---------+
                            |         |
                            | Linux   |
                            |         |
                            +----+----+
                        Mgmt LAN | 192.168.0.100/24
                                 |
    ge-0/0/1                     | ge-0/0/1                  ge-0/0/1
     +---------------------------+--------------------------+
   1 |                          2|                        3 |
+----+----+                 +----+----+                 +---+-----+
|         |ge-0/0/2 ge-0/0/2|         |ge-0/0/3 ge-0/0/2|         |
|   R1    +-----------------+   R2    +-----------------+   R3    |
|         |                 |         |                 |         |
+---------+                 +---------+                 +---------+
     |ge-0/0/3                                              |ge-0/0/3
     |                                                      |
     +------------------------------------------------------+
     
    R1-R2: 192.168.12.1-2/30
    R1-R3: 192.168.13.1-2/30
    R2-R3: 192.168.23.1-2/30
```

- shared management LAN
    - VMs connected to shared management LAN 192.168.0.0/24
    - port on vSRX ge-0/0/1
- Internet access
    - each VM provisioned by vagrant with internet access
 
