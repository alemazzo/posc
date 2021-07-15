class Application:

    @staticmethod
    def fromObject(obj, apptype):
        if type(obj) is dict:
            name = list(obj.keys())[0]
            version = obj.get(name).get("version")
            return Application(name, apptype, version)

        return Application(obj, apptype)

    def __init__(self, name, apptype, version=None):
        self.name = name
        self.apptype = apptype
        self.version = version

    def __str__(self):
        return f"{self.name} [{self.apptype}]" + (f"(v: {self.version})" if not self.version is None else "")
