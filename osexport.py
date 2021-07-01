import os
import json


def get_apt_installed_list():
    stream = os.popen('apt list --installed | grep "\[installed\]"')
    installed = stream.read().splitlines()
    print(installed)
    installed = [(elem.split('/')[0], elem.split('/')[1].split(' ')[1])
                 for elem in installed]
    return installed


exported = dict()
exported["grub"] = dict()
exported["applications"] = dict()
exported["applications"]["apt"] = list()
exported["applications"]["snap"] = dict()

apt_installed = get_apt_installed_list()
for apt_element in apt_installed:
    exported["applications"]["apt"].append({
        "name": apt_element[0],
        "version": apt_element[1]
    })


output = json.dumps(exported)
with open('output.json', 'w') as file:
    file.write(output)
