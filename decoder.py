from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# ...
stream = open('config.yml')
data = load(stream, Loader=Loader)


# Load directories
directories = data["directories"]
print(f"Directories = {directories}")

# Load applications
applications = data["applications"]
apt_applications = applications["apt"]
snap_applications = applications["snap"]
flatpak_applications = applications["flatpak"]
print(f"apt = {apt_applications}")
print(f"snap = {snap_applications}")
print(f"flatpak = {flatpak_applications}")

# Load tasks
tasks = data["tasks"]
print(f"tasks = {tasks}")
