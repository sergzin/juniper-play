from jnpr.junos import Device
from jnpr.junos.op.phyport import PhyPortTable
from lxml.etree import tostring
from pprint import pprint
from credentials import username, password


def recursive_dict(element):
    return element.tag, dict(map(recursive_dict, element)) or element.text


def print_interface_mac(hostname):
    dev = Device(user=username, host=hostname, password=password, gather_facts=False, normalize=True)

    dev.open()
    interface_output = dev.rpc.get_interface_information()

    print tostring(interface_output, method='xml', pretty_print=True)

    all_up = interface_output.xpath(".//physical-interface[starts-with(name,'ge') and oper-status='up']")

    for item in all_up:
        print hostname, item.find('name').text, item.find('current-physical-address').text, item.find('.//ifa-local').text
        # pprint(recursive_dict(item))

    dev.close()


def print_interface_table(hostname):
    dev = Device(user=username, host=hostname, password=password, gather_facts=False, normalize=True)
    dev.open()
    port_table = PhyPortTable(dev).get()
    for port in port_table:
        print hostname, port.name, port.macaddr, port.flapped
    dev.close()


for host in ['R1', 'R2', 'R3']:
    print_interface_mac(host)
    raw_input("Press enter to continue...")
    print_interface_table(host)
    raw_input("Press enter to continue...")
