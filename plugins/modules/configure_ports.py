#!/usr/bin/python

DOCUMENTATION = '''
---
module: freedge.acs
author: Freedge
short_description: Return device information
'''

EXAMPLES = '''
- name: get device info
  device_info:
'''

RETURN = '''
output:
  description: device information gathered
  returned: success
  type: dict
  sample:
    network_os: "freedge.acs"
    network_os_hostname: "Berlin"
    network_os_model: "7750 SR-12"

    network_os_version: "B-19.5.R2"
    sros_config_mode: "classic"
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection


def computeDiff(module, inventory, real):
    if len(inventory) != len(real):
        module.warn("inventory does not contain the full config %d %d"% (len(inventory), len(real)))
        return inventory

    diff = []
    # TODO: something smarter ?
    for i, l in enumerate(inventory):
        if inventory[i] != real[i] and not (real[i].startswith("#") and inventory[i] is None):
            module.warn("%d: %s vs %s" % (i, inventory[i], real[i]))
            diff = diff + [inventory[i]]
    return diff
            
        
        
    

def main():
    argument_spec = dict(ports=dict(type="list"))
    module = AnsibleModule(argument_spec=argument_spec,
                                    supports_check_mode=True)
    connection = Connection(module._socket_path)

    ports = module.params['ports']
    actualPort = []
    changed = False
    if not module.check_mode:
        raise NotImplementedError("only check mode supported")
    for port in ports:
        readObject = {}
        portId = int(port['port'])
        result = connection.send_command("list_configuration ports/serial_ports/%d" % portId)
        actualList = [ r for r in result.split("\n") if r ]
        actualPort += [ actualList ]
        if len(computeDiff(module, port['list_configuration'], actualList)) > 0:
            changed = True


    result = {'changed': changed, 'ports': ports, 'actualPorts': actualPort}

    module.exit_json(**result)


if __name__ == '__main__':
    main()
