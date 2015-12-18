from jnpr.junos import Device
from credentials import username, password
from lxml.etree import tostring

dev = Device(user=username, host='R1', password=password, normalize=True)

dev.open()
chassis_output = dev.rpc.get_chassis_inventory()

print tostring(chassis_output, method='xml', pretty_print=True)

dev.close()
