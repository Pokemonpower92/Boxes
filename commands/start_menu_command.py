from commands import command


class StartMenuCommand(command.Command):
    def execute(self) -> None:
        """Start the sim scene."""
        print("We're starting the main menu")
