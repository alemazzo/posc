#!/bin/python3

# Modules import

# My imports
from posc import Configuration, parse_arguments

if __name__ == "__main__":
    args = parse_arguments()
    configurationFilePath = args.file

    configuration = Configuration.configurationfromYamlFile(
        configurationFilePath)

    if args.tasks:
        configuration.printTasks()

    elif args.apptypes:
        configuration.printApplicationTypes()

    elif args.task:
        configuration.executeTask(args.task)

    elif args.apptype and not args.app:
        if args.apptype == 'all':
            for apptype in configuration.applications:
                configuration.printApplicationsInSpecifiedType(apptype)
        else:
            configuration.printApplicationsInSpecifiedType(args.apptype)

    elif args.apptype and args.app:
        if args.apptype == 'all':
            if args.app == 'all':
                for apptype in configuration.applications:
                    for app in configuration.applications[apptype]:
                        configuration.installApplication(apptype, app)
            else:
                print("No sense man - one app but multiple source")
        else:
            if args.app == 'all':
                for app in configuration.applications[args.apptype]:
                    configuration.installApplication(args.apptype, app)
            else:
                configuration.installApplication(args.apptype, args.app)
