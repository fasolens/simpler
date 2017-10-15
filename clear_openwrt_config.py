#!/usr/bin/python3
"""This script clean OpenWRT/LEDE config file.

It takes as argument path to config file to clean.
New file is generated with the same name as argument
plus `_clean` postfix.
"""
import sys


if len(sys.argv) < 2:
    print("It takes one argument, path to config file.")
    exit(-1)

config_file = []
with open(sys.argv[1], 'r') as f:
    config_file = f.readlines()
    f.close()


with open(sys.argv[1]+"_clean", 'w') as f:
    for line in config_file:
        if line.strip():
            if line.lstrip()[0] != "#":
                f.write(line)
