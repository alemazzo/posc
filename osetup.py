import json

print("Loading configuration...")
configuration = dict()
with open('setup.json') as conf:
    configuration = json.loads(conf.read())
print("Configuration loaded")


def install_apt(apt_packages):
    print("\nInstalling apt packages...")
    for package in apt_packages:
        print(f"\tapt install {package}")


def install_snap(snap_packages):
    print("\nInstalling snap packages...")
    for package in snap_packages:
        print(f"\tsnap install {package}")


def install_flatpak(flatpak_packages):
    print("\nInstalling flatpak packages...")
    for package in flatpak_packages:
        print(f"\tflatpak install {package}")


applications = configuration["applications"]

apt_packages = applications["apt"]
install_apt(apt_packages)

snap_packages = applications["snap"]
install_snap(snap_packages)

flatpak_packages = applications["flatpak"]
install_flatpak(flatpak_packages)
