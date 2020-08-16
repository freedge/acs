# Ansible Collection - freedge.acs

Current status: this is under development and not working yet.

An unofficial module to configure Avocent ACS6000 and ACS8000 devices. It connects through SSH to the device and shoot commands in the format used by the list_configuration cli command.

At this moment, this is based, and still contains, source code from nokia.sros module, since it is the simplest implementation of a network_os I found.

# Installation

```
ansible-galaxy collection build
cd /myproject
ansible-galaxy collection install -p ./ ...freedge-acs-0.0.1.tar.gz
```

# Usage

## Inventory

This module uses the network_cli connection and the freedge.acs.classic network_os. Inventory should look like this:

```
[acsall]
acs ansible_connection=network_cli ansible_network_os=freedge.acs.classic ansible_user=admin ansible_password=avocent ansible_port=2222 ansible_host="127.0.0.1"
```

## Modules

The syntax of the module is the same that the one from list_configuration, see under the examples/ folder:

```
    - name: configure port
      configure_ports:
        ports:
        - port: "{{item.id}}"
          list_configuration:
          - echo off
          - cd /ports/serial_ports
          - set_cas {{item.id}}
          - set status={{item.status | default("enabled") }}
          - set rj45_pin-out=auto
...
          - #set script=
          - #set emergency=
          - next
          - disable_alerts
          - cd power
          - delete -
          - save --cancelOnError
          - echo on
          - commit
```

Note that the full output of the list_configuration should be written in there. At the moment, only a run in check mode is supported.



