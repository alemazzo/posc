
class ConfigurationParser:

    @staticmethod
    def parse(yaml_object):
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
