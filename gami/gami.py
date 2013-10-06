from fabric.tasks import execute
from fabric.colors import yellow, green, blue, red
from fabric.api import env, cd, prefix, sudo as _sudo, run as _run, hide, task

from fabfile import *
import sys


###########################################
# Utils and wrappers for various commands #
###########################################

# from Mezzanine::

def _print(output):
    print
    print output
    print


def print_command(command):
    _print(blue("$ ", bold=True) +
           yellow(command, bold=True) +
           red(" ->", bold=True))
           
           
def command_switcher(arguments):
    if len(arguments) < 2:
        _print(red("Command not found.  Here is a list of the available commands.", bold=True))
        _print(green(local('fab --list')))
    else:
        cmd_string = "'" + "','".join(arguments[2:])+"'" 
        local("fab "+arguments[1] + ":" + cmd_string)
        


if __name__ == "__main__":
    # Parse command line arguments for gami
    command_switcher(sys.argv)
