# Junos playground

## install required software
- install [virtualbox 1.5+] (https://www.virtualbox.org/wiki/Downloads)
  - make sure you install extension pack for virtualbox!!
- install [Vagrant 1.7+] (https://www.vagrantup.com/downloads.html)
- install vagrant plugins
  - `vagrant plugin install vagrant-host-shell`
  - `vagrant plugin install vagrant-junos`
- install [git] (http://git-scm.com/download)
- clone repository in your work folder
  - `git clone https://github.com/sergzin/juniper-play.git`
 
## start VMs
- execute from work folder `vagrant up`
- after provisioning finished execute `vagrant ssh linux`
  - on windows use ssh client of your choice to connect to linux VM
  - use ssh key or the following credentials 
    login:`vagrant` password:`vagrant` 

## connect to junos VMs
- connect to R1,R2,R3 from VM `ssh root@R1` use password `Juniper`
- alternatively you can can connect with `vagrant ssh R1` command