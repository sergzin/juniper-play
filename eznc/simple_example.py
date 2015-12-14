from jnpr.junos import Device
from credentials import username, password

dev = Device(user=username, host='R1', password=password)

dev.open()

print dev.facts

dev.close()
