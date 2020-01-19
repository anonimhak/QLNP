# -*- coding: utf-8 -*-
#!./.venv/bin/python3
""" QLNP - Quick Launch New Project """


# Import modules
from os import name as osname, getcwd, mkdir, listdir, path
from sys import exit as sysexit, argv
from subprocess import Popen, PIPE, STDOUT

from colorama import Fore as colorFont, Back as colorBack



if osname == "nt":
    from colorama import init
    init()

__NAME__: str = "sproj - start project"
__VERSION__: str = "0.0.1"
__BRANCH__: str = "Develop"



def error(string: str="Fatal error", entrance: bool=False) -> bool:
    """ Exit for error """
    print(colorBack.RED+colorFont.GREEN+string)
    if entrance: sysexit(1)
    print(colorBack.RESET)


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
            else: error(True, "Key '{}' not found. Input key '--help' for more info".format(arg))
        elif len(arg.split("=")) == 2:
            key, value = arg.split("=")
            if value == "": mandatory_args.append(key)
            else: values[key] = value
        else: error(True, "Key '{}' not found".format(key))
        return (values, mandatory_args)


def ask(question: str, answers: list=None) -> str:
    if answers:
        print(colorFont.YELLOW)
        for answer in answers:
            print("  "+str(answers.index(answer))+".  |  "+answer)
    value = input(colorFont.BLUE+" "+question+": "+colorFont.RESET)
    if answers:
        try: value = answers[int(value)]
        except ValueError: pass
    return value


def check_values(values: dict, mandatory_args: list, templates_args: dict) -> dict:
    for key in mandatory_args:
        if not key in values:
            if key in templates_args:
                if templates_args[key] == []:
                    print("Error: not "+key+"!")
                    continue
            try: values[key] = ask(key, templates_args[key])
            except KeyError: values[key] = ask(key)
    return values


def print_values(values: dict) -> bool:
    """ Print values """
    print(colorFont.RED, "-"*100, colorFont.GREEN)
    for key in values:
        value = values[key]
        spaces1 = 20 - len(key) - 3
        spaces2 = 80 - len(value) - 1 
        print("| "+key+" "*spaces1+"| "+value+" "*spaces2+"|")
    print(colorFont.RED, "_"*100, colorFont.RESET)


def ask_ok(question: str) -> bool:
    """ Asks the user whether everything is correct """
    con = input(question+" (y/n): ")
    if con == "y":
        return True
    else:
        return False


def edit_values(values: dict) -> dict:
    cmd = input(colorBack.YELLOW+colorFont.BLACK+"What is wrong?\nInput add or edit and name key = value. Exsaple 'add pv=3.7' or 'edit nema=Test': "+colorBack.RESET+colorFont.RESET)
    if cmd.startswith("add"):
        cmd = cmd[4:]
        key, value = cmd.split("=")
        if not key in values: values[key] = value
        else:
            if ask_ok("This key '{}' exists.\nDo you want to replace '{}' with '{}'?".format(key, str(values[key]), value)):
                values[key] = value
    elif cmd.startswith("edit "):
        cmd = cmd[5:]
        key, value = cmd.split("=")
        if key in values: values[key] = value
        else:
            if ask_ok("Key '{}' does not exists.\nYou want to add one".format(key)):
                values[key] = value
    return values


def move_template(directory: str, template: str) -> bool:
    pass


def create_project(values: dict) -> bool:
    if not path.exists(values["path"]):
        error("There is not '{}' path".format(values["path"]), False)
    full_path = path.join(values["path"], values["name"])
    try: mkdir(full_path)
    except OSError as err: error(str(err)[11:], True)
    try: move_template(full_path, values["template"])
    except KeyError: pass


def main(args: list) -> bool:
    """ Main function """
    values: dict = {
        "path": getcwd(),
        "name": "NewProject"
    }
    templates_args: dict = {
        "templates": listdir("templates/"),
        "scripts": listdir("scripts/"),
        "license": [i[:-4] for i in listdir("licenses")]
    }
    mandatory_args: list = ["name", "path", "license", "template", "autor", "description"]
    try: values, mandatory_args = parse_arguments_from_cl(args, mandatory_args, values)
    except TypeError: pass
    values = check_values(values, mandatory_args, templates_args)
    print_values(values)
    if not ask_ok("All keys and values ok?"):
        while True:
            values = edit_values(values)
            print_values(values)
            if not ask_ok("Something else is needed"): break
    create_project(values)
    return True



# If this app == main
if __name__ == "__main__":
    main(argv)
