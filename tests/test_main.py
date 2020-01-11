# -*- coding: utf-8 -*-
#!./.venv/bin/python3
""" Tests for main function 'main.py' """

# Import modules
from os import getcwd
from sys import path
path.append(getcwd())
from main import *

def test__parse_arguments_from_cl():
    assert parse_arguments_from_cl(
        ["name=TeSt", "templates=", "scripts=gitinit.yaml"],
        ["name"],
        {"path": "."}
    ) = (
        {"path": ".", "name": "TeSt", "scripts": "gitinit.yaml"},
        ["name", "templates"]
    )
