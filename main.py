# -*- coding: utf-8 -*-
#!./.venv/bin/python3
""" QLNP - Quick Launch New Project """


# Import modules
from os import name as osname, getcwd, listdir
from sys import exit as sexit, argv
from subprocess import Popen, PIPE, STDOUT

from colorama import Fore as color



if osname == "nt":
    from colorama import init
    init()

__NAME__: str = "QLNP"
__VERSION__: str = "0.0.1"
__BRANCH__: str = "Develop"



def errexit(string: str) -> bool:
    """ Exit for error """
    print(string)
    sexit(1)


def parse_arguments_from_cl(args: list, mandatory_args: list, values: dict) -> tuple:
    """ Parse argument from command line """
    for arg in args:
        if arg.endswith(".py"):
            continue
        elif (arg.startswith("-") or arg.startswith("--")):
            if (arg == "-h" or arg == "--help"): pass
            elif (arg == "-a" or arg == "--about"): pass
            elif (arg == "-v" or arg == "--version"): print(__VERSION__)
            elif (arg == "-b" or arg == "--branch"): print(__BRANCH__)
            else: errexit("Key '"+arg+"' not found. Input key '--help' for more info")
        elif len(arg.split("=")) == 2:
            key, value = arg.split("=")
            if value == "": mandatory_args.append(key)
            else: values[key] = value
        else: errexit("Key '"+key+"' not found")
        return (values, mandatory_args)


def ask(question: str, answers: list=None) -> str:
    if answers:
        for answer in answers:
            print("  "+str(answers.index(answer))+".  |  "+answer)
    value = input(question)
    if answers:
        try: value = answers[int(values)]
        except ValueError: pass
    return value


def check_values(values: dict, mandatory_args: list, templates_args: dict) -> dict:
    for key in mandatory_args:
        if not key in values:
            try: values[key] = ask(key, templates_args[key])
            except KeyError: values[key] = ask(key)
    return values


def main(args: list) -> bool:
    """ Main function """
    values: dict = {
        "path": ".",
        "name": "NewProject"
    }
    templates_args: dict = {
        "templates": listdir("templates/"),
        "scripts": listdir("scripts/")
    }
    mandatory_args: list = ["name", "path"]
    try: values, mandatory_args = parse_arguments_from_cl(args, mandatory_args, values)
    except TypeError: pass
    values = check_values(values, mandatory_args, templates_args)
    return True



# If this app == main
if __name__ == "__main__":
    main(argv)
