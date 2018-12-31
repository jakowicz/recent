#!/usr/bin/env python

"""
This script is currently responsible for reading you accounts ~/.zsh_history file and processing it to show which commands you more frequently run for the program you specify.

This script can be executed by running `./recent.py <program>' e.g. `./recent.py gpg', which will show you which gpg files arein your zsh history.

To get the full effect of this you should ensure your zsh history length is set inside you ~/.zshrc file, by adding the following: `export HISTSIZE=10000000000`. That's 10 billion bytes, the default is 10k bytes.

Features to be added:
 - Add support for bash and fish
 - Add support for when multiple commands are run using 'and'
 - Add support to return output as json
 - Allow count to be passed as a parameter
"""

from termcolor import colored
from operator import itemgetter

import os
import hashlib
import sys

class RecentCommands:
    def __init__(self):
        self.recent_commands = []

    def get_recent_commands(self):
        return self.recent_commands

    def register_command(self, command):
        for recent_command in self.recent_commands:
            if recent_command["hash"] == get_command_hash(command):
                recent_command["count"] = recent_command["count"] + 1
                return

        self.recent_commands.append({
            "hash": get_command_hash(command),
            "command": command,
            "count": 1
        })

def history_file_lines():
    homedir = os.path.expanduser("~")

    return open("{0}/.zsh_history".format(homedir), "r")

def is_command_valid(command):
    single_quotes = command.count('\'')
    double_quotes = command.count('"')

    return single_quotes % 2 == 0 and double_quotes % 2 == 0

def get_command_hash(command):
    return hashlib.sha1(command).hexdigest()

def is_program_valid(filter_by_program, program):
    return "=" not in program and program == filter_by_program

def print_recent_commands(count, commands):
    print("\nRecent executions:\n")

    for command in commands:
        print(colored("{0}".format(command["command"].strip()), "yellow"))
        print(colored(" > COUNT: {0}\n".format(command["count"]), "white"))

        count = count - 1

        if count == 0:
            break

def init(program_filter):

    rec_comms = RecentCommands()

    for history_record in history_file_lines():

        # loop over each command separated by ;
        for history_command in history_record.split(";")[1:]:

            history_command = history_command.strip()
            program = history_command.split(" ", 2)[0]

            if is_program_valid(program_filter, program) and is_command_valid(history_command):
                rec_comms.register_command(history_command)

    commands_ordered_by_count = sorted(rec_comms.get_recent_commands(), key=itemgetter('count'), reverse=True)

    print_recent_commands(5, commands_ordered_by_count)


if __name__ == '__main__':
    init(sys.argv[1])
