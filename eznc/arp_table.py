from jnpr.junos import Device
from jnpr.junos.op.arp import ArpTable
from credentials import username, password


def print_arp(hostname):
    dev = Device(user=username, host=hostname, password=password)

    dev.open()

    arp_table = ArpTable(dev).get()

    for arp in arp_table:
        print hostname, arp.interface_name, arp.ip_address, arp.mac_address

    dev.close()


for host in ['R1', 'R2', 'R3']:
    print_arp(host)
