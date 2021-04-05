# gather-interface-information

This project collects information from networking devices (as of right now nexus sw only) and saves it `csv` format to
import it to our M&M IPAM solution.

## Requirements
* Ansible >=2.9
* Python >=3.8
* Parmiko
* sshpass
* Vault password

## How to use?
* Configure a `.secret`