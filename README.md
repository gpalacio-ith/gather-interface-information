# gather-interface-information

This project collects information from nexus switches and prints interface information in `csv` format to screen.
It is usually used to import that info to our M&M IPAM solution.

## Requirements
* Ansible >=2.9
* Python >=3.8
* Ansible Module: cisco.nxos.nxos
* Parmiko
* sshpass
* Vault password

## How to use?
* Add a file `.secrets/vault_pass` that contains the vault password.
* Update inventory file as necessary to point to nexus switches.
* Run the playbook `ansible-playbook nexus_gather_facts.yml`
  (files are saved in `./playbook/facts`)
* Run the Python parser `nexu_parse_files.py` which prints interface information in the terminal.  