#!/bin/python3

# Modules import

# My imports
from posc import Configuration
from posc.arguments.parser import parse_arguments


def explode(data):
    # Load directories
    directories = data["directories"]
    # print(f"Directories = {directories}")

    # Load applications
    applications = data["applications"]
    apt_applications = applications["apt"]
    snap_applications = applications["snap"]
    flatpak_applications = applications["flatpak"]
    # print(f"apt = {apt_applications}")
    # print(f"snap = {snap_applications}")
    # print(f"flatpak = {flatpak_applications}")

    # Load tasks
    tasks = data["tasks"]
    # print(f"tasks = {tasks}")
    return applications, tasks


if __name__ == "__main__":
    args = parse_arguments()
    configurationFilePath = args.file

    configuration = Configuration.configurationfromYamlFile(
        configurationFilePath)

    if args.tasks:
        configuration.printTasks()
    elif args.t:
        task = args.t
        configuration.executeTask(task)
