#!/usr/bin/python3
#simple_create : irfanDect

from prettytable import PrettyTable
from rich import print
from rich.syntax import Syntax
from rich.align import Align
from rich.panel import Panel
import subprocess
from rich import box

# yang benerrr

# yang benner

log = Align.center(
        """
╔╦╗  ╔═╗  ╔╗   ╦    ╔═╗  ╔╦╗
 ║   ╠═╣  ╠╩╗  ║    ║╣    ║║
 ╩   ╩ ╩  ╚═╝  ╩═╝  ╚═╝  ═╩╝
        """
        )
# yang benner..
try:
    class started():
        def __init__(self,banner):
            self.show_banner = banner
       
        @classmethod 
        def _banner(self):
            print(Panel(log,box=box.DOUBLE))

        @classmethod
        def tabled(self,
                headers="name|size",
                rows="udin|30",
                spliter="|",
                align="r",
                border=False,
                show_lines=False):

            """ prettytable tabl3s"""
            try:
                y = f"{headers}".split(f'{spliter}')
                x = PrettyTable(y)
                x.align='l'
                table=(f"{rows}".lower())
                z=[z for z in table.split('\n') if z]
                for z in z:
                    x.add_row(z.strip().split(f'{spliter}'))
                x.border=border
                x._hrules=show_lines
                x.horizontal_char = "─"
                x.vertical_char = "│"
                x.junction_char = "┼"
                x.top_junction_char = "┬"
                x.bottom_junction_char = "┴"
                x.right_junction_char = "┤"
                x.left_junction_char = "├"
                x.top_right_junction_char = "┐"
                x.top_left_junction_char = "┌"
                x.bottom_right_junction_char = "┘"
                x.bottom_left_junction_char = "└"
                return x
            except ValueError:
                print("[red bold]ValueError...")
            except AttributeError:
                print("[red bold]No Attribute")
except TypeError:
    pass

# example
class M(started):
    def __init__(self):
        super().__init__(Panel(log))
