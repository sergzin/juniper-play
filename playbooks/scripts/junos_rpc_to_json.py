#!/usr/bin/python

import json
import xmltodict
from jnpr.junos import Device
from lxml.etree import tostring


def to_py(device, response, **kvargs):
    return xmltodict.parse(tostring(response))


def rpc_to_json(device=Device, rpc=str, pretty=None):
    """
    Convert junos RPC output to json
    :param device:  Connector to junos device
    :type device: `Device`
    :param rpc: rpc query in XML format '<get-chassis-inventory/>'
    :type rpc: `str`
    :param pretty: if True print indented output
    :return:
    """
    if not device.connected:
        device.open()
    reply = device.execute(rpc, to_py=to_py)
    return json.dumps(reply, indent=pretty)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Return json from Junos XML RPC query')
    parser.add_argument("--host", required=True, help="Specify host to connect to")
    parser.add_argument("--username", required=True, help="Specify the username")
    parser.add_argument("--password", required=True, help="Specify the password")
    parser.add_argument("--rpc", required=True, help="Specify the XML RPC query")
    args = parser.parse_args()

    dev = Device(user=args.username, host=args.host, password=args.password)
    print rpc_to_json(dev, args.rpc, pretty=True)
    dev.close()
