# -*- mode: ruby -*-
# vi: set ft=ruby :

require "vagrant-host-shell"
require "vagrant-junos"

Vagrant.configure(2) do |config|


  config.vm.define "linux", primary: true do |linux|
    linux.vm.box = "debian/jessie64"
    linux.vm.box_version = "8.2.0"
    linux.vm.box_check_update = false
    linux.vm.hostname = "Linux"
    linux.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"
    # linux.vm.network :forwarded_port, guest: 22, host: 2201
    linux.vm.network "private_network",
      ip: "192.168.0.100",
      netmask: "255.255.255.0",
      nic_type: 'virtio',
      virtualbox__intnet: "mgmt"
    linux.vm.provision :shell, keep_color: true do |sh|
      sh.path = "provisioning/provision.sh"
      sh.args = "provisioning/setup.yml provisioning/hosts/hosts"
    end
    linux.vm.provider "virtualbox" do |vb|
      vb.check_guest_additions = false
    end
  end

  config.vm.define "R1" do |router|
    router.vm.box = "juniper/ffp-12.1X47-D15.4-packetmode"
    router.vm.hostname = "R1"
    router.vm.synced_folder "", "/vagrant", disabled: true
    router.vm.network "private_network",
        ip: "192.168.0.1",
        netmask: "255.255.255.0",
        nic_type: 'virtio',
        virtualbox__intnet: "mgmt"
    router.vm.network "private_network",
        ip: "192.168.12.1",
        netmask: "255.255.255.252",
        nic_type: 'virtio',
        virtualbox__intnet: "r1-r2"
    router.vm.network "private_network",
        ip: "192.168.13.1",
        netmask: "255.255.255.252",
        nic_type: 'virtio',
        virtualbox__intnet: "r1-r3"
    router.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", "512"]
      vb.customize ["modifyvm", :id, "--cpus", "2"]
      vb.customize ["modifyvm", :id, "--nicpromisc1", "deny"]
      vb.customize ["modifyvm", :id, "--nicpromisc2", "deny"]
      vb.customize ["modifyvm", :id, "--nicpromisc3", "deny"]
      vb.customize ["modifyvm", :id, "--nicpromisc4", "deny"]
      vb.check_guest_additions = false
    end
  end

  config.vm.define "R2" do |router|
    router.vm.box = "juniper/ffp-12.1X47-D15.4-packetmode"
    router.vm.hostname = "R2"
    router.vm.synced_folder "", "/vagrant", disabled: true
    router.vm.network "private_network",
        ip: "192.168.0.2",
        netmask: "255.255.255.0",
        nic_type: 'virtio',
        virtualbox__intnet: "mgmt"
    router.vm.network "private_network",
        ip: "192.168.12.2",
        netmask: "255.255.255.252",
        nic_type: 'virtio',
        virtualbox__intnet: "r1-r2"
    router.vm.network "private_network",
        ip: "192.168.23.1",
        netmask: "255.255.255.252",
        nic_type: 'virtio',
        virtualbox__intnet: "r2-r3"
    router.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", "512"]
      vb.customize ["modifyvm", :id, "--cpus", "2"]
      vb.customize ["modifyvm", :id, "--nicpromisc1", "deny"]
      vb.customize ["modifyvm", :id, "--nicpromisc2", "deny"]
      vb.customize ["modifyvm", :id, "--nicpromisc3", "deny"]
      vb.customize ["modifyvm", :id, "--nicpromisc4", "deny"]
      vb.check_guest_additions = false
    end
  end

  config.vm.define "R3" do |router|
    router.vm.box = "juniper/ffp-12.1X47-D15.4-packetmode"
    router.vm.hostname = "R3"
    router.vm.synced_folder "", "/vagrant", disabled: true
    router.vm.network "private_network",
        ip: "192.168.0.3",
        netmask: "255.255.255.0",
        nic_type: 'virtio',
        virtualbox__intnet: "mgmt"
    router.vm.network "private_network",
        ip: "192.168.23.2",
        netmask: "255.255.255.252",
        nic_type: 'virtio',
        virtualbox__intnet: "r2-r3"
    router.vm.network "private_network",
        ip: "192.168.13.2",
        netmask: "255.255.255.252",
        nic_type: 'virtio',
        virtualbox__intnet: "r1-r3"
    router.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", "512"]
      vb.customize ["modifyvm", :id, "--cpus", "2"]
      vb.customize ["modifyvm", :id, "--nicpromisc1", "deny"]
      vb.customize ["modifyvm", :id, "--nicpromisc2", "deny"]
      vb.customize ["modifyvm", :id, "--nicpromisc3", "deny"]
      vb.customize ["modifyvm", :id, "--nicpromisc4", "deny"]
      vb.check_guest_additions = false
    end
  end

end
