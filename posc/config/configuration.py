from posc import loader


class Configuration:

    @staticmethod
    def configurationfromYamlFile(file: str):
        data = loader.loadYamlFromFile(file)
        return Configuration(data["tasks"], data["applications"])

    def __init__(self, tasks, applications):
        self.tasks = tasks
        self.applications = applications

    def printTasks(self):
        for task in self.tasks:
            print(f'[T] {task}')

    def executeTask(self, taskName):
        if not taskName in self.tasks:
            print(f"Task : {taskName} is not a valid task name")
            return
        task = tasks[taskName]
        print(f"Executing {taskName}")
        print(task)

    def printApplicationsType(self):
        for applicationType in self.applications:
            print(f'[AT] {applicationType}')

    def printApplicationsInSpecifiedType(self, applicationTypeName):
        if not applicationTypeName in self.applications:
            print(
                f"Application Type : {applicationTypeName} is not a valid application type name")
            return

        apps = self.applications[applicationTypeName]
        for app in apps:
            print(f'[A] {app}')

    def installApplication(self, applicationTypeName, applicationName):
        if not applicationTypeName in self.applications:
            print(
                f"Application Type : {applicationTypeName} is not a valid application type name")
            return
        apps = self.applications[applicationTypeName]
        if not applicationName in apps:
            print(
                f"Application : {applicationName} is not a valid application for type {applicationTypeName}")
            return

        print(f"Installing {applicationName} [{applicationTypeName}]")
