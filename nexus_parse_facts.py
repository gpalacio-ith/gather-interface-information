#! /usr/bin/python
import os
import glob
import json


# Process the JSON file containing the facts about one device
def device_interface_information(file_name):
    # Loads the file contents into a dic
    with open(file_name, 'r') as j:
        device_facts = json.loads(j.read())

    # Prints device name
    print('-----------------------')
    print(device_facts['ansible_net_hostname'])
    print('-----------------------')

    # Loads interface facts only
    interfaces_info = device_facts["ansible_net_interfaces"].items()
    for each_interface, int_info in interfaces_info:
        if "ipv4" in int_info:
            print(device_facts['ansible_net_hostname'] + ',' + each_interface + ','  + int_info["ipv4"]["address"] + '/' + int_info["ipv4"]["masklen"])
    print('\n')


# Main Block
def main():
    # Iterates over all of the device facts files
    os.chdir("./playbook/facts")
    for file in glob.glob("*_facts.json"):
        device_interface_information(file)


if __name__ == "__main__":
    main()