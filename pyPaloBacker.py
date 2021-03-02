#!/usr/bin/env python3
import requests, datetime

# Generate the API Key using the following URL:
# https://<firewall-ip>/api/?type=keygen&user=<username>&password=<password>
api_key = ''
# Palo Firewall / Panorama IP
palo_IP = ''

# Reads file contents for write function
def readConf(fileName):
    with open(fileName, 'r') as i:
        line = i.read()
    return line

# Writes to file again amending file so it is the same as an export
def writeConf(fileName, content):
    file = content.splitlines()
    with open(fileName, 'w') as i:
        for line in file:
            if line == '<response status="success"><result><config version="9.0.0" urldb="paloaltonetworks">':
                i.writelines(['<?xml version="1.0"?>\n', '<config version="9.0.0" urldb="paloaltonetworks">\n'])
            elif line == '</config></result></response>':
                i.writelines(['</config>\n'])
            else:
                i.writelines('{}\n'.format(line))

# Main function
def main():
    # Get Date for filename
    x = datetime.datetime.now()
    # API url used to get running config, working as of 9.0.x
    url = 'https://{}/api/?type=config&action=show&key={}'.format(palo_IP, api_key)
    # Filename running-config-<date>.xml <date> format = 01-Jan-2021
    filename = 'running-config-{}.xml'.format(x.strftime("%d-%b-%Y"))
    # Downloads the running config, ignore SSL cert issues on... remove or keep verify=False if needed
    running_config = requests.get(url, allow_redirects=True, verify=False)
    # Init download write
    open(filename, 'wb').write(running_config.content)
    # Amend config to match an export from GUI
    writeConf(filename,readConf(filename))

# Run Program
if __name__ == '__main__':
    main()
