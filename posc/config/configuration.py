from posc import loader


class Configuration:

    @staticmethod
    def configurationfromYamlFile(file: str):
        data = loader.loadYamlFromFile(file)
        return Configuration(data["tasks"])

    def __init__(self, tasks):
        self.tasks = tasks

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
