#!/bin/python3
# Modules import
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# My imports
from posc.arguments.parser import parse_arguments


def load_configuration(configFile: str):
    stream = open(config_file)
    data = load(stream, Loader=Loader)
    return data


def explode(data):
    # Load directories
    directories = data["directories"]
    #print(f"Directories = {directories}")

    # Load applications
    applications = data["applications"]
    apt_applications = applications["apt"]
    snap_applications = applications["snap"]
    flatpak_applications = applications["flatpak"]
    #print(f"apt = {apt_applications}")
    #print(f"snap = {snap_applications}")
    #print(f"flatpak = {flatpak_applications}")

    # Load tasks
    tasks = data["tasks"]
    #print(f"tasks = {tasks}")

    return applications, tasks


def showTasks(tasks):
    for task in tasks:
        print(f"[T] {task}")


def executeTask(tasks, taskName):
    if not taskName in tasks:
        print(f"Task : {taskName} is not a valid task name")
        return
    task = tasks[taskName]
    print(f"Executing {taskName}")
    print(task)


if __name__ == "__main__":
    args = parse_arguments()
    config_file = args.file
    data = load_configuration(config_file)
    applications, tasks = explode(data)

    if args.tasks:
        showTasks(tasks)
    elif args.t:
        executeTask(tasks, args.t)
