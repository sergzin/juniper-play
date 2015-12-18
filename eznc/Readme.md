# Juniper junos-eznc

junos-eznc - is a Python library for Junos automation

## Links

- [official documentation](http://www.juniper.net/techpubs/en_US/release-independent/junos-pyez/information-products/pathway-pages/index.html)
- [github repository](https://github.com/Juniper/py-junos-eznc)
- [API documentation](http://junos-pyez.readthedocs.org/en/1.2.3/)
- [Jinja template language](http://jinja.pocoo.org/)

## Examples demonstrating RPC queries 

 - assign username and password in `credentials.py`
 - `simple_example.py` - simplest possible example. prints device facts.
 - `simple_example_rpc.py` - example of using rpc requests.
    - connect to device `ssh root@R1 -s netconf`
        - `-s netconf` starts netconf instead of c-shell  
    - paste the following to netconf shell prompt:
     `<rpc><get-chassis-inventory/></rpc> ]]>]]>`
 - `xpath_example.py` - usage of xpath expressions in XML RPC 
    - [XPath Overview](http://www.juniper.net/documentation/en_US/junos14.2/topics/concept/junos-script-automation-xpath-overview.html)

## Examples demonstrating Templating

 - in Python world Jinja is one of the most used template engines
 - `templating_example.py` - demonstrates basic template usage