from jnpr.junos import Device
from credentials import username, password
from lxml.etree import tostring

dev = Device(user=username, host='R1', password=password, normalize=True, gather_facts=False)

dev.open()
chassis_output = dev.rpc.get_route_information(extensive=True, exact=True, destination='192.168.0.1/32')

print tostring(chassis_output, method='xml', pretty_print=True)

dev.close()
