# -*- coding: utf-8 -*-
#!./.venv/bin/python3
""" QLNP - Quick Launch New Project """


# Import modules
from os import name as osname, getcwd
from sys import exit as sexit, argv, path, stdout
from json import load as j_load
from subprocess import Popen, PIPE, STDOUT

from yaml import load as y_load
from colorama import Fore as color



if osname == "nt":
    from colorama import init
    init()

__NAME__: str = "QLNP"
__VERSION__: str = "0.0.1"
__BRANCH__: str = "Develop"



def main(args: list) -> bool:
    values: dict = {
        "path": ".",
        "name": "NewProject"
    }
    templates_args: dict = {
        "templates": lambda: for i in listdir("templates/"): print(i),
        "scripts": lambda: for i in listdir("scripts/"): print(i)
    }
    return True



# If this app == main
if __name__ == "__main__":
    main()
