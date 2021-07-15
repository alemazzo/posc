from posc import loader


class Configuration:

    @staticmethod
    def configurationfromYamlFile(file: str):
        from posc import Application, Task, Operation
        data = loader.loadYamlFromFile(file)

        applications = dict()
        tasks = dict()

        for taskname in data["tasks"]:
            operations = [Operation(command)
                          for command in data["tasks"][taskname]["commands"]]
            tasks[taskname] = Task(
                taskname, operations)

        for key in data["applications"].keys():
            applications[key] = [Application.fromObject(
                app, key) for app in data["applications"][key]]

        return Configuration(tasks, applications)

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
        task = self.tasks[taskName]
        print(f"Executing {taskName}")
        task.executeTask()

    def printApplicationTypes(self):
        for applicationType in self.applications:
            print(f'[AT] {applicationType}')

    def checkApplicationType(self, applicationTypeName):
        if not applicationTypeName in self.applications:
            print(
                f"Application Type : {applicationTypeName} is not a valid application type name")
            return False
        return True

    def checkApplicationName(self, applicationName, apps):
        if not applicationName in apps:
            print(
                f"Application : {applicationName} is not a valid application for type {applicationTypeName}")
            return False
        return True

    def printApplicationsInSpecifiedType(self, applicationTypeName):
        if not self.checkApplicationType(applicationTypeName):
            return
        apps = self.applications[applicationTypeName]
        for app in apps:
            print(f'[A] {app}')

    def installApplication(self, applicationTypeName, applicationName):
        if not self.checkApplicationType(applicationTypeName):
            return
        apps = self.applications[applicationTypeName]
        if not self.checkApplicationName(applicationName, apps):
            return
        self._installApp(applicationTypeName, applicationName)

    def _installApp(self, appType, appName):
        print(f"Installing {appName} [{appType}]")
