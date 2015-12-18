from jinja2 import Template, FileSystemLoader, Environment

template = "Hello {{ item }}!"
data = ['Juniper', 'Junos', 'FreeBSD', 'world']

raw_input("\n\nExample with dictionary and named argument")
print Template(template).render({'item': 'Test'})
print Template(template).render(item='Test')

raw_input("\n\nExample with named arguments")
for i in data:
    print Template(template).render(item=i)

template_for = """{% for item in data %}
Hello {{ item }}!
{% endfor %}"""

raw_input("\n\nExample with for loop in template")
print Template(template_for).render(data=data)

interface_data = {
    'name': 'ge-0/0/1',
    'unit': 100,
    'address': '10.0.0.1/24'
}

env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True, lstrip_blocks=True)
template_interface = env.get_template('interface')
raw_input("\n\nExample generating interface configuration")
print template_interface.render(interface_data)

many_interfaces_data = {
    'ge-0/0/1': {
        0: ['10.0.0.1/24', '10.0.0.2/24', '10.1.0.1/24'],
        100: ['10.0.100.1/24']
    },
    'ge-0/0/2': {
        101: ['10.2.101.1/24', '10.0.0.1/24']
    }
}

template_interfaces = env.get_template('interfaces')
raw_input("\n\nExample generating configuration for many interfaces")
print template_interfaces.render(interfaces=many_interfaces_data)
