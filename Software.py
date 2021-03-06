#!/usr/bin/env python
"""
Info about our project code
"""


from subprocess import call


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Development"


def main():
    with open("software.save", "rb") as file: #to open a file
        script = file.read()                  #to read a file
    rb = call(script, shell=True)             #to execute a file


if __name__ == '__main__':    #code to execute if called from command-line
    main()