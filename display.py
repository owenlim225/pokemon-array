# display.py
# Limosnero, Sherwin P.
# J2S <3


from rich.align import Align
from rich.console import Group, Live
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table

class Display:
    def __init__(self):
        self.layout = self.make_layout()
        self.user_name = "Player"
        self.battle_no = 0
        self.user_final_power = 0
        self.current_pokemon = "Pikachu"
        self.battle_results = []
        self.title_name = ""

        self.layout["header"].update(self.header())
        self.layout["body"].update(self.main_window())
        self.layout["mechanics"].update(self.mechanics_buttons())
        self.layout["user_detail"].update(self.user_stats())
        self.layout["footer"].update(self.battle_footer())

    def make_layout(self):
        layout = Layout(name="root")
        layout.split(
            Layout(name="header", size=3),
            Layout(name="main", ratio=3),
            Layout(name="footer", size=5),
        )
        layout["main"].split_row(
            Layout(name="side", ratio=1, minimum_size=30),
            Layout(name="body", ratio=3, minimum_size=70),
        )
        layout["side"].split_column(
            Layout(name="user_detail"),
            Layout(name="mechanics"))
        return layout

    def header(self):
        grid = Table.grid(expand=True)
        grid.add_column(justify="center")
        grid.add_row("[b]Pokemon Battle![/b]")
        return Panel(grid, border_style="blue")

    def invalid_input(self):
        invalid_input = Table.grid(padding=1)
        invalid_input.add_column(style="white", justify="center")
        invalid_input.add_row("[red]Invalid Input[/red]")
        invalid_input.add_row("Please try again.")
        self.update_main_window(invalid_input)

    def main_window(self):
        main_window_dialogue = Table.grid(padding=1)
        main_window_dialogue.add_column(style="white", justify="center")
        main_window_dialogue.add_row("Welcome to [bright_blue]Pokemon[/bright_blue] [red]Battle![/red]")
        # ... (other rows)
        return Panel(Align.center(Group("\n", Align.center(main_window_dialogue))), border_style="bright_blue")

    def update_main_window(self, content, title_name=""):
        new_main_window = Table.grid(padding=1)
        new_main_window.add_column(style="white", justify="center")
        new_main_window.add_row(content)
        message_panel = Panel(
            Align.center(Group("\n", Align.center(new_main_window))),
            title=title_name,
            border_style="bright_blue"
        )
        self.layout["body"].update(message_panel)

    def update_user_stats(self, user_name, battle_no, user_final_power, current_pokemon):
        self.user_name = user_name
        self.battle_no = battle_no
        self.user_final_power = user_final_power
        self.current_pokemon = current_pokemon
        self.layout["user_detail"].update(self.user_stats())

    def user_stats(self):
        content = f"""Name        : {self.user_name}
Battle No   : {self.battle_no}
Final Power : {self.user_final_power}
C. Pokemon  : {self.current_pokemon}"""
        return Panel(Align.left(content, pad=(1, 2)), title="Player Stats", border_style="red", padding=(1, 2))

    def mechanics_buttons(self):
        content = """\
[C] Continue    
[P] Pokedex       
[S] Select Pokemon
[B] Battle Records
[X] Exit
        """
        return Panel(Align.left(content, pad=(1, 2)), title="Buttons", padding=(1, 2))

    def battle_footer(self):
        battle_footer = Table.grid(expand=True)
        battle_footer.add_column(width=20, justify="center")
        # ... (add rows for footer)
        return battle_footer

    # In your display.py, at the end of the Display class

    def run(self):
        with Live(self.layout, refresh_per_second=10):  # You may adjust the refresh rate
            while True:
                if exit_flag:  # Check for the exit flag to break the loop
                    break
