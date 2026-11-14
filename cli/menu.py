from rich.console import Console
from rich.panel import Panel
from task import Task  # noqa: F401


class Menu:
    def __init__(self, name):
        self.name = name
        self.user_choice = None
        self.console = Console()
        self.cli_menu()
        self.input_handling()

    def input_handling(self):
        self.user_choice = input("Enter your choice: ")
        match self.user_choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case _:
                print("Invalid Input")

    def cli_menu(self):

        choices = {
            "1": "Add A Task",
            "2": "View Tasks",
            "3": "Edit Task",
            "4": "Delete Task",
            "5": "Exit",
        }
        menu_options = "\n".join(
            f"{number},{option}" for number, option in choices.items()
        )
        self.console.print(
            Panel(
                f"[cyan]Welcome {self.name} to Task Manager.[/cyan]\n"
                "[dim]Please select an option from the menu below.[/dim]\n"
                f"[magenta bold]{menu_options}[/magenta bold]\n",
                title="[bold]MAIN MENU[/bold]",
                border_style="blue",
                padding=(1, 2),
            )
        )
