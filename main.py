
import random
from rich import box
from rich.align import Align
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.progress import Progress
from rich.console import Console, Group

console = Console()

with Progress() as progress:
    task = progress.add_task("[cyan]Processing...", total=100)
    for i in range(100):
        progress.update(task, advance=1)
