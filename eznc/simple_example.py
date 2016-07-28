from jnpr.junos import Device
from credentials import username, password
from pprint import pprint

dev = Device(user=username, host='R2', password=password)

dev.open()

pprint(dev.facts)

dev.close()
