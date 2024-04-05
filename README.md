# Ansible System Information Collection Project

## Overview
This project automates the collection of system information from multiple machines using Ansible and Python scripting. It orchestrates the execution of a Python script (`script.py`) on target machines to gather various system details such as hostname, IP address, OS flavor, and disk usage.

## Project Structure
- `script.py`: Python script responsible for collecting system information based on commands specified in the `os_comands.json` file.
- `os_comands.json`: JSON file containing shell commands to collect system information.
- `project.yml`: Ansible playbook to execute the Python script on target machines and fetch the generated CSV file.
- `data_csv`: Generated CSV file containing collected system information.

## Usage
1. Ensure Ansible is installed on the control node and target machines.
2. Customize the `os_comands.json` file with the desired shell commands to collect system information.
3. Update the `project.yml` playbook if necessary, specifying target hosts and file paths.
4. Run the Ansible playbook `project.yml` using the `ansible-playbook` command.
5. Review the output of the command execution and the fetched CSV file for further analysis.

## Requirements
- Ansible
- Python 3.x

## Example Commands
```bash
ansible-playbook project.yml
