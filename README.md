This is a repo demoing how to rewrite a linux deploy ansible script in python.

Prerequisites for the linux box:
python 2.7 (should be on there already)
yum install ansible
pip install termcolor

Run commands:
To run the ansible version:
ansible-playbook main.yml -i hosts

To run the python version:
python linux_deploy.py
